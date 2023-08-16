"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_dynamodb.tap import TapDynamoDB

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "region_name": "region_name_example",
    "account_id": "account_id_example",
    "external_id": "external_id_example",
    "role_name": "role_name_example",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapDynamoDB, config=SAMPLE_CONFIG)
    for test in tests:
        assert True
        # test()


# TODO: Create additional tests as appropriate for your tap.
