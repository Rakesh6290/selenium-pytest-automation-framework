import json
import pytest
import allure

with open("data/product_test_data.json") as file:

    test_data = json.load(file)


login_data = test_data["login_data"]["valid_user"]

checkout_test_data = test_data["checkout_data"]


@allure.title("Verify Successful Checkout")

@allure.description(
    "Verify user can complete checkout successfully"
)

@pytest.mark.regression
def test_valid_checkout(
    login_page,
    product_page,
    cart_page,
    checkout_page
):

    user = checkout_test_data["valid_checkout"]

    with allure.step(
        "Login with valid credentials"
    ):
        
        login_page.login(
            login_data["username"],
            login_data["password"]
    )


    with allure.step(
        "Add product to cart"
    ):

        product_page.add_product_to_cart(
            user["product_name"]
    )


    with allure.step(
        "Open cart page"
    ):
        product_page.open_cart()


    with allure.step(
        "Open checkout page"
    ):

        cart_page.click_checkout()


    with allure.step(
        "Enter checkout details"
    ):
        checkout_page.enter_checkout_details(
            user["first_name"],
            user["last_name"],
            user["zip_code"]
    )
        
    with allure.step(
        "Click continue button"
    ):

        checkout_page.click_continue()

    with allure.step(
        "Finish the order"
    ):

        checkout_page.click_finish()
    
    
    with allure.step(
        "Verify successful checkout message"
    ):

        assert (
            user["success_message"]
            in checkout_page.get_success_message()
    )


@pytest.mark.negative
def test_empty_firstname(
    login_page,
    product_page,
    cart_page,
    checkout_page
):

    user = checkout_test_data["empty_firstname"]

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    product_page.add_product_to_cart(
        user["product_name"]
    )

    product_page.open_cart()

    cart_page.click_checkout()

    checkout_page.enter_checkout_details(
        user["first_name"],
        user["last_name"],
        user["zip_code"]
    )

    checkout_page.click_continue()

    assert (
        user["error_message"]
        in checkout_page.get_error_message()
    )