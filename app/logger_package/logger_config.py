import logging

class LoggerClass:

    @property
    def logger_obj(self):
        logger = logging.getLogger("flask_project")
        logger.setLevel(logging.DEBUG)

        #create a file handler
        file_handler = logging.FileHandler('log_history.log')
        file_handler.setLevel(logging.DEBUG)

        #create a logger formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        #add the file handler to logger
        logger.addHandler(file_handler)
        return logger


