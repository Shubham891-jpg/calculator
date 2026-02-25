import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import yaml
import os
import sys
import joblib

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.preprocessing.text_cleaner import TextCleaner
from src.preprocessing.language_detector import LanguageDetector
from src.preprocessing.translator import TextTranslator
from src.features.embeddings import MultilingualEmbeddings
from src.scoring.severity_scaler import SeverityScaler
from src.utils.logger import get_logger

logger = get_logger(__name__)

class SeverityModelTrainer:
    """Train IT ticket severity prediction model."""
    
    def __init__(self, config_path: str = "src/config/config.yaml"):
        """Initialize trainer with configuration."""
        self.config = self._load_config(config_path)
        
        # Initialize components
        self.text_cleaner = TextCleaner(
            remove_stopwords=self.config['preprocessing']['remove_stopwords'],
            lowercase=self.config['preprocessing']['lowercase']
        )
        self.language_detector = LanguageDetector()
        self.translator = TextTranslator()
        self.embeddings = MultilingualEmbeddings(
            model_name=self.config['features']['embedding_model']
        )
        self.scaler = SeverityScaler(
            min_score=self.config['scaling']['min_score'],
            max_score=self.config['scaling']['max_score']
        )
        
        # Model
        self.model = RandomForestRegressor(
            n_estimators=self.config['model']['n_estimators'],
            max_depth=self.config['model']['max_depth'],
            random_state=self.config['model']['random_state'],
            n_jobs=-1
        )
        
        # Data storage
        self.X_train = None
        self.X_val = None
        self.X_test = None
        self.y_train = None
        self.y_val = None
        self.y_test = None
        
    def _load_config(self, config_path: str) -> dict:
        """Load configuration from YAML file."""
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info(f"Configuration loaded from {config_path}")
            return config
        except Exception as e:
            logger.error(f"Failed to load config: {str(e)}")
            raise
    
    def load_data(self, data_path: str = "models/it_ticket_severity_dataset.csv") -> pd.DataFrame:
        """Load raw ticket data."""
        try:
            df = pd.read_csv(data_path)
            logger.info(f"Loaded {len(df)} tickets from {data_path}")
            
            # Rename columns to match expected format
            if 'DESCRIPTIONS' in df.columns:
                df = df.rename(columns={'DESCRIPTIONS': 'ticket_text'})
            
            # Basic data validation
            required_columns = ['ticket_text', 'severity_score']
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")
            
            # Remove rows with missing values
            df = df.dropna(subset=['ticket_text', 'severity_score'])
            logger.info(f"After removing missing values: {len(df)} tickets")
            
            return df
            
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            raise
    
    def preprocess_text(self, texts: list) -> list:
        """Preprocess text data with language detection and cleaning."""
        processed_texts = []
        
        logger.info("Starting text preprocessing...")
        
        for i, text in enumerate(texts):
            try:
                # Detect language
                language = self.language_detector.detect_language(text)
                
                # Clean text
                cleaned_text = self.text_cleaner.clean_text(text, language)
                
                # For Hindi text, we'll keep it as is since we're using multilingual embeddings
                # The multilingual model can handle both languages
                processed_texts.append(cleaned_text)
                
                if (i + 1) % 100 == 0:
                    logger.info(f"Processed {i + 1}/{len(texts)} texts")
                    
            except Exception as e:
                logger.warning(f"Failed to process text {i}: {str(e)}, using original")
                processed_texts.append(text)
        
        logger.info("Text preprocessing completed")
        return processed_texts
    
    def extract_features(self, texts: list) -> np.ndarray:
        """Extract features from preprocessed texts."""
        try:
            logger.info("Extracting multilingual embeddings...")
            
            # Use multilingual embeddings for feature extraction
            features = self.embeddings.encode_texts(texts, batch_size=32, show_progress=True)
            
            logger.info(f"Feature extraction completed. Shape: {features.shape}")
            return features
            
        except Exception as e:
            logger.error(f"Feature extraction failed: {str(e)}")
            raise
    
    def split_data(self, df: pd.DataFrame):
        """Split data into train, validation, and test sets."""
        try:
            # First split: train + val vs test
            train_val_df, test_df = train_test_split(
                df,
                test_size=self.config['data']['test_size'],
                random_state=self.config['data']['random_state'],
                stratify=None  # Can't stratify continuous targets
            )
            
            # Second split: train vs val
            val_size = self.config['data']['validation_size'] / (1 - self.config['data']['test_size'])
            train_df, val_df = train_test_split(
                train_val_df,
                test_size=val_size,
                random_state=self.config['data']['random_state']
            )
            
            logger.info(f"Data split - Train: {len(train_df)}, Val: {len(val_df)}, Test: {len(test_df)}")
            
            # Save split data
            os.makedirs("data/processed", exist_ok=True)
            train_df.to_csv("data/processed/train.csv", index=False)
            val_df.to_csv("data/processed/validation.csv", index=False)
            test_df.to_csv("data/processed/test.csv", index=False)
            
            return train_df, val_df, test_df
            
        except Exception as e:
            logger.error(f"Data splitting failed: {str(e)}")
            raise
    
    def prepare_features_and_targets(self, train_df: pd.DataFrame, 
                                   val_df: pd.DataFrame, 
                                   test_df: pd.DataFrame):
        """Prepare features and targets for training."""
        try:
            # Preprocess texts
            train_texts = self.preprocess_text(train_df['ticket_text'].tolist())
            val_texts = self.preprocess_text(val_df['ticket_text'].tolist())
            test_texts = self.preprocess_text(test_df['ticket_text'].tolist())
            
            # Extract features
            self.X_train = self.extract_features(train_texts)
            self.X_val = self.extract_features(val_texts)
            self.X_test = self.extract_features(test_texts)
            
            # Prepare targets
            self.y_train = train_df['severity_score'].values
            self.y_val = val_df['severity_score'].values
            self.y_test = test_df['severity_score'].values
            
            logger.info("Features and targets prepared successfully")
            
        except Exception as e:
            logger.error(f"Feature preparation failed: {str(e)}")
            raise
    
    def train_model(self):
        """Train the severity prediction model."""
        try:
            logger.info("Starting model training...")
            
            # Train the model
            self.model.fit(self.X_train, self.y_train)
            
            # Make predictions on training and validation sets
            train_pred = self.model.predict(self.X_train)
            val_pred = self.model.predict(self.X_val)
            
            # Fit scaler on training predictions
            self.scaler.fit(train_pred)
            
            # Scale predictions
            train_pred_scaled = self.scaler.transform(train_pred)
            val_pred_scaled = self.scaler.transform(val_pred)
            
            # Calculate metrics
            train_metrics = self._calculate_metrics(self.y_train, train_pred_scaled)
            val_metrics = self._calculate_metrics(self.y_val, val_pred_scaled)
            
            logger.info("Model training completed")
            logger.info(f"Training metrics: {train_metrics}")
            logger.info(f"Validation metrics: {val_metrics}")
            
            return train_metrics, val_metrics
            
        except Exception as e:
            logger.error(f"Model training failed: {str(e)}")
            raise
    
    def evaluate_model(self):
        """Evaluate model on test set."""
        try:
            logger.info("Evaluating model on test set...")
            
            # Make predictions
            test_pred = self.model.predict(self.X_test)
            test_pred_scaled = self.scaler.transform(test_pred)
            
            # Calculate metrics
            test_metrics = self._calculate_metrics(self.y_test, test_pred_scaled)
            
            logger.info(f"Test metrics: {test_metrics}")
            
            # Analyze prediction distribution
            score_distribution = self.scaler.get_score_distribution(test_pred_scaled.tolist())
            logger.info(f"Test prediction distribution: {score_distribution}")
            
            return test_metrics, test_pred_scaled
            
        except Exception as e:
            logger.error(f"Model evaluation failed: {str(e)}")
            raise
    
    def _calculate_metrics(self, y_true: np.ndarray, y_pred: np.ndarray) -> dict:
        """Calculate regression metrics."""
        return {
            'mse': float(mean_squared_error(y_true, y_pred)),
            'rmse': float(np.sqrt(mean_squared_error(y_true, y_pred))),
            'mae': float(mean_absolute_error(y_true, y_pred)),
            'r2': float(r2_score(y_true, y_pred)),
            'mean_pred': float(np.mean(y_pred)),
            'std_pred': float(np.std(y_pred)),
            'min_pred': float(np.min(y_pred)),
            'max_pred': float(np.max(y_pred))
        }
    
    def save_model(self, model_dir: str = "models"):
        """Save trained model and components."""
        try:
            os.makedirs(model_dir, exist_ok=True)
            
            # Save model
            model_path = os.path.join(model_dir, "severity_model.pkl")
            joblib.dump(self.model, model_path)
            
            # Save scaler
            scaler_path = os.path.join(model_dir, "severity_scaler.pkl")
            self.scaler.save_scaler(scaler_path)
            
            # Save embeddings model info (the model itself is cached by sentence-transformers)
            embeddings_info = {
                'model_name': self.embeddings.model_name,
                'embedding_dim': self.embeddings.embedding_dim
            }
            embeddings_path = os.path.join(model_dir, "embeddings_info.pkl")
            joblib.dump(embeddings_info, embeddings_path)
            
            logger.info(f"Model saved to {model_dir}")
            
        except Exception as e:
            logger.error(f"Failed to save model: {str(e)}")
            raise
    
    def run_full_training_pipeline(self):
        """Run the complete training pipeline."""
        try:
            logger.info("Starting full training pipeline...")
            
            # Load data
            df = self.load_data()
            
            # Split data
            train_df, val_df, test_df = self.split_data(df)
            
            # Prepare features and targets
            self.prepare_features_and_targets(train_df, val_df, test_df)
            
            # Train model
            train_metrics, val_metrics = self.train_model()
            
            # Evaluate model
            test_metrics, test_predictions = self.evaluate_model()
            
            # Save model
            self.save_model()
            
            logger.info("Training pipeline completed successfully!")
            
            return {
                'train_metrics': train_metrics,
                'val_metrics': val_metrics,
                'test_metrics': test_metrics
            }
            
        except Exception as e:
            logger.error(f"Training pipeline failed: {str(e)}")
            raise

def main():
    """Main training function."""
    try:
        trainer = SeverityModelTrainer()
        results = trainer.run_full_training_pipeline()
        
        print("\n" + "="*50)
        print("TRAINING COMPLETED SUCCESSFULLY!")
        print("="*50)
        print(f"Training R²: {results['train_metrics']['r2']:.4f}")
        print(f"Validation R²: {results['val_metrics']['r2']:.4f}")
        print(f"Test R²: {results['test_metrics']['r2']:.4f}")
        print(f"Test RMSE: {results['test_metrics']['rmse']:.2f}")
        print(f"Test MAE: {results['test_metrics']['mae']:.2f}")
        print("="*50)
        
    except Exception as e:
        logger.error(f"Training failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()