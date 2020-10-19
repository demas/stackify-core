
class DownloadQuestionsError(Exception):
    def __init__(self, status_code):
        self.message = "Error downloading questions"
        self.status_code = status_code
