Feature: Checkboxes Page Test


Scenario: User checks and unchecks checkboxes
    Given the user is on the Checkboxes page
    When the user checks the first checkbox
    And the user unchecks the second checkbox
    Then the first checkbox should be checked
    And the second checkbox should be unchecked