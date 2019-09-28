# Lexical-Analysis

(1) Underscoring the Magnitude:  In this problem you will use regular expressions to specify tokens for a part of a new programming language. You must handle seven types of
tokens:

       PLUS            +
       MINUS           -
       TIMES           *
       DIVIDE          /
       IDENT           my_variable  Caps_Are_OK
       STRING          'yes'  "also this"  
       NUMBER          123  123_456_789

The last three merit a more detailed explanation. 

An IDENT token is a non-empty sequence of lower- and/or upper-case letters and underscores, but the first character cannot be an underscore. (Letters are a-z and A-Z only.) The value of an IDENT token is the string matched. A STRING token is zero or more of any character surrounded by 'single quotes' or "double quotes". In this language, there are no escape sequences, so "this\" is a string containing five characters. The value of a STRING token is the string matched with the quotes removed. A NUMBER is a a non-empty sequence of digits (0-9) and/or underscores, except that the first character cannot be an underscore. Many real-world languages actually support this, to make large number easier to read. All NUMBERs in this language are positive integers; negative signs and/or periods are not part of NUMBERs. The value of a NUMBER is the integer value of its digits with all of the underscores removed: the value of "12_34" is 1234 (the integer). For this problem we do *not* care about line number information. Only the types and values of tokens matter. Whitespace characters are ' \t\v\r' (and we have already filled them in for you below). 

(2) A Gruesome Problem:  In this problem you will use re.findall() to find all words matching a certain property. Taking liberties with Nelson Goodman's paradox, we say that a word is "blue" if it contains a lowercase "b" before a lowercase "t" and a word is "green" if it contains a lowercase "g" after a lowercase "t". For example:

       "wombat"        is blue (b before t)
       "fabricate"     is blue (b before t) 
       "habitat"       is blue (b before t)
       "waftage"       is green (g after t)
       "rackateering"  is green (g after t) 
       "abating"       is blue and gree (b ... t and t ... g) 

We say that a word is "grue" if it is EITHER "green" OR "blue" (or both). For this problem, words are non-empty sequences of the English letters a-z and/or A-Z. Write a procedure gruesome() that takes a string as an argument and returns a list of all "grue"some words (i.e., words that contain either a b before a t or that contain a g after a t) in that given string.
