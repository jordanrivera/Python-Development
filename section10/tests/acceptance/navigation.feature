Feature: Test navigation between pages

  Scenario: Homepage can go to Blog
    Given I am on t he homepage
    When I click on the with "Go to blog" link
    Then I am on the blog page

  Scenario: Blog can go to Homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage