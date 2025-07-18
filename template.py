import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
project_name = "DataScienceProject"
list_of_files = [
    ".github/workflows/.gitkeep", # Placeholder for GitHub Actions CI/CD workflows
    f"src/{project_name}/__init__.py",#Main package init file
    f"src/{project_name}/components/__init__.py", # Holds core ML components like transformers, trainers, evaluators
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # Reusable utility functions (e.g., file handling, logging setup)
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py", #Reads from config files, organizes pipeline setup
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "schema.yaml",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]
for file_path in list_of_files:
    filepath = Path(file_path) #Convert the string path into a Path object from pathlib for easier path manipulation.
    filedir,filename = os.path.split(filepath)#Split the full path into the directory (filedir) and file name (filename).
    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    if (not os.path.exists(filepath))or (os.path.getsize(filepath)==0 ): #Check if the file does not exist OR if it exists but is empty.
        # Create the file if it does not exist or is empty
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")   