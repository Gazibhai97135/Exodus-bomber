import os
import threading
import time
from main import app
from bot import start_bot

def run_bot():
    # Give Flask a moment to bind to the port first
    time.sleep(2)
    port = int(os.environ.get("PORT", 5000))
    print(f"[Runner] Starting Telegram bot, pointing to API on port {port}...")
    success = start_bot(port)
    if not success:
        print("[Runner] ⚠️ Bot failed to start (check BOT_TOKEN)")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    # 1. Start Flask FIRST (this satisfies Render's port scanner)
    print(f"[Runner] Starting Flask on port {port}...")
    
    # Start the bot in a background thread AFTER Flask is configured
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # 2. Run Flask (blocking call, keeps the process alive)
    app.run(host="0.0.0.0", port=port, use_reloader=False)
