import logging
import os

PATH_TO_FILE_lOG = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'application.log')


def setup_logging(app_name: str) -> logging.Logger:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=PATH_TO_FILE_lOG,  # Запись логов в файл
        filemode='w')

    return logging.getLogger(app_name)
