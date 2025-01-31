from pathlib import Path
from typing import Dict, Any, Union, AnyStr
import logging
import yaml

from .loader import Loader

# Setup the logging



class Config:
    def __init__(self, file: Union[Path, AnyStr] = None):
        pass

    @staticmethod
    def load(path: Union[Path, AnyStr]) -> Dict[AnyStr, Any]:
        # Logging the start of the loading process
        logging.info(f"Starting to load configuration from {path}")
        try:
            with open(path, "r") as f:
                config = yaml.load(f, Loader=Loader)
                logging.info(f"Successfully loaded configuration from {path}")
                return config
        except FileNotFoundError:
            logging.error(f"Config file {path} not found")
            raise FileNotFoundError(f"Config file {path} not found")
        except yaml.YAMLError as e:
            logging.error(f"YAML error occurred while loading the configuration: {e}")
            raise yaml.YAMLError(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise Exception(e)

    @staticmethod
    def from_file(path: Union[Path, AnyStr]) -> Dict[AnyStr, Any]:
        logging.info(f"Creating Config from file: {path}")
        config = Config.load(path)
        return config

    @staticmethod
    def from_dict(config: Dict[AnyStr, Any]) -> Dict[AnyStr, Any]:
        logging.info(f"Creating Config from dictionary")
        return Config(**config)
