"""Implementation of the state pattern"""
import itertools


class VolumeState:

    state = {
        'Increase': IncreaseVolume,
    }

    def change_volume(self):
        pass


class IncreaseVolume(VolumeState):

    def increase_volume(self):
        pass


class DecreaseVolume(VolumeState):

    def decrease_volume(self):
        pass


class State:
    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        print("Scanning... Station is", self.stations.__next__(), self.name)


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = itertools.cycle(["1250", "1380", "1510"])
        self.name = "AM"

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = itertools.cycle(["81.3", "89.1", "103.9"])
        self.name = "FM"

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio:
    """A radio.
    It has a scan button, and an AM/FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""

        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate
        self._volume_state = State()

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def increase_volume(self):
        self._volume_state.change_volume("Increase")

    def decrease_volume(self):
        self._volume_state.change_volume("Decrease")


def main():
    ''' Test our radio out '''
    radio = Radio()
    actions = ([radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2) * 2
    for action in actions:
        action()


if __name__ == '__main__':
    main()
"""
Scanning... Station is 1250 AM
Scanning... Station is 1380 AM
Switching to FM
Scanning... Station is 81.3 FM
Scanning... Station is 89.1 FM
Scanning... Station is 103.9 FM
Scanning... Station is 81.3 FM
Switching to AM
Scanning... Station is 1510 AM
Scanning... Station is 1250 AM
"""
