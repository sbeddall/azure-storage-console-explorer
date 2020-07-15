from abc import ABC, abstractmethod


class ControlState(ABC):
    def __init__(self, previous_state, outputter, input_payload):
        print("in init for ControlState")
        self.property_bag = {}

        if input_payload:
            self.property_bag.update(input_payload)
        self.outputter = outputter
        self.exit_payload = {}

    @abstractmethod
    def execute(self):
        pass
