import logging
def test_loging():
    logger = logging.getLogger(__name__)
    fileHandler =  logging.FileHandler(filename='.\\Logs\\automation.log')
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
