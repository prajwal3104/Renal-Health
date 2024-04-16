from src.renalClassifier.config.configuration import ConfigurationManager
from src.renalClassifier.components.model_evaluation_mlflow import Evaluation
from src.renalClassifier import logger

STAGE_NAME = "Stage 04: Model Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage name: {STAGE_NAME} started <<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage name: {STAGE_NAME} completed!<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"stage name: {STAGE_NAME} error: {e}")
        raise e