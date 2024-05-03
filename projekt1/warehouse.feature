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
    Then shoud see warning message
    And product is not created

  Scenario: Add new product - filling required fields
    Given a web browser is at the "Add Product" page  
    And required fields are filled
    When admin clicks on "Save" button
    Then shoud see sucess message
    And product is created

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
    Given a web browser is at the "Product" page
    And filter table is filled whit right informations about created product
    And admin clicks on "Filter" button
    Then shoud see only added product

  Scenario: Edit added product - go to edit page 
    Given a web browser is at the "Products" page
    When admin clicks on "Edit" button for added product
    Then shoud see "Edit Product" page

  Scenario: Edit added product - make change whitout save
    Given a web browser is at the "Edit Product" page for added product
    And edits information
    When admin clicks on "Back" button
    Then shoud see "Products" page
    And product was not edited

  Scenario: Edit added product - make change whit save
    Given a web browser is at the "Edit Product" page for added product
    And edits information
    When admin clicks on "Save" button
    Then shoud see sucess message
    And product is edited

  Scenario: Add variant of added product
    Given a web browser is at the "Products" page
    When admin clicks on "dropdown" button for added product
    And admin clicks on "+ Add variant" button 
    Then shoud see "Add Product" page
    And warning message about creating variant

  Scenario: Copy added product
    Given a web browser is at the "Products" page
    And added product is selected
    When admin clicks on "Copy" button
    Then shoud see copy of added product whic is disabled

  Scenario: Wanting to delete added product
    Given a web browser is at the "Products" page
    And added product is selected
    When admin clicks on "Delete" button
    Then shoud see popup message "Are you sure?" whit buttons "Ok" and "Cancel"

  Scenario: Deleting added product
    Given a web browser is at the "Products" page with popup "Are you sure?" whit buttons "Ok" and "Cancel"
    And added product is selected
    When admin clicks on "Ok" button
    Then shoud see sucess message
    And shoud not see deleted product
    