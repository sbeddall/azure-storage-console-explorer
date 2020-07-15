from .control_state import ControlState

# get all the common settings
from .env import INPUT_FIELD_NAME


class InteractionNodes:
    class OutputNode(ControlState):
        def __init__(self, *args):
            super().__init__(*args)

        def execute(self):
            self.outputter.print(self.input_payload)

    class InteractionNode(ControlState):
        def __init__(self, *args):
            super().__init__(*args)

        def execute(self, default_input=None):
            if not default_input:
                input_data = input("Give me some input: ")
            else:
                input_data = default_input

            self.exit_payload.update({INPUT_FIELD_NAME: input_data})
            return self.exit_payload
