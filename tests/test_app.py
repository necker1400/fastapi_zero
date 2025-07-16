from http import HTTPStatus


def test_root_should_return_ok_and_hello_world(client):
    """
    Test has 3 parts:
    - A: Arrange: Arrange the necessary components for the test.
    - S: Act: Execute the code being tested.
    - A: Assert: Verify the expected outcomes.
    """
    # S: Act
    response = client.get('/')

    # A: Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client):
    response = client.post(  # UserSchema
        '/users',
        json={
            'username': 'palmer',
            'email': 'palmer@example.com',
            'password': 'password123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    # UserPublic
    assert response.json() == {
        'username': 'palmer',
        'email': 'palmer@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'palmer',
                'email': 'palmer@example.com',
                'id': 1,
            }
        ]
    }


def test_get_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'palmer',
        'email': 'palmer@example.com',
        'id': 1,
    }


def test_get_user_should_return_not_found(client):
    response = client.get('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'palmer_updated',
            'email': 'palmer_updated@example.com',
            'password': 'newpassword123',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'palmer_updated',
        'email': 'palmer_updated@example.com',
        'id': 1,
    }


def test_update_user_should_return_not_found(client):
    response = client.put(
        '/users/999',
        json={
            'username': 'havertz',
            'email': 'havertz@example.com',
            'password': 'havertz123',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_should_return_not_found(client):
    response = client.delete('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
