import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")
WRONGPASS = os.getenv("WRONG_PASSWORD")