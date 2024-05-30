
def test_health_endpoint_returns_200(flask_test_client):
    # when
    response = flask_test_client.get('/health')

    # then
    assert response.status_code == 200