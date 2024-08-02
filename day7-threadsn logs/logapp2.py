
import logging

logger = logging.getLogger(__name__)   # logapp2.py
# Configure logging
formatter=logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
lf=logging.FileHandler('mysample123.log')
lf.setFormatter(formatter)
logger.addHandler(lf)
def getemi():
    logger.info('function started')
    print('emi amount is 9999')
    logger.info('function end')
logger.info('function called 1st time')
getemi()
logger.info('funciton called 2nd time')
getemi()