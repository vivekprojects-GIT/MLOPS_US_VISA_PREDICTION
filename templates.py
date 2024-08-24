from pathlib import Path
import os
from stat import FILE_ATTRIBUTE_DIRECTORY

Project_Name = "us_visa"

list_of_files = [
    f"{Project_Name}/__init__.py",
    f"{Project_Name}/Components/__init__.py",
    f"{Project_Name}/Components/data_ingestion.py",
    f"{Project_Name}/components/data_validation.py",
    f"{Project_Name}/components/data_transformation.py",
    f"{Project_Name}/components/model_evaluation.py",
    f"{Project_Name}/components/model_trainer.py",
    f"{Project_Name}/components/model_pusher.py",
    f"{Project_Name}/configuration/__init__.py",
    f"{Project_Name}/constants/__init__.py",
    f"{Project_Name}/entity/__init__.py",
    f"{Project_Name}/entity/artifact_entity.py",
    f"{Project_Name}/entity/config_entity.py",
    f"{Project_Name}/exception/__init__.py",
    f"{Project_Name}/logger/__init__.py",
    f"{Project_Name}/pipeline/__init__.py",
    f"{Project_Name}/pipeline/train_pipeline.py",
    f"{Project_Name}/pipeline/prediction_pipeline.py",
    f"{Project_Name}/utils/__init__.py",
    f"{Project_Name}/utils/main_utlils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filepath = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
    else:
        print(f"File {filepath} already exists.")






