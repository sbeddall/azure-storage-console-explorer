import pytest
from asce.engine import *

def test_cant_instantiate():
  try:
    cs = ControlState()
  except TypeError as f:
    # if we got here we are happy
    assert(True==True)
  except Exception as e:
    assert(False)

def test_basic_interact():
  orig = InteractionNode(None, None, None)
  next_state = orig.execute("test input data that should appear in property_bag of next state")

  assert(next_state != None)
  assert(INPUT_FIELD_NAME in next_state.property_bag)