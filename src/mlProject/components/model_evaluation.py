from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import joblib
from mlProject.utils.common import save_json
from mlProject.config.configuration import ModelEvaluationConfig





class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config



    def evaluation_metrics(self, actual, predicted):
        mse = mean_squared_error(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)

        return mse, mae, r2 
    
    

    def save_results(self):
        test = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_name)

        test_x = test.drop(columns=[self.config.target_column], axis=1)
        test_y = test[[self.config.target_column]]

        predictions = model.predict(test_x)
        mse, mae, r2 = self.evaluation_metrics(test_y, predictions)

        scores = {"mse": mse, "mae": mae, "r2": r2}
        save_json(path=Path(self.config.matric_file_path), data=scores)

