from separate_and_choose_input import SeparateAndChooseInput as sep
import json
import numpy.random as random

# import flask
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# linebotTest1
from flask import Flask

app = Flask(__name__)

# [待填]channel access token
line_bot_api = LineBotApi("輸入channel access token")
# [待填]channel secret
handler = WebhookHandler("輸入channel secret")

# load dictionary of separated responses
with open("response_dict.json") as f:
    response_dict = json.load(f)

# load responses to a list
with open("all_sentences/responses.txt") as f:
    response_list = f.readlines()


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # 獲得使用者輸入的訊息
    body = request.get_data(as_text=True)
    try:
        # 送出訊息
        handler.handle(body, signature)
    except InvalidSignatureError:
        # 送出Bad request (400)
        abort(400)
    # 回覆OK
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
# 加入一個handle_message function
def handle_message(event):
    try:
        sep.pickMeaningfulWord(event.message.text) in response_dict
        output_sentence = response_list[
            random.choice(response_dict[sep.pickMeaningfulWord(event.message.text)])
        ].strip()
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=output_sentence)
        )
    except Exception:
        output_sentence = "加油！"
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=output_sentence)
        )


if __name__ == "__main__":
    app.run(port=5002)
