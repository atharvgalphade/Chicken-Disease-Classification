from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.data_ingestion import dataIngestion 
from CNNClassifier import logger

STAGE_NAME= "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        di_config= ConfigurationManager() # create object of class
        data_ingestion_config= di_config.get_data_ingestion_config() #call function and store in other object
        data_ingestion=dataIngestion(config=data_ingestion_config) #create object for class
        data_ingestion.download_file() # call function
        data_ingestion.extract_zip_file() #call function

if __name__=='__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<{STAGE_NAME} started>>>>>>>>>>>>>>")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<{STAGE_NAME} completed>>>>>>>>>>>>>>")
    
    except Exception as e:
        logger.exception(e)
        raise e