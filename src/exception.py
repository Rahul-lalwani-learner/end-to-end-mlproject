import sys # provides various functions and variables used to manipulate different parts of the Python runtime environment
from src.logger import logging


def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #exc_info() provide details about the exception that is currently being handled 
    file_name = exc_tb.tb_frame.f_code.co_filename #co_filename is the filename from which the code was compiled
    error_message = "Error occured in python Script name [{0}] line number [{1}] with error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomExecption(Exception): 
    def __init__(self, error_message, error_detail:sys): 
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self): 
        return self.error_message
    
"""
if __name__=="__main__": 
    try: 
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error occured")
        raise CustomExecption(e, sys)
"""