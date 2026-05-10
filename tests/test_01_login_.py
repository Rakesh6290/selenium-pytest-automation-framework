import json
import pytest
import allure
from utils.config import INVENTORY_URL
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "login_test_data.json")

with open(DATA_PATH) as file:
    test_data = json.load(file)
# =========================
# ✅ Positive Test Case
# =========================

@allure.title("Verify valid login")

@allure.description(
    "Verify user can login using valid credentials"
)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_valid_login(login_page):
    user = test_data["valid_user"]

    with allure.step("Enter username"):
        login_page.enter_username(user["username"])

    with allure.step("Enter password"):
        login_page.enter_password(user["password"])

    with allure.step("Click login button"):
        login_page.click_login()

    with allure.step("Verify login success"):
        assert "inventory" in login_page.driver.current_url


# =========================
# ❌ Negative Test Cases
# =========================

@pytest.mark.regression
@pytest.mark.login
def test_invalid_username(login_page):

    user = test_data["invalid_username_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_invalid_password(login_page):

    user = test_data["invalid_password_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()



@pytest.mark.regression
@pytest.mark.login
def test_both_invalid(login_page):

    user = test_data["both_invalid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_empty_username(login_page):

    user = test_data["empty_username_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["username_required"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_empty_password(login_page):

    user = test_data["empty_password_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["password_required"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_both_empty(login_page):

    user = test_data["empty_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["username_required"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_locked_user(login_page):

    user = test_data["locked_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["locked_user_error"]

    assert expected_error in login_page.get_error_message().lower()


# =========================
# ⚠️ Edge Test Cases
# =========================
@pytest.mark.regression
@pytest.mark.login
def test_username_with_spaces(login_page):

    user = test_data["space_username_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_password_with_spaces(login_page):

    user = test_data["space_password_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_case_sensitive_username(login_page):

    user = test_data["uppercase_username_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_case_sensitive_password(login_page):

    user = test_data["uppercase_password_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_very_long_username(login_page):

    user = test_data["long_username_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


@pytest.mark.regression
@pytest.mark.login
def test_very_long_password(login_page):

    user = test_data["long_password_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    expected_error = test_data["messages"]["invalid_credentials"]

    assert expected_error in login_page.get_error_message()


# =========================
# 🔒 Security / Navigation
# =========================
@pytest.mark.regression
@pytest.mark.login
def test_direct_url_access_without_login(login_page):

    login_page.driver.get(INVENTORY_URL)

    expected_url = test_data["messages"]["security_redirect_url"]

    assert expected_url in login_page.driver.current_url