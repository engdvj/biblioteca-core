from django.utils.deprecation import MiddlewareMixin

import logging
logger = logging.getLogger(__name__)

class TokenCookieMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get('auth_token')
        if token:
            request.META['HTTP_AUTHORIZATION'] = f'Token {token}'
            logger.info(f'Token {token} adicionado ao cabeçalho Authorization')
