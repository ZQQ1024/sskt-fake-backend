import traceback

class NullResultQueryException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['Query result not exist.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo


class NoneUploadfileException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['None upload file.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class UploadfileExistedException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['Upload file existed.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class NoMatchingAppException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['No mathcing Application,', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class ConfirmCommentFailException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['Confirm comment failed.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class UserGroupErrorException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['User group error.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class GroupErrorException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['Group error.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class AddGroupErrorException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['Add user to group error.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class NameCollecErrorException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['Get name collection error.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo

class ApplicationInfoErrorException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = '  '.join(['Application info error.', ErrorInfo])

    def __str__(self):
        return self.ErrorInfo