import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # Note: You can add different data transformation techniques such as Scaler, PCA and all
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model
    # I am only adding train_test_spliting cz this data is already cleaned up
    def scalling(self):
        pass

    def encoding(self):
        pass 

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data splitted into train and test sets")
        logger.info(f"shape of training set: {train.shape}")
        logger.info(f"Shpae of test set: {test.shape}")

