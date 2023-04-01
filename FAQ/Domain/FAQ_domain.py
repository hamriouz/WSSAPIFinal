class FAQDomain:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FAQDomain, cls).__new__(cls)
            print(cls)
        return cls.instance

    @staticmethod
    async def get_response(question):

    # TODO
    #  call model, ask question and get answer

    