# settings.py
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)

# Default Environments Variables
SERVER_SECRET_KEY = os.environ.get("SERVER_SECRET_KEY")
SERVER_DEFAULT_PORT = int(os.environ.get("PORT", 5000))
