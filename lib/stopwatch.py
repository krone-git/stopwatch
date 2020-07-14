import datetime


class StopWatch:
    def __init__(self):
        self._active = False
        self.reset()

    @property
    def timedelta(self):
        if self._active:
            self.tic()
        return self._duration

    @property
    def total_seconds(self):
        if self._duration:
            return self._duration.total_seconds()
        else:
            return 0

    def is_active(self):
        return self._active

    def toggle(self):
        if self._active:
            self.stop()
        else:
            self.start()
        return self

    def start(self):
        self._start = None
        self._active = True
        self.tic()
        return self

    def stop(self):
        self.tic()
        self._start = None
        self._active = False
        return self

    def reset(self):
        self._start = None
        self._duration = datetime.timedelta(0)
        return self

    def tic(self):
        if self._active:
            if self._start:
                self._duration += datetime.datetime.now() - self._start
            self._start = datetime.datetime.now()
        return self



if __name__ == "__main__":
    import time
    s = StopWatch()

    print(s.total_seconds)
    s.start()
    time.sleep(1)
    s.stop()
    print(s.total_seconds)

    time.sleep(2)

    s.start()
    time.sleep(1)
    s.stop()
    print(s.total_seconds)

    s.stop()
    print(s.total_seconds)
    time.sleep(1)
    s.stop()
    print(s.total_seconds)

    s.start()
    print(s.total_seconds)
    time.sleep(1)
    s.start()
    print(s.total_seconds)
    time.sleep(1)
    s.start()
    print(s.total_seconds)
    s.stop()
    print(s.total_seconds)

    s.start()
    time.sleep(1)
    s.stop()
    print(s.total_seconds)
    
