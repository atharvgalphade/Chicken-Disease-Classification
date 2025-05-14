from CNNClassifier.constants import *
from CNNClassifier.utils.common import read_yaml,create_directories
from CNNClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    #Constructor with two optional arguments:
    #config_filepath: Path to your config.yaml.
    #params_filepath: Path to your params.yaml.
    def __init__(
        self,
        config_filepath= CONFIG_FILE_PATH,
        params_filepath= PARAMS_FILE_PATH):
        #Reads the config.yaml file and stores it in self.config as a Python dictionary
        self.config= read_yaml(config_filepath)
        #Reads the params.yaml file and stores it in self.params as a dictionary.
        self.params= read_yaml(params_filepath)
        #Creates the base directory (e.g., artifacts/) specified in config.yaml under the key artifacts_root.
        create_directories([self.config.artifacts_root], verbose=True)
        
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        
        create_directories([config.root_dir], verbose=True)
        
        data_ingestion_config= DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config