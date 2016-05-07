# Debugging with PDB
__PDB__ is the Python command line DeBugger

## Some hints on usage

```bash
import pdb
pdb.set_trace()
help
help continue
```

## How to debug?

Execute `pdb` as a script and pass an argument to it:
```bash
python -m pdb palindrome.py
> j:\py\pyfunds\classes\palindrome.py(1)<module>()
-> import unittest
```
`import unittests` is the next command to be executed.

Find the current location in the code:
```bash
(Pdb) where
  c:\python34\lib\bdb.py(431)run()
-> exec(cmd, globals, locals)
  <string>(1)<module>()
> j:\py\pyfunds\classes\palindrome.py(1)<module>()
-> import unittest
```
We are at line 1.

Run the next command:
```bash
(Pdb) next
> j:\py\pyfunds\classes\palindrome.py(3)<module>()
-> def digits(x):
```
Continue execution and then break with Ctrl-C:
```bash
(Pdb) cont

Program interrupted. (Use 'cont' to resume).
> j:\py\pyfunds\classes\palindrome.py(18)digits()
-> digs.append(mod)
```
We can now check a piece of our source code:
```bash
(Pdb) list
 13         [4, 5, 8, 6, 3, 7, 8]
 14         """
 15         digs = []
 16         while x != 0:
 17             div, mod = divmod(x, 10)
 18  ->         digs.append(mod)
 19             x = mod
 20         return digs
 21
 22
 23     def is_palindrome(x):
```
We see that we are inside a loop. We can try to exit the function
by typing `return`, then break again:
```bash
(Pdb) return

Program interrupted. (Use 'cont' to resume).
> j:\py\pyfunds\classes\palindrome.py(16)digits()
-> while x != 0:
```
Exit `PDB` with `quit` command (a couple of times).
