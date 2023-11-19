"""
Test if the version route response, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_route_response(client):
    """
    Test if the version route response
    """
    response = client.get("/version")
    assert response.status_code == 200
