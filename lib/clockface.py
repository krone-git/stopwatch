import tkinter as tk
import datetime


class ClockFace(tk.Frame):
    def __init__(self, stopwatch, **kwargs):
        tk.Frame.__init__(self, **kwargs)
        self._stopwatch = stopwatch
        self._duration_var = tk.StringVar(self)
        self._face = tk.Label(self, textvariable=self._duration_var)
        self._face.pack()
        self.update_clockface()

    def update_clockface(self):
        clock = datetime.datetime.min + self._stopwatch.timedelta
        self._duration_var.set(clock.strftime("%H:%M:%S"))
        self._face.after(1, self.update_clockface)
