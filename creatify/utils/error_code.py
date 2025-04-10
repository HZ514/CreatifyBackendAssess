from typing import Dict, Optional
# from django.utils.translation import gettext_lazy as _

"""
错误码设计类，可以定制的返回更友好的错误信息。
"""


class ErrorCode:

    def __init__(
            self,
            code: str,
            message: str or Dict[str, str],
            http_status: int,
            default_lang: str = 'zh'
    ):
        self.code = code
        self.http_status = http_status
        self.default_lang = default_lang

        if isinstance(message, str):
            self.message_templates = {default_lang: message}
        else:
            self.message_templates = message

    def get_message(self, **kwargs) -> str:
        """根据本地化消息
        :param kwargs:
        :return:
        """
        # TODO: 目前写死为中文，实际使用时可以根据前端传递的参数或者后端配置使用不同的语言
        lang = self.default_lang
        template = (
                self.message_templates.get(lang) or
                self.message_templates.get('en') or
                list(self.message_templates.values())[0]
        )
        return template.format(**kwargs)


class APIErrors:
    """所有API错误码分类"""

    class Auth:
        INVALID_CREDENTIALS = ErrorCode(
            code='AUTH-1001',
            message={
                'zh': '邮箱或密码不正确',
                'en': 'Invalid email or password'
            },
            http_status=401
        )

        EMAIL_EXISTS = ErrorCode(
            code='AUTH-1002',
            message={
                'zh': '邮箱已被注册',
                'en': 'Email already registered'
            },
            http_status=409
        )

        PERMISSION_DENIED = ErrorCode(
            code='AUTH-1004',
            message={
                'zh': '没有操作权限',
                'en': 'Permission denied'
            },
            http_status=403
        )

    class Validation:
        MISSING_FIELD = ErrorCode(
            code='VALID-2001',
            message={
                'zh': '缺少必填字段: {field}',
                'en': 'Missing required field: {field}'
            },
            http_status=400
        )

        NOT_FOUND = ErrorCode(
            code='VALID-2004',
            message={
                'zh': '资源不存在',
                'en': 'Resource not found'
            },
            http_status=404
        )

        BAD_REQUEST = ErrorCode(
            code='VALID-2005',
            message={
                'zh': '非法请求',
                'en': 'Bad request'
            },
            http_status=400
        )

        DRF_VALIDATION_ERROR = ErrorCode(
            code='VALID-2006',
            message={
                'zh': '数据验证失败',
                'en': 'Validation error'
            },
            http_status=400
        )

    class System:
        INTERNAL_ERROR = ErrorCode(
            code='SYS-5001',
            message={
                'zh': '服务器内部错误',
                'en': 'Internal server error'
            },
            http_status=500
        )


if __name__ == '__main__':
    # 使用示例
    print(APIErrors.Auth.INVALID_CREDENTIALS.get_message())
    print(APIErrors.Validation.MISSING_FIELD.get_message(field='email'))