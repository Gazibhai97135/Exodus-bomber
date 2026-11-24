import os
import threading
from main import app
from bot import start_bot

if __name__ == "__main__":
    # 1. Start the Telegram bot in a background thread
    # We pass the PORT so bot.py knows where to find the Flask API
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting bot... looking for API on port {port}")
    start_bot(port)

    # 2. Start the Flask Web Server (This satisfies Render's port scanner)
    # We disable the reloader to prevent double-starting the bot
    print(f"Starting Flask web server on port {port}...")
    app.run(host="0.0.0.0", port=port, use_reloader=False)
