from collections import namedtuple
from datetime import datetime
import uuid
from visa.config.configuration import Configuration
from visa.logger import logging
from visa.exception import CustomException
from threading import Thread
from typing import List

from multiprocessing import Process
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.components.data_ingestion import DataIngestion
import os
import sys
import pandas as pd


class Pipeline:

    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise CustomException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys) from e

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys) from e
