Feature: Register / look in history

  Scenario: registration -  find register button
    Given a web browser is at the home page 
    When clicks on "My Acount"
    Then shoud see popup whit buttons "Register" and "Login"

  Scenario: registration - go to register acout page
    Given a web browser is at the home page whit popup buttons "Register" and "Login"
    When user clicks at "Register" button
    Then shoud see "Register Acount" page
  
  Scenario: registration - not filling required fields
    Given a web browser is at the "Register Acount" page
    And required fields are not filled
    When user click on "Continue" button
    Then shoud see warning message
  
  Scenario: registration - filling required fields
    Given a web browser is at the "Register Acount" page
    And required fields are filled
    When user click on "Continue" button
    Then acount shoud by created 
  
  Scenario: go to history page
    Given user is logged in as new registred user
    And a web browser is on "Account" page
    When user click on "View your order history" button
    Then shoud see "Order History" page
    And orders shoud by empty
  
  Scenario: go back from history page
    Given a web browser is at the "Order History" page for new registred user
    When user click on "Continue" button
    Then shoud see "Account" page