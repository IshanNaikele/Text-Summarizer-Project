import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from text_summarizer_project.logging import logger

logger.info("Hello, My Name is Ishan Naikele")
logger.info("Welcome to the custom Log")