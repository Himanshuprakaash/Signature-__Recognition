import os
import sys
import dill
import yaml
import base64
from src.logger import logging
from src import CustomException

def save_object(file_path, obj :object) -> None:
    logging.info(f"Saving object to file: {file_path}")

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved successfully to file: {file_path}")

    except Exception as e:
        logging.error(f"Error occurred while saving object to file: {file_path}")
        raise CustomException(e, sys) from e
    
def load_object(file_path) -> object:
    logging.info(f"Loading object from file: {file_path}")

    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info(f"Object loaded successfully from file: {file_path}")
        return obj

    except Exception as e:
        logging.error(f"Error occurred while loading object from file: {file_path}")
        raise CustomException(e, sys) from e
    

def image_to_base64(image_path :str) -> str:
    logging.info(f"Converting image to base64: {image_path}")                                           
    
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        logging.info(f"Image converted to base64 successfully: {image_path}")
        return encoded_string
    except Exception as e:
        logging.error(f"Error occurred while converting image to base64: {image_path}")
        raise CustomException(e, sys) from e    