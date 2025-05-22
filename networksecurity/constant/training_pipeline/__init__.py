import os 
import sys
import numpy
import pandas as pd


'''
defining common constant variable for training pipeline
'''

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

'''
Data Ingestion related constant 
'''

DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str = "BADARAI"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATABASE_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATABASE_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATIO: float = 0.2

