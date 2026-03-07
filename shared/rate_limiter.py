"""Token-bucket rate limiter for API calls."""
import time
import threading


class RateLimiter:
    """
    Token-bucket rate limiter.

    Args:
        calls_per_second: Maximum number of calls allowed per second.
    """

    def __init__(self, calls_per_second: float = 1.0):
        self.calls_per_second = calls_per_second
        self.min_interval = 1.0 / calls_per_second
        self._lock = threading.Lock()
        self._last_call = 0.0

    def wait(self) -> None:
        """Block until the next call is allowed."""
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_call
            wait_time = self.min_interval - elapsed
            if wait_time > 0:
                time.sleep(wait_time)
            self._last_call = time.monotonic()

    def __call__(self, func):
        """Decorator usage: @rate_limiter"""
        import functools

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.wait()
            return func(*args, **kwargs)

        return wrapper
