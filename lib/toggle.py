import tkinter as tk


class ToggleSwitch(tk.Frame):
    def __init__(self, stopwatch, **kwargs):
        tk.Frame.__init__(self, **kwargs)
        self._stopwatch = stopwatch
        self._start = tk.Button(
            self, text="Start", command=self._stopwatch.start
            )
        self._stop = tk.Button(
            self, text="Stop", command=self._stopwatch.stop
            )
        self._reset = tk.Button(
            self, text="Reset", command=self._stopwatch.reset
            )

        for i in (self._start, self._stop, self._reset):
            i.pack(side=tk.LEFT, padx=10)
    
