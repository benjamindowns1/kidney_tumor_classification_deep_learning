from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_model import PreapareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage{STAGE_NAME} started <<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)




STAGE_NAME = "Prepare base model"

try:
    logger.info(f"******************")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    obj = PreapareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Training"

try:
    logger.info(f"****************************")
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e