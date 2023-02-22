from result import Err, Ok


def handler(func):
    def wrapper(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            return Ok(data)
        except Exception as e:
            return Err(e)

    return wrapper


__all__ = [
    "handler"
]
