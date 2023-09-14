import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Face-expressions-recognition"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/data_loader.py",
    f"src/parameters.py",
    f"src/optimize_hyperparameters.py",
    f"src/model.py",
    f"src/train.py",
    f"src/predict.py",
    f"src/logging/__init__.py",
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