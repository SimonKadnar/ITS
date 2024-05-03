Feature: add/serach/edit/delete customer

  Background:
    Given a user is logged in as admin
    And a web browser is at the "Customer" page

  Scenario: Add new customer - go to "Add Customer" page
    When admin clicks on "Add New" button
    Then shoud see "Add Customer" page
  
  Scenario: Add new customer - not filling required fields
    Given a web browser is at the "Add Customer" page  
    And required fields are not filled
    When admin clicks on "Save" button
    Then shoud see warning message for accounts

  Scenario: Add new customer - filling required fields
    Given a web browser is at the "Add Customer" page  
    And required fields are filled for new account
    When admin clicks on "Save" button
    Then shoud see sucess message for accounts

  Scenario: Add new customer - go back
    Given a web browser is at the "Add Customer" page
    When admin clicks on "Back" button
    Then shoud see "Customer" page
  
  Scenario: Search for added customer - filling wrong informations
    Given a web browser is at the "Customer" page
    And filter table is filled whit wrong information about created user
    When admin clicks on "Filter" button
    Then shoud see no users

  Scenario: Search for added customer - filling right informations
    Given a web browser is at the "Customer" page
    And filter table is filled whit right informations about created user
    And admin clicks on "Filter" button
    Then shoud see only added customer
  
  Scenario: Edit added customer - go to edit page 
    Given a web browser is at the "Customer" page
    When admin clicks on "Edit" button for added customer
    Then shoud see "Edit Customer" page

  Scenario: Edit added customer - make change whit save
    Given a web browser is at the "Edit Customer" page for added customer
    And edits information for account
    When admin clicks on "Save" button
    Then shoud see sucess message for accounts

  Scenario: Edit added customer - look on orders
    Given a web browser is at the "Edit Customer" page on added customer
    When admin clicks on "Orders" button
    Then shoud see "Order List" page for added customer

  Scenario: Wanting to delete added customer
    Given a web browser is at the "Customer" page
    And added customer is selected
    When admin clicks on "Delete" button
    And shoud see popup message "Are you sure?" whit buttons "Ok" and "Cancel"
    And admin clicks on "Ok" button
    Then shoud zero useres accounts
