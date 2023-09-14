import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Face-expressions-recognition"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data_loader.py",
    f"src/{project_name}/parameters.py",
    f"src/{project_name}/optimize_hyperparameters.py",
    f"src/{project_name}/model.py",
    f"src/{project_name}/train.py",
    f"src/{project_name}/predict.py",
    f"src/{project_name}/logging/__init__.py",
    "app.py",
    "requirements.txt",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")