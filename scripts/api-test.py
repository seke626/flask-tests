def test_get_user_api(client):
    response = client.get('/api/users/1')
    assert response.status_code == 200
    assert response.json['username'] == 'test_user'
    assert response.json['email'] == 'test@example.com'