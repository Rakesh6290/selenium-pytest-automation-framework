import json
import pytest


with open("data/product_test_data.json") as file:

    test_data = json.load(file)


login_data = test_data["login_data"]["valid_user"]

sorting_data = test_data["sorting_data"]


@pytest.mark.regression
def test_sort_name_a_to_z(
    login_page,
    product_page
):

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    product_page.sort_products(
        sorting_data["name_a_to_z"]
    )


@pytest.mark.regression
def test_sort_price_low_to_high(
    login_page,
    product_page
):

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    product_page.sort_products(
        sorting_data["price_low_to_high"]
    )