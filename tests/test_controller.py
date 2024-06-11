
def test_health_endpoint_returns_200(flask_test_client):
    """
    Test to ensure that the health endpoint returns a status code of 200
    """
    # when:  Making a GET request to the /health endpoint 
    response = flask_test_client.get('/health')

    # then: Assert that the response status code is 200 (OK)
    assert response.status_code == 200
