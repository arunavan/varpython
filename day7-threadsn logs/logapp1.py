import logging

# Configure logging
logging.basicConfig(level=logging.INFO ,format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
def calculate_sum(a, b):
   logging.debug(f"Calculating sum of {a} and {b}")
   try:
      x=10/0
      print(x)
   except Exception:
      logging.info('divide by zero')

   result = a + b
   logging.info(f"Sum calculated successfully: {result}")
   return result

# Main program
#if __name__ == "__main__":

logger = logging.getLogger(__name__)  

lf=logging.FileHandler('sample123.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
lf.setFormatter(formatter)

# add file handler to logger
logger.addHandler(lf)
#logging.basicConfig(level=logging.INFO, file='sample.log' )

logger.info("Starting the program")
result = calculate_sum(10, 20)
logger.info("Program completed")