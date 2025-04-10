from utils.error_code import ErrorCode, APIErrors

"""
通过在视图中抛出异常，在django中间件中捕获异常返回想要的错误信息格式。
也可以将所有的django自带异常做处理，返回自定义的错误异常。
"""


class MyAPIException(Exception):
    """基础API异常"""

    def __init__(
            self,
            error_code: ErrorCode,
            details=None,
            **message_kwargs
    ):
        self.error_code = error_code
        self.details = details or {}
        self.message = error_code.get_message(**message_kwargs)
        self.status_code = error_code.http_status

    def to_dict(self) -> dict:
        return {
            'code': self.error_code.code,
            'message': self.message,
            'details': self.details,
            'status': self.status_code
        }


class SystemException(MyAPIException):
    """邮箱已存在"""

    def __init__(self):
        super().__init__(
            error_code=APIErrors.System.INTERNAL_ERROR,
        )


class EmailExistsException(MyAPIException):
    """邮箱已存在"""

    def __init__(self):
        super().__init__(
            error_code=APIErrors.Auth.EMAIL_EXISTS,
        )


if __name__ == '__main__':
    # 使用示例
    try:
        raise MyAPIException(
            error_code=APIErrors.Auth.INVALID_CREDENTIALS
        )
    except MyAPIException as e:
        print(e.to_dict())

    try:
        raise EmailExistsException()
    except MyAPIException as e:
        print(e.to_dict())
