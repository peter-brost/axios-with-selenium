Feature: Login to The Internet


Scenario: Authenticate using form authentication
    Given I am on the /login page
    When I enter "tomsmith" in the username field
    And I enter "SuperSecretPassword!" into the password field
    And I click on the login button
    Then I should see "secure" in the current page's url
    And I should see the logout button on the current page