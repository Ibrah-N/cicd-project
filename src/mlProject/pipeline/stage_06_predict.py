import joblib
from pathlib import Path 





class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model_v1.joblib'))


    
    def predict(self, sample):
        prediction = self.model.predict(sample)


        return prediction