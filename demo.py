from visa.pipeline.pipeline import Pipeline
from visa.exception import CustomException
from visa.logger import logging
from visa.config.configuration import Configuration
from visa.components.data_ingestion import DataIngestion
import os


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        logging.error(f"{e}")


if __name__ == "__main__":
    main()
