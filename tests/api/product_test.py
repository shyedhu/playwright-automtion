import pytest
from utils.helper import readdatas,getresponsetext

@pytest.mark.parametrize("name, price, available_quantity", readdatas())
def test_product_attribute(name, price, available_quantity,api_url):
    products = getresponsetext(api_url)
    for product in products:
     if product["name"] == name:
      assert product["price"] == int(price)
      assert product["available_quantity"] == int(available_quantity)