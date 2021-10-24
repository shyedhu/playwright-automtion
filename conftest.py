import pytest

@pytest.fixture
def api_url():
   input = "https://nodes-api-demo.vercel.app/api/products"
   return input