Feature: Add/Remove Elements Page Test on a mobile device


Scenario: User adds and removes elements
    Given the user is on the Add/Remove Elements page
    When the user adds a random number of elements
    Then the page should display the correct number of delete buttons
    When the user removes all added elements
    Then the page should display zero delete buttons