Feature: Serach and buy product

  Scenario: search product
    Given a web browser is at the home page 
    And the user enters name of testing product into the search bar
    When user clicks on "Search" button
    Then shoud see test product on "Search" page

  Scenario: add product to basket
    Given a web browser is at the "Search" page whit test product  
    When user clicks on "Add Cart" button
    Then shoud see sucess message for added product
  
  Scenario: product is in basket - view cart
    Given a web browser is at the home page
    And in basket is test product
    When user clicks on "View Cart" button
    Then shoud see "Shopping Cart" page whit added product

  Scenario: product is in basket - remove product
    Given a web browser is at the "Shopping Cart" page
    And in basket is test product
    When user clicks on "Remove" button
    Then shopping cart shoud by empty

  Scenario: product is in basket - checkout
    Given a web browser is at the home page
    And in basket is test product
    When user clicks on "Checkout" button
    Then shoud see "Checkout" page whit added product

  Scenario: buy product - not filling required fields
    Given a web browser is at the "Checkout" page
    And in basket is test product
    And required fields are not filled
    When user click on "button-register" button
    Then shoud see warning message for order

  Scenario: buy product - filling required fields
    Given a web browser is at the "Checkout" page
    And in basket is test product
    And required fields are filled for order
    When user click on "Confirm Order" button
    Then shoud see "Success" page
