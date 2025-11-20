from cloud_utils_lib import ping

def test_ping():
    assert ping() == "pong"
