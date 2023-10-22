Feature: Search Functioanlity

  @search
  Scenario: Search for a valid product
    Given I navigate to home page
    When I enter valid product say "HP" into the search box field
    And I click on Search Button
    Then Valid product should get displayed in search results

  @search
  Scenario: Search for an invalid product
    Given I navigate to home page
    When I enter invalid product say "HONDA" into the search box field
    And I click on Search Button
    Then Proper error message should be displayed in search results

  @search
  Scenario: Search without entering any product
    Given I navigate to home page
    When I dont enter anything into the search box field
    And I click on Search Button
    Then Proper error message should be displayed in search results