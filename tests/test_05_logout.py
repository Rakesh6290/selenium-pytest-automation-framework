import json
import pytest


with open("data/product_test_data.json") as file:

    test_data = json.load(file)


login_data = test_data["login_data"]["valid_user"]

logout_data = test_data["logout_data"]


@pytest.mark.smoke
def test_logout(
    login_page,
    product_page
):

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    product_page.logout()

    assert (
        product_page.driver.current_url
        == logout_data["expected_url"]
    )