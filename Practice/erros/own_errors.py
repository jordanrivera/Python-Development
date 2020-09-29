class RuntimeErrorWithCode(TypeError):
    """Exception raised when a specific error is needed"""

    def __init__(self, message, code):
        super().__init__(f'Error code {code} {message}')
        self.code = code


err = RuntimeErrorWithCode('An error happend.', 500)
print(err.__doc__)


