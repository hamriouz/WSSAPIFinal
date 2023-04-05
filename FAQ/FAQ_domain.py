import requests
import json

url = "https://wss.sadraei.tech/webhooks/rest/webhook"


class FAQDomain:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FAQDomain, cls).__new__(cls)
            print(cls)
        return cls.instance

    @staticmethod
    def get_response(question):
        print(question)
        payload = json.dumps({
            "sender": "test",
            "message": question
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()[0]['text']


    