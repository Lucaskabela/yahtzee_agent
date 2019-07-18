# Yahtzee AI Agent

A simple agent made to play the game [Yahtzee](https://en.wikipedia.org/wiki/Yahtzee)
Written primarily in python

Base off: https://pdfs.semanticscholar.org/8414/a69fe8e7f2eb72b0726f11c8140109f277d7.pdf

## About

Growing up I played a lot of Yahtzee with my family.  So, I decided that I was
tired of losing and wanted to make an A.I. that maximized the chance of me 
winning!

## Gameplan:

1. Need Turn State
	a. Dice rolls
	b. Continue or Stop
	c. Where to add score

2. Need Player State
	a. Score
	b. Turn Number

3. Need Agent
	a. Decision Making
		- likely rule based (optimal solution maybe discovered?)
		- neural net (pytorch?)
		- hidden markov model (next states?)