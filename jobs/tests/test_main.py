from main import transform_source_table


def test_transform_source_table(test_session):
    """"""
    test_data = [
        {"AIQ_INDID": "A", "AIQ_HOME_AGE": 5, "HOMEVALUEIQ": 50},
        {"AIQ_INDID": "A", "AIQ_HOME_AGE": 10, "HOMEVALUEIQ": 100},
        {"AIQ_INDID": "B", "AIQ_HOME_AGE": 15, "HOMEVALUEIQ": 150},
        {"AIQ_INDID": "B", "AIQ_HOME_AGE": 15, "HOMEVALUEIQ": 150},
    ]

    test_df = test_session.create_dataframe(test_data)

    test_result = transform_source_table(source_table=test_df)

    assert "MEAN_HOME_VALUE_IQ" in test_result.columns
