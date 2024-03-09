from src.renalClassifier import logger
from src.renalClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

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

