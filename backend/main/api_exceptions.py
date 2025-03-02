
class UnAuthorized(Exception):
    pass

class SpotifyError(Exception):
    def __init__(self, error_dict):
        self.error

class APIError(Exception):

    def __init__(self, exception, error, traceback):
        super().__init__()

        self.exception = exception
        self.error_details = error
        self.error_description = None
        self.traceback = str(traceback)
        self.type = self.exception.__class__.__name__
        self.status_code = 500
        self.message = "Something went wrong, please contact admin."

        if isinstance(exception, KeyError):
            self.error_description = 'Accessing a key that does not exist in object'
            self.status_code = 500
        

        if isinstance(exception, UnAuthorized):
            self.status_code = 401
            self.message = error

        if isinstance(exception, SpotifyError):
            self.status_code = exception.error_dict['status']
            self.message = exception.error_dict['message']

    

    def __str__(self):
        return self.exception.__str_()
    
    def __dict__(self):
        return {'status': 0, 'message': self.message, 'status_code': self.status_code}
        