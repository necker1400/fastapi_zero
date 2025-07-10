from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_should_return_ok_and_hello_world():
    """
    Test has 3 parts:
    - A: Arrange: Arrange the necessary components for the test.
    - S: Act: Execute the code being tested.
    - A: Assert: Verify the expected outcomes.
    """
    # A: Arrange
    client = TestClient(app)

    # S: Act
    response = client.get('/')

    # A: Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}
