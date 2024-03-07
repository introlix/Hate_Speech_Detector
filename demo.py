import sys
from hate.logger import logging
from hate.exception import CustomException
from hate.configuation.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hatespeech-15d3d.appspot.com", "dataset.zip", "dataset")