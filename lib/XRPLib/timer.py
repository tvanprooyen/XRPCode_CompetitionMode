import time


class Timer:
    def __init__(self):
        """
        Create and start a timer.
        """
        self.reset()

    def reset(self):
        """
        Restart the timer from now.
        """
        self._start_ms = time.ticks_ms()

    def elapsed_ms(self):
        """
        :return: Elapsed time in milliseconds.
        """
        return time.ticks_diff(time.ticks_ms(), self._start_ms)

    def elapsed(self):
        """
        :return: Elapsed time in seconds as a float.
        """
        return self.elapsed_ms() / 1000

    def has_elapsed(self, seconds):
        """
        Return True once the given number of seconds has passed.

        :param seconds: Target elapsed time in seconds.
        :type seconds: float
        """
        return self.elapsed() >= seconds

    def has_elapsed_ms(self, milliseconds):
        """
        Return True once the given number of milliseconds has passed.

        :param milliseconds: Target elapsed time in milliseconds.
        :type milliseconds: int
        """
        return self.elapsed_ms() >= milliseconds


__all__ = ["Timer"]
