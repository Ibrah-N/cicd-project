from mlProject import logger
from mlProject.components.data_validation import DataValidation
from mlProject.config.configuration import ConfigurationManager



STAGE_NAME = "Data Validation Starge"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()





if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started  <<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started  <<<<<<<<<\n\nx==========x")
            
    except Exception as e:
        logger.info(e)
        raise e