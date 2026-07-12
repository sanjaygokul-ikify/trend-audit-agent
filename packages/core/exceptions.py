class AuditAgentException(Exception):
    pass

class InferenceException(AuditAgentException):
    def __init__(self, message: str):
        super().__init__(message)

class ExecutionException(AuditAgentException):
    def __init__(self, message: str):
        super().__init__(message)

class LoggingException(AuditAgentException):
    def __init__(self, message: str):
        super().__init__(message)

class QueryException(AuditAgentException):
    def __init__(self, message: str):
        super().__init__(message)

class LogNotFoundException(AuditAgentException):
    def __init__(self, message: str):
        super().__init__(message)
