Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hello world!")
hello world!
>>> first_name = "Michael"
>>> print(first_name)
Michael
>>> fact = "I miss home. Kinda."
>>> print("My name is " + first_name + " and " + fact)
My name is Michael and I miss home. Kinda.
>>> message = first_name + fact
>>> print(message)
MichaelI miss home. Kinda.
>>> num1 = 1
>>> num2 = 2
>>> answer = num1+num2-num1*num1
>>> print(answer)
2
>>> word1 = "cat"
>>> word2 = "barks"
>>> word3 = "tree"
>>> word4 = "Nacho Libre"
>>> word5 = "lazily"
>>> word6 = "'Darn it!'"
>>> print(word4 + word2 + " and the " + word1 + word5 + " climbs the " + word3 ". " + word6)
SyntaxError: invalid syntax
>>> print(word4 + word2 + " and the " + word1 + word5 + " climbs the " + word3 "." + word6)
SyntaxError: invalid syntax
>>> print(word4 + word2 + " and the " + word1 + word5 + " climbs the " + word3 + ". " + word6)
Nacho Librebarks and the catlazily climbs the tree. 'Darn it!'
>>> print(word4 + word2 + " and the " + word1 + word5 + " climbs the " + word3 ". " + word6)
SyntaxError: invalid syntax
>>> print(word4 + word2 + " and the " + word1 + word5 + " climbs the " + word3 + ". " + word6)
Nacho Librebarks and the catlazily climbs the tree. 'Darn it!'
>>> input()
