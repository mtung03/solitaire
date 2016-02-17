## Klondike Deal 3 in Python 3.4 ##

Input format:

n == deal three new cards onto the waste pile from the deck

[char index of starting pile][number of cards moving][char index of ending pile]

Goal:
 To fill all four foundation piles fully from ace to king of the same suit

 Cards on the tableau must be descending by rank and alternating color
 (clubs and spades are black, diamonds and hearts red)

12/18/15 - deals, moves cards, tells when won





To-Do:
 - make rules for what cards can go where
	- descending			-- done 2/13
	- alternating color		-- done 2/13
	- only kings on open spaces -- done 2/13
	- only up on foundation piles -- done 2/15
 - waste pile displays top 3 instead of the number in that set -- done 2/16
 - allow for more than 10 stacks of cards to be moved -- done
 - subtle semi-repeatable bug when attempting to put an ace in en empty foundation pile
 - code still contains debugging print statements
 - better organization possible -- especially in check_move function