# 🌐 Using IT Ticket Severity Calculator with ngrok

## What is ngrok?

ngrok creates a secure tunnel to your localhost, allowing you to share your local server with anyone on the internet.

## Setup Instructions

### Step 1: Start the Server

First, make sure your server is running:

```bash
python run_server.py
```

You should see:
```
🚀 Starting IT Ticket Severity Calculator Server...
🌐 Server will be available at: http://localhost:8000
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Start ngrok

Open a NEW terminal/command prompt and run:

```bash
ngrok http 8000
```

You'll see output like:
```
Session Status                online
Forwarding                    https://abc123.ngrok.io -> http://localhost:8000
```

### Step 3: Share the URL

Copy the `https://abc123.ngrok.io` URL and share it with anyone!

They can access:
- **Web Interface**: https://abc123.ngrok.io
- **API Documentation**: https://abc123.ngrok.io/docs
- **Health Check**: https://abc123.ngrok.io/health

## ✅ Fixed Issues

The web interface now automatically detects whether it's running on:
- localhost (http://localhost:8000)
- ngrok (https://your-url.ngrok.io)
- Any other domain

No configuration needed - it just works!

## 🧪 Testing with ngrok

### Test the API:
```bash
curl https://your-url.ngrok.io/health
```

### Test a prediction:
```bash
curl -X POST "https://your-url.ngrok.io/predict" \
     -H "Content-Type: application/json" \
     -d '{"ticket_text": "Server is down"}'
```

## 📝 Important Notes

1. **Keep Both Running**: Keep both the Python server AND ngrok running
2. **Free Tier Limits**: ngrok free tier has session time limits
3. **URL Changes**: Each time you restart ngrok, you get a new URL
4. **Security**: Anyone with the URL can access your server

## 🔒 Security Tips

For production use:
1. Use ngrok authentication: `ngrok http 8000 --auth="username:password"`
2. Set up proper CORS restrictions in `api/app.py`
3. Add rate limiting
4. Use environment variables for sensitive data

## 🐛 Troubleshooting

### "Failed to fetch" error:
✅ **FIXED!** The web interface now uses dynamic URLs.

### ngrok not found:
Install ngrok from https://ngrok.com/download

### Connection refused:
Make sure the Python server is running on port 8000

### Slow responses:
First prediction takes 5-10 seconds (model loading), then it's fast

## 📊 Example Usage

1. **Start Server**:
   ```bash
   python run_server.py
   ```

2. **Start ngrok** (in new terminal):
   ```bash
   ngrok http 8000
   ```

3. **Share URL**:
   ```
   https://abc123.ngrok.io
   ```

4. **Test**:
   - Open the URL in browser
   - Enter a ticket description
   - Click "Analyze Severity"
   - See results!

## 🎉 You're Ready!

The application now works seamlessly with ngrok. Share your URL and let others test the IT Ticket Severity Calculator!
