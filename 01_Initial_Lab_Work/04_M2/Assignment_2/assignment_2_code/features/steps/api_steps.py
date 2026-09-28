import requests
import time
from behave import given, then


@given('I send a GET request for user "{user_id}"')
def send_get_request(context, user_id):

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    context.response = requests.get(url)

    time.sleep(2)


@then("the API response status should be 200")
def verify_status_code(context):

    assert context.response.status_code == 200

    time.sleep(1)


@then('the user name should be "{expected_name}"')
def verify_user_name(context, expected_name):

    data = context.response.json()

    actual_name = data["name"]

    assert actual_name == expected_name

    print(f"Expected: {expected_name}")
    print(f"Actual: {actual_name}")

    time.sleep(5)