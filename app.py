from src.logger import logging
from src.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("the execution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)   