import logging

from ...settings import project_env

logger = logging.getLogger('project')

# logger config
c_handler = logging.StreamHandler()
c_handler.setFormatter(logging.Formatter(fmt='{asctime} | {levelname:<10} | {message}', datefmt='%d/%m/%y %H:%M:%S', style='{'))
logger.addHandler(c_handler)
logger.setLevel(project_env.LOGGING_LEVEL)
