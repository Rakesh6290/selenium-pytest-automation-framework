import json
import pytest


with open("data/product_test_data.json") as file:

    test_data = json.load(file)


login_data = test_data["login_data"]["valid_user"]

product_test_data = test_data["valid_products"]

cart_data = test_data["cart_data"]


@pytest.mark.regression
def test_add_product_to_cart(login_page, product_page):

    product = product_test_data["backpack"]

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    product_page.add_product_to_cart(
        product["product_name"]
    )

    assert product_page.get_cart_count() == cart_data["cart_count"]


@pytest.mark.regression
def test_remove_product_from_cart(login_page, product_page):

    product = product_test_data["bike_light"]

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    product_page.add_product_to_cart(
        product["product_name"]
    )

    product_page.remove_product_from_cart(
        product["product_name"]
    )

    cart_badge = product_page.driver.find_elements(
        *product_page.CART_BADGE
    )

    assert len(cart_badge) == 0