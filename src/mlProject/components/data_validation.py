from mlProject import logger
import os
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig





class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config 
        

    def validate_all_columns(self):
        try:
            validation_status = False

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            schema_cols = self.config.allschema.keys()
        
            for col in all_cols:
                if col not in schema_cols:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        
            return validation_status

        except Exception as e:
            raise e