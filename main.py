import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
import model

logging.basicConfig(level=logging.DEBUG)
app = App(token=os.environ.get("SLACK_BOT_TOKEN"), signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))

@app.event("message")
def message_hello(say, body):
  logging.info(body)
  mention = body["event"]
  text = mention["text"]
  say(
        text=model.Post(text)
    )

# アプリを起動します
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 8080)))
