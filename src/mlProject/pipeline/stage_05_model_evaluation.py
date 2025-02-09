from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger





STAGE_NAME = "Model Evaluation "

class ModelTrainingEvaluationPipeline:
    def __init__(self):
        pass




    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()




if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        obj = ModelTrainingEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e