def test_home_template(client):
    response = client.get(url_for('home'))
    assert b"Welcome to My Flask App" in response.data