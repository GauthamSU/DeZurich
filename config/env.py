from pathlib import Path
import environ

env = environ.FileAwareEnv()

BASE_DIR = Path(__file__).resolve().parent.parent

APPS_DIR = BASE_DIR / 'lounge_app_services'