from snowflake.snowpark import Session
import pytest


@pytest.fixture
def test_session():
    session = Session.builder.config("local_testing", True).create()
    yield session
