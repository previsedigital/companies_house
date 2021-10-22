import os
import tempfile


DEFAULT_README_PATH: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'README.md'))
DEFAULT_DEFINITIONS_FILE: str = os.path.join(tempfile.gettempdir(), "definition.csv")