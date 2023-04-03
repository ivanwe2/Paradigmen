Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
хелп
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    хелп
NameError: name 'хелп' is not defined
help
Type help() for interactive help, or help(object) for help about object.
help()

Welcome to Python 3.11's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> print("helo");
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    help()
  File "<frozen _sitebuiltins>", line 103, in __call__
  File "C:\Users\rusev\AppData\Local\Programs\Python\Python311\Lib\pydoc.py", line 2007, in __call__
    self.interact()
  File "C:\Users\rusev\AppData\Local\Programs\Python\Python311\Lib\pydoc.py", line 2034, in interact
    self.help(request)
  File "C:\Users\rusev\AppData\Local\Programs\Python\Python311\Lib\pydoc.py", line 2060, in help
    elif request: doc(request, 'Help on %s:', output=self._output)
  File "C:\Users\rusev\AppData\Local\Programs\Python\Python311\Lib\pydoc.py", line 1784, in doc
    pager(render_doc(thing, title, forceload))
  File "C:\Users\rusev\AppData\Local\Programs\Python\Python311\Lib\pydoc.py", line 1758, in render_doc
    object, name = resolve(thing, forceload)
  File "C:\Users\rusev\AppData\Local\Programs\Python\Python311\Lib\pydoc.py", line 1744, in resolve
    raise ImportError('''\
ImportError: No Python documentation found for 'print("helo");'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.
print("asdasd")
asdasd
if(5>3):
print(1)
SyntaxError: expected an indented block after 'if' statement on line 1
"yes
SyntaxError: incomplete input
"ywrsdfshf"
'ywrsdfshf'
x=4
y="yes"
c=50
print(x,y,c)
4 yes 50
print(x)
4
print(x) print(type(x))
SyntaxError: invalid syntax
print(type(x))
<class 'int'>
>>> cls
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> z=x/y
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    z=x/y
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> z=x/c
>>> z
0.08
>>> int(z)
0
>>> float(x)
4.0
>>> d=x*y
>>> d
'yesyesyesyes'
>>> g=y/x
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    g=y/x
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> id(x)
140707899700104
>>> X=2
>>> id(x)
140707899700104
>>> type(x)
<class 'int'>
>>> id(X)
140707899700040
>>> x
4
>>> x=2
>>> id(x)
140707899700040
