import json

from flask import Flask, request, jsonify, make_response

from FAQ.Util.Exceptions import InvalidQuestionException, NoQuestionAsked

from FAQ.Handler.FAQ_handler import FAQHandler


app = Flask(__name__)


@app.route('/FAQ/Ask', methods=['GET'])
# do we need to check role?
# @check_role
async def ask_question():
    try:
        request_handler = FAQHandler()
        faq_input = await json.loads(request.data)
        answer = await request_handler.get_response(faq_input)
        return make_response(jsonify(answer), 200)

    except InvalidQuestionException:
        message = {"Invalid question! Please contact our admins for more information."}
        return make_response(jsonify(message), 400)

    except NoQuestionAsked:
        message = {"No question asked! Please type in your question."}
        return make_response(jsonify(message), 401)
