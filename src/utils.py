import os
import sys
import numpy as np
import pandas as pd
# import pickle
from src.exception import CustomExecption
from src.logger import logging
import dill

def save_object(file_path,obj): 
    try: 
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as f:
            # pickle.dump(obj, f)
            dill.dump(obj, f)

            
    except Exception as e: 
        
        raise CustomExecption(e,sys)