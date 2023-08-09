"""hw9_contacts/__init__.py"""
from typing import Annotated

TITLE: str = 'Your Contacts'
__app_name__: str = 'contacts'
__version__: str = '0.1.0'

DATABASE_PATH: str = 'db'
DATABASE: Annotated[str, 'path to the database'] = f'{DATABASE_PATH}/{__app_name__}.db'

