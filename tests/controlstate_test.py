import pytest


def test_import():
  from asce.engine import ControlState

  cs = ControlState()

  assert(cs is not None)