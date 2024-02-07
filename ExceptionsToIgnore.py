from contextlib import contextmanager


class ExceptionsToIgnore:
    def __init__(self, exception_types):
        """
        Initialize the NoExceptions context manager.

        :param exception_types: List of exception types to be ignored.
        """
        self.exception_types = exception_types

    @contextmanager
    def handle_exceptions(self):
        """
        Context manager that catches and optionally ignores specified exceptions.
        """
        try:
            yield
        except Exception as e:
            if not any(isinstance(e, exception_type) for exception_type in self.exception_types):
                raise e
            else:
                print(f"Ignoring exception {e}")

    def __enter__(self):
        """
        Called when entering the 'with' block.

        :return: The 'handle_exceptions' context manager.
        """
        return self.handle_exceptions()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Called when exiting the 'with' block.

        :param exc_type: Type of the exception that occurred (or None if no exception).
        :param exc_value: The exception instance (or None if no exception).
        :param traceback: The traceback object (or None if no exception).
        :return: Always returns False to indicate that exceptions should propagate.
        """
        return False



