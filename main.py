from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f"<<<<<<<<<<<<<{STAGE_NAME} started>>>>>>>>>>>>>>")
    dataingestion=DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f"<<<<<<<<<<<<<{STAGE_NAME} completed>>>>>>>>>>>>>>")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Prepare Base Model"
try:
    logger.info(f"<<<<<<<<<<<<<<<{STAGE_NAME} started>>>>>>>>>>>>>")
    basemodel= PrepareBaseModelPipeline()
    basemodel.main()
    logger.info(f"<<<<<<<<<<<<<<<{STAGE_NAME} completed>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
    