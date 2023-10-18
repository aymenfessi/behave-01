Feature: Basic Calculator Operations
  Scenario: Add two numbers
    Given a calculator
    When I add 2 and 3
    Then the result should be 5