from renalClassifier.config.configuration import ConfigurationManager
from renalClassifier.components.model_training import Training
from renalClassifier import logger

STAGE_NAME = "Stage 03: Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage name: {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage name: {STAGE_NAME} completed!<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"stage name: {STAGE_NAME} error: {e}")
        raise e
