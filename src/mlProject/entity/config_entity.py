from dataclasses import dataclass
from pathlib import Path





@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path 
    unzip_dir: Path





@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    status_file: str 
    allschema: dict 




@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path 
    data_path: Path




@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path 
    test_data_path: Path 
    model_name: Path
    alpha: float
    l1_ratio: float
    target_column: str





@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir : Path 
    test_data_path: Path 
    model_name: Path 
    all_params: dict 
    matric_file_path: Path
    target_column: str