class ApiError(Exception):
    def __init__(self, message, status_code):
        self.status_code = status_code
        self.message = message


class ExistError(ApiError):
    pass


class NotExistError(ApiError):
    pass


class PasswordValidationError(ApiError):
    pass


class PhoneNumberValidationError(ApiError):
    pass


class InsertFailError(ApiError):
    pass


class NotMatchError(ApiError):
    pass
