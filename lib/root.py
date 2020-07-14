from widget import StopWatchWidget
import tkinter as tk
from datetime import timedelta


class StopWatchRoot(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self._stopwatch1 = StopWatchWidget(master=self)
        self._stopwatch1.pack()

        self._stopwatch2 = StopWatchWidget(master=self)
        self._stopwatch2.pack()


root = StopWatchRoot()
root.mainloop()
