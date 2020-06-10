from abc import ABC, abstractmethod

class ControlState(ABC):
  def __init__(self, previous_state, outputter, input_payload):
    self.property_bag = {}

    if input_payload:
      self.property_bag.update(input_payload)
    self.outputter = outputter
    self.exit_payload = {}

  @abstractmethod
  def execute(self):
      pass

  def __repr__(self):
    if self.outputter:
      outputter.log("Previous State: {}".format(self.property_bag))
      outputter.log("Error State: {}".format(self.property_bag))
      outputter.log("Properties: {}".format(self.property_bag))
