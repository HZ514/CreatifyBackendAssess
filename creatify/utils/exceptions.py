from creatify.utils.error_code import ErrorCode, APIErrors


class APIException(Exception):
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


if __name__ == '__main__':
    # 使用示例
    try:
        raise APIException(
            error_code=APIErrors.Auth.INVALID_CREDENTIALS
        )
    except APIException as e:
        print(e.to_dict())
