import time


class Retry(object):
    def __init__(self, tries, delay=0):
        """
        Decorator for retrying function if exception occurs

        tries -- no of retries
        delay -- wait between retries
        """
        self.tries = tries
        self.delay = delay

    def __call__(self, f):
        def fn(*args, **kwargs):
            exception = None
            for _ in range(self.tries):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    print("Retry, exception: " + str(e))
                    time.sleep(self.delay)
                    exception = e
            raise exception

        return fn
