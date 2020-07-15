# this is the single location in the engine namespace where we import directly
# from the "cmdui" namespace. We do this so that we can actually output given
# our entrance is  directly from console_scripts
from .state_machine import StateMachine

from asce.cmdui import RawOutput


def run():
    print("executing state machine")

    json_map = ""  # todo: populate with load from json graph
    outputter = RawOutput()

    main_machine = StateMachine(json_map, outputter, False)
    main_machine.run()
