Feature: add/serach/edit/delete order

  Background:
    Given a user is logged in as admin
    And Test customer was created
    And Test product was created

  Scenario: Add new order - go to "Add order" page
    Given a web browser is at the "Orders" page
    When admin click on "Add New" button
    Then shoud see "Add order" page
  
  Scenario: Add new order - not filling required fields
    Given a web browser is at the "Add order" page  
    And required fields are not filled
    When admin clicks on "Confirm" button
    Then shoud see warnings messages
    And order is not created

  Scenario: Add new order - filling required fields
    Given a web browser is at the "Add order" page  
    And required fields are filled
    When admin clicks on "Confirm" button
    Then shoud see sucess message
    And order is created

  Scenario: Add new order - go back
    Given a web browser is at the "Add order" page
    When admin click on "Back" button
    Then shoud see "Orders" page
  
  Scenario: Search for added order - filling wrong informations
    Given a web browser is at the "Orders" page
    And filter table is filled whit wrong information about created order
    When admin clicks on "Filter" button
    Then shoud see no Orders

  Scenario: Search for added order - filling right informations
    Given a web browser is at the "order" page
    And filter table is filled whit right informations about created order
    And admin clicks on "Filter" button
    Then shoud see only added order

  Scenario: Wanting to see order
    Given a web browser is at the "Orders" page
    When admin clicks on "View" button for added order
    Then shoud see detials about order
  
  Scenario: Invoice order
    Given a web browser is at the page for specific order
    When admin clicks on "Print Invoice" button for added order
    Then shoud see "Invoice" page
  
  Scenario: Dispatch order
    Given a web browser is at the page for specific order
    When admin clicks on "Print Invoice" button for added order
    Then shoud see "Dispatch" page

  Scenario: Wanting to delete added order
    Given a web browser is at the "Orders" page
    And added order is selected
    When admin clicks on "Delete" button
    Then shoud see popup message "Are you sure?" whit buttons "Ok" and "Cancel"

  Scenario: Deleting added order
    Given a web browser is at the "Orders" page with popup "Are you sure?" whit buttons "Ok" and "Cancel"
    And added order is selected
    When admin clicks on "Ok" button
    Then shoud see sucess message
    And shoud not see deleted order
