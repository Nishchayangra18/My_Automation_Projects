#Featur is like a test suite
Feature: Verify if Boooks are added and deleted using Library API

  #Scenario is like a test case
  Scenario: Verify AddBook API Functionality
    Given the Book details which need to be added to Library
    When we execute the AddBook PostAPI method
    Then Book is successfully added