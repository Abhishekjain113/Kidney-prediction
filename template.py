import os 
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]:%(message)s:')

project_name = "cheast_Classifier"

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir = filepath.parent   # Get the parent directory

    # Create directory if it does not exist
    if not filedir.exists() and filedir != Path('.'):
        logging.info(f"Creating directory: {filedir}")
        filedir.mkdir(parents=True, exist_ok=True)
    else:
        logging.info(f"Directory already exists: {filedir}")

    # Create file if it does not exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
