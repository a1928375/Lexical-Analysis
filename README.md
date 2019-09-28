# Lexical-Analysis

In this problem you will use regular expressions to specify tokens for a part of a new programming language. You must handle seven types of
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
