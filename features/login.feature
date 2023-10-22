Feature:

  @login @only
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I enter valid eamil address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |email                          |password    |
      |amotoorisampleone@gmail.com    |secondone   |
      |demoauto@gmail.com             |soumya123   |
      |soumya8917@gmail.com           |soumya123   |


  @login
  Scenario: Login with invalid eamil address and valid password
    Given I navigated to login page
    When I enter invalid eamil address and valid password say "soumya123" into the fields
    And I click on Login button
    Then I should get propper warning message

  @login
  Scenario:  Login with valid eamil address and invalid password
    Given I navigated to login page
    When I enter valid eamil address and invalid password say "soumyaranjan" into the fields
    And I click on Login button
    Then I should get propper warning message

  @login
  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I enter invalid eamil address and invalid password say "soumyaranjan" into the fields
    And I click on Login button
    Then I should get propper warning message

  @login
  Scenario:  Login without entering any credentials
    Given I navigated to login page
    When I  dont enter anything into  the fields
    And I click on Login button
    Then I should get propper warning message