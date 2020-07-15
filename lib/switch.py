import tkinter as tk


class ToggleButton(tk.Button):
    def __init__(self, state_cnf=({},), master=None, **kwargs):
        tk.Button.__init__(self, master=master)
        self.protected_keys = set()
        kwargs.update(dict(command=self.toggle_state))
        self.configure(**kwargs)
        self._state_pointer = 0
        self._states = []

        [self.add_state(**cnf) for cnf in state_cnf]

        self.set_state_configuration()

    @property
    def configurable_keys(self):
        return tuple(set(self.keys()).difference(self.protected_keys))

    @property
    def states(self):
        return tuple(self._states)

    @property
    def current_state(self):
        if self._states:
            return self._states[self._state_pointer]

    def toggle_state(self):
        self.current_state.invoke()
        self.cycle_state()
        return self

    def cycle_state(self, step=1):
        self._state_pointer += step
        if self._states:
            self._state_pointer %= len(self._states)
        else:
            self._state_pointer = 0
        self.set_state_configuration()
        return self

    def set_state_configuration(self):
        state = self.current_state
        if state:
            cnf = {
                k: state[k] for k in self.configurable_keys
                }
            tk.Button.configure(self, **cnf)
        self.update()
        return self

    def add_state(self, new_state=None, **kwargs):
        if not isinstance(new_state, tk.Misc):
            new_state = tk.Button()
        new_state.configure(**kwargs)
        self._states.append(new_state)
        self.set_state_configuration()
        return self        

    def configure(self, **kwargs):
        self.protected_keys.update(kwargs.keys())
        return tk.Button.configure(self, **kwargs)

    config = configure


class ToggleSwitch(tk.Frame):        
    def __init__(self, clock, **kwargs):
        tk.Frame.__init__(self, **kwargs)
        self._clock = clock
        self._toggle_button = ToggleButton(
            master=self,
            state_cnf=(
                dict(text="Start", command=self._clock.start),
                dict(text="Stop", command=self._clock.stop)
                )
            )
        
        reset_button = tk.Button(self, text="Reset")

        self.set_reset_button(reset_button)

        for i in (self._toggle_button, self._reset_button): ###
            i.pack(side=tk.LEFT, padx=10)                   ###

    @property
    def toggle_button(self):
        return self._toggle_button

    @property
    def start_button(self):
        return self._toggle_button.states[0]

    @property
    def stop_button(self):
        return self._toggle_button.states[1]

    @property
    def reset_button(self):
        return self._reset_button

    def set_reset_button(self, button):
        button.configure(command=self._clock.reset)
        self._reset_button = button
        return self

    def set_clock(self, clock):
        self._clock = clock
        self.set_reset_button(self._reset_button)
    
    
class StartStopSwitch(tk.Frame):
    def __init__(self, clock, **kwargs):
        tk.Frame.__init__(self, **kwargs)
        self._clock = clock
        
        start_button = tk.Button(self, text="Start")
        stop_button = tk.Button(self, text="Stop")
        reset_button = tk.Button(self, text="Reset")

        self.set_start_button(start_button)
        self.set_stop_button(stop_button)
        self.set_reset_button(reset_button)

        for i in (                          ###
            self._start_button,             ###
            self._stop_button,              ###
            self._reset_button              ###
            ):                              ###
            i.pack(side=tk.LEFT, padx=10)   ###
    
    @property
    def start_button(self):
        return self._start_button

    @property
    def stop_button(self):
        return self._stop_button

    @property
    def reset_button(self):
        return self._reset_button

    def set_clock(self, clock):
        self._clock = clock
        self.set_start_button(self._start_button)
        self.set_stop_button(self._stop_button)
        self.set_reset_button(self._reset_button)
        return self

    def set_start_button(self, button):
        button.configure(command=self._clock.start)
        self._start_button = button
        return self

    def set_stop_button(self, button):
        button.configure(command=self._clock.stop)
        self._stop_button = button
        return self

    def set_reset_button(self, button):
        button.configure(command=self._clock.reset)
        self._reset_button = button
        return self

