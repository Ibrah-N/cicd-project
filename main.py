from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_training import ModelTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelTrainingEvaluationPipeline


STAGE_NAME = "Data Ingestion "
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\n\n\nx=========================x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data Validation "
try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started  <<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<<\n\n\n\nx=========================x")
        
except Exception as e:
    logger.info(e)
    raise e




STAGE_NAME = "Data Transformation "
try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} Started  <<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} Completed  <<<<<<<<\n\n\n\nx=========================x")

except Exception as e:
    logger.info(e)
    raise e



STAGE_NAME = "Model Training "
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<\n\n\n\nx=========================x")

except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Evaluation "
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    obj = ModelTrainingEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\n\n\nx=========================x")

except Exception as e:
    logger.exception(e)
    raise e