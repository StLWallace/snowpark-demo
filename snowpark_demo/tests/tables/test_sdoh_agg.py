from snowpark_demo.tables.sdoh_agg import SdohAgg


class TestSdohAgg:
    def test_create(self, test_session):
        """"""
        test_data = [
            {"AIQ_INDID": "A", "AIQ_HOME_AGE": 5, "HOMEVALUEIQ": 50},
            {"AIQ_INDID": "A", "AIQ_HOME_AGE": 10, "HOMEVALUEIQ": 100},
            {"AIQ_INDID": "B", "AIQ_HOME_AGE": 15, "HOMEVALUEIQ": 150},
            {"AIQ_INDID": "B", "AIQ_HOME_AGE": 15, "HOMEVALUEIQ": 150},
        ]

        test_sdoh_sample = test_session.create_dataframe(test_data)

        test_sdoh_agg = SdohAgg(session=test_session, sdoh_sample=test_sdoh_sample)

        assert "MEAN_HOME_VALUE_IQ" in test_sdoh_agg.columns
