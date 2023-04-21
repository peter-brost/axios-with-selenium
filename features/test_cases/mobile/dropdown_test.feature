Feature: Dropdown Page Test on a mobile device


Scenario: User selects options from dropdown menu
    Given the user is on the Dropdown page
    When the user selects Option 1 from the dropdown menu
    Then Option 1 should be displayed as the selected option
    When the user selects Option 2 from the dropdown menu
    Then Option 2 should be displayed as the selected option