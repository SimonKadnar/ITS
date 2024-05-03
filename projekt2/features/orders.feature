Feature: add order

  Background:
    Given a user is logged in as admin

  Scenario: Add new order - go to "Add order" page
    Given a web browser is at the "Orders" page
    When admin click on "Add New" button
    Then shoud see "Add order" page
  
  Scenario: Add new order - not filling required fields
    Given a web browser is at the "Add order" page  
    And required fields are not filled
    When admin clicks on "Confirm" button
    Then shoud see warning message
