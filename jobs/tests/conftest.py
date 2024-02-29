from snowflake.snowpark import Session
import pytest
import os
import sys

# Add modules to path for correct imports
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
LIBS_DIR = f"{ROOT_DIR}/libs"
MODELS_DIR = f"{ROOT_DIR}/models"
TABLES_DIR = f"{ROOT_DIR}/tables"
JOBS_DIR = os.path.dirname(ROOT_DIR)
[sys.path.append(d) for d in [ROOT_DIR, LIBS_DIR, MODELS_DIR, TABLES_DIR, JOBS_DIR]]


@pytest.fixture
def test_session():
    session = Session.builder.config("local_testing", True).create()
    yield session


@pytest.fixture
def jobs_dir():
    yield JOBS_DIR
