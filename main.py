from src.renalClassifier import logger
from src.renalClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.renalClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"----> stage {STAGE_NAME} started <----")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"----> stage {STAGE_NAME} completed <----\n\nX########X")
except Exception as e:
    logger.error(f"----> stage {STAGE_NAME} failed <----")
    logger.error(e)
    raise e

STAGE_NAME = "Stage 02: Prepare Base Model Stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e