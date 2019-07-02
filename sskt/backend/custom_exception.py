class NullResultQueryException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '\n'.join(['Query result not exist, info: ', ErrorInfo])
    def __str__(self):
        return self.ErrorInfo