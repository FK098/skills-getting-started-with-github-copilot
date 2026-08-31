from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Return a test client for the FastAPI app."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def reset_activities():
    """Reset the in-memory activity state before and after each test."""
    original = deepcopy(activities)
    activities.clear()
    activities.update(deepcopy(original))
    yield
    activities.clear()
    activities.update(deepcopy(original))
