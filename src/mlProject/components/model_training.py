import os
import pandas as pd
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig




class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config



    def train(self):
        try: 
            print(self.config.train_data_path, self.config.test_data_path)
            train_ =  pd.read_csv(self.config.train_data_path)
            test_ = pd.read_csv(self.config.test_data_path)


            train_x = train_.drop([self.config.target_column], axis=1)
            train_y = train_[[self.config.target_column]]

            test_x = test_.drop([self.config.target_column], axis=1)
            test_y = test_[[self.config.target_column]]

            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42) 
            lr.fit(train_x, train_y)

            joblib.dump(lr, filename=self.config.model_name)

        except Exception as e:
            raise e