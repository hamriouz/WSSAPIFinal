from Exceptions import NoQuestionAsked
from FAQ_domain import FAQDomain


class FAQHandler:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FAQHandler, cls).__new__(cls)
            print(cls)
        return cls.instance

    @staticmethod
    def get_response(asked_question):
        question = asked_question["question"]
        if question is None:
            raise NoQuestionAsked
        else:
            faq_domain = FAQDomain()
            response = faq_domain.get_response(question)
            return response

