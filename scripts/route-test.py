from flask import url_for

def test_home_route(client):
    response = client.get(url_for('home'))
    assert response.status_code == 200