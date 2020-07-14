from stopwatch import StopWatch
from clockface import ClockFace
from toggle import ToggleSwitch
import tkinter as tk


class StopWatchWidget(tk.Frame):
    def __init__(self, **kwargs):
        tk.Frame.__init__(self, **kwargs)
        self._stopwatch = StopWatch()
        self._face = ClockFace(self._stopwatch, master=self)
        self._toggle = ToggleSwitch(self._stopwatch, master=self)
        self._face.pack(side=tk.TOP, pady=5, padx=10)
        self._toggle.pack(side=tk.TOP, pady=5, padx=10)
