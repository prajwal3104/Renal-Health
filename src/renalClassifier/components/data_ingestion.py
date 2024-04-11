import os
import zipfile
import gdown
from src.renalClassifier import logger
from src.renalClassifier.utils.common import get_size
from src.renalClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self) -> str:
        """
        Fetch the data from the source URL and store it in the local data path
        """

        try:
            dataset_url = self.config.source_URL
            zip_download_path = self.config.local_data_file

            # Skip download if file already exists
            if os.path.exists(zip_download_path):
                logger.info(f"Dataset file already exists at {zip_download_path}. Skipping download.")
                return zip_download_path

            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading the dataset from {dataset_url} to file {zip_download_path}")

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_path)

            logger.info(f"Downloaded the dataset from {dataset_url} to file {zip_download_path}")
            return zip_download_path

        except Exception as e:
            logger.error(f"Error downloading the dataset from {dataset_url} to file {zip_download_path}")
            raise e
        

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
