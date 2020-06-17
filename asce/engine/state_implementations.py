import importlib
from .control_state import ControlState

# get all the common settings
from .env import *

class InteractionNode(ControlState):
    def execute(self, default_input=None):
        if not default_input:
            input_data = input("Give me some input: ")
        else:
            input_data = default_input

        self.exit_payload.update({INPUT_FIELD_NAME: input_data})
        return OutputNode(self, self.outputter, self.exit_payload)


class OutputNode(ControlState):
    def execute(self):
        self.outputter.print(self.input_payload)
