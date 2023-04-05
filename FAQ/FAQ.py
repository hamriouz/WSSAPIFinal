import asyncio
import json

from flask import Flask, request, jsonify, make_response

from Exceptions import InvalidQuestionException, NoQuestionAsked

from FAQ_handler import FAQHandler


app = Flask(__name__)


@app.route('/FAQ/Ask', methods=['POST'])
# @check_role
def ask_question():
    try:
        request_handler = FAQHandler()
        faq_input = json.loads(request.data)
        answer = request_handler.get_response(faq_input)
        return make_response(jsonify(answer), 200)

    except InvalidQuestionException:
        message = {"Invalid question! Please contact our admins for more information."}
        return make_response(jsonify(message), 400)

    except NoQuestionAsked:
        message = {"No question asked! Please type in your question."}
        return make_response(jsonify(message), 401)


if __name__ == '__main__':
    asyncio.run(app.run(host="127.0.0.1", port="80"))
