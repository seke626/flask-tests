def test_login_form(client):
    response = client.post(url_for('login'), data={'username': 'test_user', 'password': 'password123'})
    assert response.status_code == 200
    assert b"Login successful" in response.data