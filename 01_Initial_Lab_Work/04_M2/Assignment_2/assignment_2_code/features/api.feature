Feature: Data driven API testing

  Scenario Outline: Verify user details using test data
    Given I send a GET request for user "<user_id>"
    Then the API response status should be 200
    And the user name should be "<expected_name>"

    Examples:
      | user_id | expected_name   |
      | 1       | Leanne Graham   |
      | 2       | Ervin Howell    |
      | 3       | Clementine Bauch |