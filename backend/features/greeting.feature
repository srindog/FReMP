@greeting
Feature: Greeting
Upon entering the app, I want to be greeted

  @default
  Scenario Outline: Greet with the default greeting
    Given we arrive at the app
    When the default greeting is requested
    Then the default greeting says "Hello!"

  @mongo
  Scenario Outline: Greet with the mongo greeting
    Given we arrive at the app
    When the mongo greeting is requested
    Then the mongo greeting says "Hello from Mongo!"