class StateMachine:
  def __init__(self, json_state_map, outputter, debug_mode=False):
    self.debug_mode = debug_mode
    self.state_map = self.parse_json_map(json_state_map)
    self.outputter = outputter

  def run(self):
    if self.debug_mode:
      outputter.log("Running")
