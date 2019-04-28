Feature: Demo for using external class

Scenario Outline: Deal initial cards
  Given a dealer
  When the round starts
  Then the dealer gives itself two cards
  And first card is <card>
  And second card is "A-Diamond"
  Then card number is "5"
  Then use context


  Examples: Hands
  | card|
  |A-claver|


