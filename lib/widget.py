from stopwatch import StopWatch
from clockface import ClockFace
from switch import ToggleSwitch
import tkinter as tk


class StopWatchWidget(tk.Frame):
    def __init__(self, clock=None, clockface=None, buttons=None, **kwargs):
        tk.Frame.__init__(self, **kwargs)
        if not isinstance(clock, StopWatch):
            clock = StopWatch()
            
        if not isinstance(clockface, ClockFace):
            clockface = ClockFace(clock, master=self)
            
        if not isinstance(buttons, ToggleSwitch):
            buttons = ToggleSwitch(clock, master=self)

        self.set_clock(clock)
        self.set_buttons(buttons)
        self.set_clockface(clockface)
        
        self.clockface.pack(side=tk.TOP, pady=5, padx=10)   ###
        self.buttons.pack(side=tk.TOP, pady=5, padx=10)     ###

    @property
    def clock(self):
        return self._clock

    @property
    def buttons(self):
        return self._buttons

    @property
    def clockface(self):
        return self._clockface

    def set_clock(self, clock):
        self._clock = clock
        
    def set_buttons(self, buttons):
        buttons.set_clock(self._clock)
        self._buttons = buttons

    def set_clockface(self, clockface):
        clockface.set_clock(self._clock)
        self._clockface = clockface
