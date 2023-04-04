class InvalidQuestionException(Exception):
    def __init__(self):
        message = "Invalid question! Please contact our admins for more information"
        super().__init__(message)


class NoQuestionAsked(Exception):
    def __init__(self):
        message = "No question asked! Please type in your question."
        super().__init__(message)
