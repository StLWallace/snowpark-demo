from libs.utils import get_connection_params


def test_get_connection_params():
    """"""
    test_conf_path = "../conf/snowflake_conn.yml"
    test_result = get_connection_params(test_conf_path)

    assert test_result.warehouse == "TEST_WH"
