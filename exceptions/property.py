class PropertyInfoException(Exception):
    """[Main Exceptions Class]"""
    ...

class PropertyInfoNotFoundError(PropertyInfoException):
    def __init__(self):
        """[return 404: Exception Response]"""
        self.status_code = 404
        self.detail = "Property Info Not Found"

class PropertyInfoInfoAlreadyExistError(PropertyInfoException):
    def __init__(self):
        """[return 404: Defined Exception Response]"""
        self.status_code = 409
        self.detail = "Property Info Already Exists"
