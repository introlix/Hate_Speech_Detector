import sys
from hate.logger import logging
from hate.exception import CustomException

def devide(a,b):
    try:
        logging.info(f"Dividing {a} by {b}")
        return a/b
    except Exception as e:
        raise CustomException(e, sys)
    
devide(5, 0)