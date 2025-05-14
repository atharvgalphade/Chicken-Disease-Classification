import os
from box.exceptions import BoxValueError
import yaml
from CNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox # suppose we have dict we have to call it as dict["key"] so that we can get value. 
#if we use configbox we can do dict.key and then get the value for it
from pathlib import Path 
from typing import Any
import base64 

@ensure_annotations #this will help to raise the error if the function definition datatype doesnot match function call datatype
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads the yaml file and returns
    
    Args: path_to_yaml (str): path like input
    
    Raises: Valueerror: if yaml file is empty
    e: empty file 
    
    Returns: ConfigBox: ConfigBox Type"""
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
#@ensure_annotations
def create_directories(path_to_directories: list[str], verbose: True):
    """create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to false. 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    
    Args: apth: path to json file 
    data: data to be saved in json file
    """
    with open(path,"w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"Json file saved at: {path}")