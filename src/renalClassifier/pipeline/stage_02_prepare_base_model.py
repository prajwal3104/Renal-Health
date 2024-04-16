from renalClassifier.config.configuration import ConfigurationManager
from renalClassifier.components.prepare_base_model import PrepareBaseModel 
from renalClassifier import logger

STAGE_NAME = "Stage 02: Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage name: {STAGE_NAME} started <<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage name: {STAGE_NAME} completed!<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"stage name: {STAGE_NAME} error: {e}")
        raise e