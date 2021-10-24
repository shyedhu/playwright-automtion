import pytest
from utils.helper import getresponse

@pytest.mark.regression
def test_response_status_code(api_url):
     response = getresponse(api_url)
     print("response status_code ", response.status_code)
     assert response.status_code == 200

@pytest.mark.regression
def test_response_headers_content(api_url):
     response = getresponse(api_url)
     print("response headers ",  response.headers["Content-Type"])
     assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    
@pytest.mark.skip
def test_response_headers_cache(api_url):
     response = getresponse(api_url)
     print("response Cache-Control ",  response.headers["Cache-Control"])
     assert response.headers["Cache-Control"] == "public, max-age=0, must-revalidate"