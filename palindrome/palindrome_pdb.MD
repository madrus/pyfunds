# Debugging, Distribution and Installation

## PDB - the Python command line DeBugger

### Some hints on usage

```bash
import pdb
pdb.set_trace()
help
help continue
```

### How to debug?

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

Now we can add PDB inside our Python module at the beginning
of the loop:
```python
import pdb
pdb.set_trace()
```
and run the program without specifying PDB at the command prompt:
```bash
python classes/palindrome.py
> j:\py\pyfunds\classes\palindrome.py(19)digits()
-> digs = []
```
Checking with `where` command confirms the desired location.

We can use `next` command or `Enter` key to step through the code.

Using `print` command, we can inspect variables:
```bash
(Pdb) print(x)
1234
(Pdb) print(digs)
[]
```
So, in this way, combining stepping through the program and
inspecting the variables, we can find the bug.

## nose debugger

`nose` is another debugger with possibility to do test discovery.
In that case, we don't need to write a special `main` module.

We can install it with e.g. PIP:
> `(env) pip install nose`

We can now use `nosetests` command to run our test:
```bash
(venv) J:\py\pyfunds\palindrome (master){hg}
λ nosetests palindrome.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s
OK
```


## Distributing programs

Move or copy all the project files to the `palindrome` folder.

Create the installer file: `setup.py`.

Create a new virtual invironment and activate it:
```bash
J:\py\pyfunds\palindrome (master){hg}
λ virtualenv venv
New python executable in J:\py\pyfunds\palindrome\venv\Scripts\python.exe
Installing setuptools, pip, wheel...done.
J:\py\pyfunds\palindrome (master){hg}
λ venv\Scripts\activate
(venv) J:\py\pyfunds\palindrome (master){hg}
```
Install the project:
```bash
λ python setup.py install
running install
running build
running build_py
creating build
creating build\lib
copying palindrome.py -> build\lib
running install_lib
copying build\lib\palindrome.py -> J:\py\pyfunds\palindrome\venv\Lib\site-packages
byte-compiling J:\py\pyfunds\palindrome\venv\Lib\site-packages\palindrome.py to palindrome.pyc
running install_egg_info
Writing J:\py\pyfunds\palindrome\venv\Lib\site-packages\palindrome-1.0-py2.7.egg-info
(venv) J:\py\pyfunds\palindrome (master){hg}
```
Change to parent folder to be sure we don't import the local file.
Start Python and import the module:
```bash
λ cd ..
(venv) J:\py\pyfunds (master){hg}
λ python
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import palindrome
>>> palindrome.__file__
'J:\\py\\pyfunds\\palindrome\\venv\\lib\\site-packages\\palindrome.pyc'
```
We can also create a distribution in a zip format
inside a `dist` subfolder:
```bash
(venv) J:\py\pyfunds (master){hg}
λ cd palindrome\
(venv) J:\py\pyfunds\palindrome (master){hg}
λ python setup.py sdist --format zip
running sdist
running check
warning: check: missing required meta-data: url
warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)
warning: sdist: standard file not found: should have one of README, README.txt
writing manifest file 'MANIFEST'
creating palindrome-1.0
copying files to palindrome-1.0...
copying palindrome.py -> palindrome-1.0
copying setup.py -> palindrome-1.0
creating dist
creating 'dist\palindrome-1.0.zip' and adding 'palindrome-1.0' to it
adding 'palindrome-1.0\palindrome.py'
adding 'palindrome-1.0\PKG-INFO'
adding 'palindrome-1.0\setup.py'
removing 'palindrome-1.0' (and everything under it)
```
We can also check all the possible distribution formats:
```bash
(venv) J:\py\pyfunds\palindrome (master){hg}
λ python setup.py sdist --help-formats
List of available source distribution formats:
  --formats=bztar  bzip2'ed tar-file
  --formats=gztar  gzip'ed tar-file
  --formats=tar    uncompressed tar file
  --formats=zip    ZIP file
  --formats=ztar   compressed tar file
```
And also general help on `setup.py`:
```bash
(venv) J:\py\pyfunds\palindrome (master){hg}
λ python setup.py --help
Common commands: (see '--help-commands' for more)

  setup.py build      will build the package underneath 'build/'
  setup.py install    will install the package

Global options:
  --verbose (-v)      run verbosely (default)
  --quiet (-q)        run quietly (turns verbosity off)
  --dry-run (-n)      don't actually do anything
  --help (-h)         show detailed help message
  --no-user-cfg       ignore pydistutils.cfg in your home directory
  --command-packages  list of packages that provide distutils commands

Information display options (just display information, ignore any commands)
  --help-commands     list all available commands
  --name              print package name
  --version (-V)      print package version
  --fullname          print <package name>-<version>
  --author            print the author's name
  --author-email      print the author's email address
  --maintainer        print the maintainer's name
  --maintainer-email  print the maintainer's email address
  --contact           print the maintainer's name if known, else the author's
  --contact-email     print the maintainer's email address if known, else the
                      author's
  --url               print the URL for this package
  --license           print the license of the package
  --licence           alias for --license
  --description       print the package description
  --long-description  print the long package description
  --platforms         print the list of platforms
  --classifiers       print the list of classifiers
  --keywords          print the list of keywords
  --provides          print the list of packages/modules provided
  --requires          print the list of packages/modules required
  --obsoletes         print the list of packages/modules made obsolete

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help
```

## Installing programs

Three most common installers:
* distutils
* easy_install
* pip

### distutil

This utility is useful to install programs from the command
prompt with `setup.py`. This should also work when the other
two utilities fail.

Most common usage:

> `python setup.py install`

Check where the package has been installed:
```bash
>>> import palindrome
>>> palindrome.__file__
'J:\\py\\pyfunds\\palindrome\\venv\\lib\\site-packages\\palindrome.pyc'
```



### easy_install and pip

Both utilities search for packages in the central Python repository,
a.k.a. `cheeseshop` and then download and install them with
their dependencies. You can browse the `cheeseshop` at
[pypi.python.org/pypi](http://pypi.python.org/pypi)

Installing with `easy_install`:

> `easy_install <package name>`

Installing with `pip`:

> `pip install <package name>`
