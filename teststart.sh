#!/usr/bin/env bash
cd "$(dirname "$0")"


trap "echo '⛔ Stopping bot...'; exit 0" SIGINT

# loop to auto-restart on crash
while true; do
  python3 -u test_bot.py
  echo "Bot stopped — restarting in 5s... (press Ctrl+C to stop)"
  sleep 5
done
