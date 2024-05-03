Feature: add/serach/edit/delete product

  Background:
    Given a user is logged in as admin

  Scenario: Add new product - go to "Add Product" page
    Given a web browser is at the "Products" page
    When admin click on "Add New" button
    Then shoud see "Add Product" page
  
  Scenario: Add new product - not filling required fields
    Given a web browser is at the "Add Product" page  
    And required fields are not filled
    When admin clicks on "Save" button
    Then shoud see warning message for warehouse

  Scenario: Add new product - filling required fields
    Given a web browser is at the "Add Product" page  
    And required fields are filled for warehouse
    When admin clicks on "Save" button
    Then shoud see sucess message for warehouse

  Scenario: Add new product - go back
    Given a web browser is at the "Add Product" page
    When admin click on "Back" button
    Then shoud see "Products" page
  
  Scenario: Search for added product - filling wrong informations
    Given a web browser is at the "Products" page
    And filter table is filled whit wrong information about created product
    When admin clicks on "Filter" button
    Then shoud see no products

  Scenario: Search for added product - filling right informations
    Given a web browser is at the "Products" page
    And filter table is filled whit right informations about created product
    And admin clicks on "Filter" button
    Then shoud see only added product

  Scenario: Edit first product - go to edit page 
    Given a web browser is at the "Products" page
    When admin clicks on "Edit" button for first product
    Then shoud see "Edit Product" page

  Scenario: Edit first product - make change whit save
    Given a web browser is at the "Edit Product" page for first product
    And edits information for product
    When admin clicks on "Save" button
    Then shoud see alert sucess message

  Scenario: Add variant of first product - go to add variant page
    Given a web browser is at the "Products" page
    When admin clicks on "dropdown" button for first product
    And admin clicks on "+ Add variant" button 
    Then shoud see "Add Product" page
    And warning message about creating variant
  
  Scenario: Add variant of first product - add variant
    Given a web browser is at the "add variant" page
    When admin chnage data
    And admin clicks on "save" button 
    And sucess message about creating variant

  Scenario: Copy first product
    Given a web browser is at the "Products" page
    And first product is selected
    When admin clicks on "Copy" button
    Then shoud see copy of first product which is disabled

  Scenario: Wanting to delete first product
    Given a web browser is at the "Products" page
    And first product is selected
    When admin clicks on "Delete" button
    And see popup message "Are you sure?" whit buttons "Ok" and "Cancel"
    And admin clicks on "Ok" button
    Then shoud see sucess message
    