"""
Test if the version route response, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument

from app import version

def test_version_route_response(client):
    """
    Test the version route to return current version
    """
    response = client.get("/version")
    assert response.status_code == 200
    assert b"Fhe current version of the app is: " + version.encode() in response.data
