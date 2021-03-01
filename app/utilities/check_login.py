import logging
from functools import wraps

from fastapi.responses import RedirectResponse


def check_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("session_id"):
            logging.error("Session not found")
            return RedirectResponse("/")
        return func(*args, **kwargs)

    return wrapper
