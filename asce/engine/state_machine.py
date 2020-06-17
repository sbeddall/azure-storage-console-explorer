from .state_implementations import InteractionNodes

class StateMachine:
    def __init__(self, json_state_map, outputter, debug_mode=False):
        self.debug_mode = debug_mode
        self.state_map = self.parse_json_map(json_state_map)
        self.outputter = outputter

    def parse_json_map(self, json_state_map):
      return {}

    def run(self):
        if self.debug_mode:
            self.outputter.log("Running")

    def construct_node(self, node_type):
      targetClass = getattr(InteractionNodes, node_type)
      instance = targetClass()
      return instance