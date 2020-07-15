import tkinter as tk
import datetime


class ClockFace(tk.Label):
    def __init__(self, clock, refresh=1, fmt_str="%H:%M:%S.%f",
                 master=None, **kwargs):
        self._clockface = tk.StringVar(master=master)
        kwargs.update(
            dict(
                master=master,
                textvariable=self._clockface
                )
            )
        tk.Label.__init__(self, **kwargs)
        self._clock = clock
        self._refresh = int(refresh)
        self._format_string = fmt_str
        self.update_clockface()

    def set_clock(self, clock):
        self._clock = clock
        return self

    def set_format_string(self, fmt_str):
        self._format_string = fmt_str
        return self

    def set_refresh_rate(self, rate):
        self._refresh = rate
        return self

    def update_clockface(self):
        clocktime = datetime.datetime.min + self._clock.timedelta
        self._clockface.set(clocktime.strftime(self._format_string))
        self.after(self._refresh, self.update_clockface)
        return self
