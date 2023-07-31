"""contacts/__main__.py"""

from contacts6 import cli
from contacts6 import __app_name__

def main():
    
    cli.app(__app_name__)
    
if __name__ == '__main__':
    main()