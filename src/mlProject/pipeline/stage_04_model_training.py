from mlProject.components.model_training import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger





STAGE_NAME = "Model Training "

class ModelTrainingPipeline:
    def __init__(self):
        pass



    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_configuration()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()





if __name__=="__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e