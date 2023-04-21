Feature: Key Presses Page Test on a desktop device


Scenario: User enters a random character
    Given the user is on the Key Presses page
    When the user enters a random character
    Then the page should display the message "You entered: [character]"