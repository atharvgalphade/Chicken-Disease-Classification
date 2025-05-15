from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f"<<<<<<<<<<<<<{STAGE_NAME} started>>>>>>>>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<<<<<{STAGE_NAME} completed>>>>>>>>>>>>>>")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Prepare Base Model"
try:
    logger.info(f"<<<<<<<<<<<<<<<{STAGE_NAME} started>>>>>>>>>>>>>")
    obj= PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<<<<<<<{STAGE_NAME} completed>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
    