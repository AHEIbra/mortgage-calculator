'''
    Why does this file exist?

    Well the first module running is not called by its actual name, but the interpreter
    will rename it to __main__. This means that if another piece of code wants to import from
    the module it will trigger the import a second time under its real name and your code gets
    imported twice!

    i.e. When you run `python -m mortgage_calculator` python will execute `__main__.py` as a script.
    This means that there won't be any ``mortgage_calculator.__main__`` in ``sys.modules``.

    See:
    -   https://click.palletsprojects.com/en/5.x/setuptools/

'''


import sys

from mortgage_calculator.cli import cli

if __name__ == '__main__':
    sys.exit(cli())
