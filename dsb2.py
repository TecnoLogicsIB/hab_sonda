import time
from w1thermsensor import W1ThermSensor
import logging
import thingspeak

logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/dsb2.log')
fh = logging.FileHandler('logs/dbs.log')    
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

sensor = W1ThermSensor()
temperatura = [] 
canal = thingspeak.Channel('2052291', 'TMN63LV2K9555WOD')

try:
  while True:
    for sensor in W1ThermSensor.get_available_sensors():
      temperatura.append(round(sensor.get_temperature(),2)) 
      print("sensor",sensor.id,"retorna",sensor.get_temperature(),"C","\t", end=" ")  
    print('')
    logger.info(str(temperatura[0]) + '|' + str(temperatura[1])) 
    dada_nubol = canal.update ({1:temperatura[0], 2:temperatura[1]});
    temperatura.clear()
    time.sleep(1)	
     
except:
  print ("execucio interrompuda")
