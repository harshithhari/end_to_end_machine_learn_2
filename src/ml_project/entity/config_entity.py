from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:# The class here used is from library dataclass hence we no need to use the self while declaring a variable.
    root_dir: Path
    source_URL: str
    local_data_file : Path
    unzip_dir:Path
    
    