# flake8: noqa

from asce.engine import * #noqa: F403

def test_basic_interact():
    orig = InteractionNodes.InteractionNode(None, None, None)

    exit_payload = orig.execute(
        "test input data that should appear in property_bag of next state"
    )

    assert exit_payload != None
    assert INPUT_FIELD_NAME in exit_payload
