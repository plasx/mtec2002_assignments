Daniels-MacBook:Desktop plasx$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 1
False
>>> "test" = "test"
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> "test" ==  "test"
True
>>> 1 ==2 or 2 != 1
True
>>> True and 1 == 1
True
>>> False and - != =
  File "<stdin>", line 1
    False and - != =
                 ^
SyntaxError: invalid syntax
>>> False and - != 0
  File "<stdin>", line 1
    False and - != 0
                 ^
SyntaxError: invalid syntax
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test != "testing"
  File "<stdin>", line 1
    "test != "testing"
                    ^
SyntaxError: invalid syntax
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not( 10 == 1 or 1000 == 1000)
False
>>> not (1 != 10 or 3 == 4)
False
>>> not ("testing" == ("testing" == 1 or 1 == 0)
... 
... 
... false
  File "<stdin>", line 4
    false
        ^
SyntaxError: invalid syntax
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and not ("testing" == 1 or 1 == 0)
True
>>> 1 == 1 and not ("testing" == 1 or 1 == 0)
True
>>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
False
>>> 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
False
>>> Type "help", "copyright", "credits" or "license" for more information.
  File "<stdin>", line 1
    Type "help", "copyright", "credits" or "license" for more information.
              ^
SyntaxError: invalid syntax
>>> >>> True and True
  File "<stdin>", line 1
    >>> True and True
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> False and True
  File "<stdin>", line 1
    >>> False and True
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> 1 == 1 and 2 == 1
  File "<stdin>", line 1
    >>> 1 == 1 and 2 == 1
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> "test" = "test"
  File "<stdin>", line 1
    >>> "test" = "test"
     ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
  File "<stdin>", line 1
    File "<stdin>", line 1
    ^
IndentationError: unexpected indent
>>> SyntaxError: can't assign to literal
  File "<stdin>", line 1
    SyntaxError: can't assign to literal
               ^
SyntaxError: invalid syntax
>>> >>> "test" ==  "test"
  File "<stdin>", line 1
    >>> "test" ==  "test"
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> 1 ==2 or 2 != 1
  File "<stdin>", line 1
    >>> 1 ==2 or 2 != 1
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> True and 1 == 1
  File "<stdin>", line 1
    >>> True and 1 == 1
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> False and - != =
  File "<stdin>", line 1
    >>> False and - != =
     ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
  File "<stdin>", line 1
    File "<stdin>", line 1
    ^
IndentationError: unexpected indent
>>>     False and - != =
  File "<stdin>", line 1
    False and - != =
    ^
IndentationError: unexpected indent
>>>                  ^
  File "<stdin>", line 1
    ^
    ^
IndentationError: unexpected indent
>>> SyntaxError: invalid syntax
  File "<stdin>", line 1
    SyntaxError: invalid syntax
               ^
SyntaxError: invalid syntax
>>> >>> False and - != 0
  File "<stdin>", line 1
    >>> False and - != 0
     ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
  File "<stdin>", line 1
    File "<stdin>", line 1
    ^
IndentationError: unexpected indent
>>>     False and - != 0
  File "<stdin>", line 1
    False and - != 0
    ^
IndentationError: unexpected indent
>>>                  ^
  File "<stdin>", line 1
    ^
    ^
IndentationError: unexpected indent
>>> SyntaxError: invalid syntax
  File "<stdin>", line 1
    SyntaxError: invalid syntax
               ^
SyntaxError: invalid syntax
>>> >>> False and 0 != 0
  File "<stdin>", line 1
    >>> False and 0 != 0
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> True or 1 == 1
  File "<stdin>", line 1
    >>> True or 1 == 1
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> "test" == "testing"
  File "<stdin>", line 1
    >>> "test" == "testing"
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> 1 != 0 and 2 == 1
  File "<stdin>", line 1
    >>> 1 != 0 and 2 == 1
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> "test != "testing"
  File "<stdin>", line 1
    >>> "test != "testing"
     ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
  File "<stdin>", line 1
    File "<stdin>", line 1
    ^
IndentationError: unexpected indent
>>>     "test != "testing"
  File "<stdin>", line 1
    "test != "testing"
    ^
IndentationError: unexpected indent
>>>                     ^
  File "<stdin>", line 1
    ^
    ^
IndentationError: unexpected indent
>>> SyntaxError: invalid syntax
  File "<stdin>", line 1
    SyntaxError: invalid syntax
               ^
SyntaxError: invalid syntax
>>> >>> "test" != "testing"
  File "<stdin>", line 1
    >>> "test" != "testing"
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> "test" == 1
  File "<stdin>", line 1
    >>> "test" == 1
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> not (True and False)
  File "<stdin>", line 1
    >>> not (True and False)
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> not (1 == 1 and 0 != 1)
  File "<stdin>", line 1
    >>> not (1 == 1 and 0 != 1)
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> not( 10 == 1 or 1000 == 1000)
  File "<stdin>", line 1
    >>> not( 10 == 1 or 1000 == 1000)
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> not (1 != 10 or 3 == 4)
  File "<stdin>", line 1
    >>> not (1 != 10 or 3 == 4)
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> not ("testing" == ("testing" == 1 or 1 == 0)
  File "<stdin>", line 1
    >>> not ("testing" == ("testing" == 1 or 1 == 0)
     ^
SyntaxError: invalid syntax
>>> ... 
  File "<stdin>", line 1
    ... 
    ^
SyntaxError: invalid syntax
>>> ... 
  File "<stdin>", line 1
    ... 
    ^
SyntaxError: invalid syntax
>>> ... false
  File "<stdin>", line 1
    ... false
    ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 4
  File "<stdin>", line 1
    File "<stdin>", line 4
    ^
IndentationError: unexpected indent
>>>     false
  File "<stdin>", line 1
    false
    ^
IndentationError: unexpected indent
>>>         ^
  File "<stdin>", line 1
    ^
    ^
IndentationError: unexpected indent
>>> SyntaxError: invalid syntax
  File "<stdin>", line 1
    SyntaxError: invalid syntax
               ^
SyntaxError: invalid syntax
>>> >>> not ("testing" == "testing" and "Zed" == "Cool Guy")
  File "<stdin>", line 1
    >>> not ("testing" == "testing" and "Zed" == "Cool Guy")
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> 1 == 1 and not ("testing" == 1 or 1 == 0)
  File "<stdin>", line 1
    >>> 1 == 1 and not ("testing" == 1 or 1 == 0)
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> 1 == 1 and not ("testing" == 1 or 1 == 0)
  File "<stdin>", line 1
    >>> 1 == 1 and not ("testing" == 1 or 1 == 0)
     ^
SyntaxError: invalid syntax
>>> True
True
>>> >>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
  File "<stdin>", line 1
    >>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
     ^
SyntaxError: invalid syntax
>>> False
False
>>> >>> 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
  File "<stdin>", line 1
    >>> 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
     ^
SyntaxError: invalid syntax
>>> False
False
>>> 
