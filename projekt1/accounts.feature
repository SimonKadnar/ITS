Feature: add/serach/edit/delete customer

  Background:
    Given a user is logged in as admin

  Scenario: Add new customer - go to "Add Customer" page
    Given a web browser is at the "Customer" page
    When admin clicks on "Add New" button
    Then shoud see "Add Customer" page
  
  Scenario: Add new customer - not filling required fields
    Given a web browser is at the "Add Customer" page  
    And required fields are not filled
    When admin clicks on "Save" button
    Then shoud see warning message
    And customer is not created

  Scenario: Add new customer - filling required fields
    Given a web browser is at the "Add Customer" page  
    And required fields are filled
    When admin clicks on "Save" button
    Then shoud see sucess message
    And customer is created

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

  Scenario: Edit added customer - make change whitout save
    Given a web browser is at the "Edit Customer" page for added customer
    And edits information
    When admin clicks on "Back" button
    Then shoud see "Customer" page
    And Customer was not edited

  Scenario: Edit added customer - make change whit save
    Given a web browser is at the "Edit Customer" page for added customer
    And edits information
    When admin clicks on "Save" button
    Then shoud see sucess message
    And customer is edited

  Scenario: Edit added customer - look on orders
    Given a web browser is at the "Edit Customer" page on added customer
    When admin clicks on "Orders" button
    Then shoud see "Order List" page for added customer
    And added customer shoud have no orders

  Scenario: Use customer account
    Given a web browser is at the "Customer" page
    And admin clicks on "dropdown" button for added customer
    When admin clicks on "Your Store" button
    Then shoud be logged as added customer

  Scenario: Wanting to delete added customer
    Given a web browser is at the "Customer" page
    And added customer is selected
    When admin clicks on "Delete" button
    Then shoud see popup message "Are you sure?" whit buttons "Ok" and "Cancel"

  Scenario: Deleting added customer
    Given a web browser is at the "Customer" page with popup "Are you sure?" whit buttons "Ok" and "Cancel"
    And added customer is selected
    When admin clicks on "Ok" button
    Then shoud see sucess message
    And shoud not see deleted customer
