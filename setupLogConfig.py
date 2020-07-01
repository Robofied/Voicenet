# -*- coding: utf-8 -*-

##########################
# AUTHOR : PRANEET NIGAM
##########################

# built-in module
import os
import logging

# third-party module
import yaml

def setup_logging(
    default_path:str = './logConfig.yaml', 
    default_level:int = logging.INFO,
    env_key:str = 'LOG_CFC'
):
    """
    Setup logging configuration
    """
    
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as file:
            config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Logging configuration setup..")