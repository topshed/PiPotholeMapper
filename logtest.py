import logging
import time
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
tmstmp = time.strftime("%Y%m%d-%H%M%S")
#logging.basicConfig(format='%(asctime)s %(message)s',filename='pothole.log',level=logging.DEBUG)
#logging.basicConfig(filename='pothole.log',level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s',
    filename='pothole'+str(tmstmp) +'.log',
                             level=logging.DEBUG)
logging.info('starting')
