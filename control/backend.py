import socket
import numpy as np
import threading
import logging
import time

time.time()

logging.basicConfig(filename="logs/flight_"+str(int(time.time()))+".log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s ")#(%(filename)s:%(lineno)d)")
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

logger.info("Started ROV control backend")


class ROV:
    def __init__(self, ip):
        logger.info("Attempting to create ROV object...")
        self.addr = (ip, 36543)
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            logger.error("Failed to establish socket!")
            logger.info("Followup error info: "+str(e))
        self.message = []
        for i in range(1024):
            self.message.append(np.ubyte(0))
            
        logger.info("Created new ROV object with ip '"+ip+"'")
        
    def connect(self):
        logger.info("Attempting to connect to ROV @"+self.addr[0]+":"+str(self.addr[1])+"...")
        try:
            self.client.connect(self.addr)
        except Exception as e:
            logger.error("Failed to connect to ROV @"+self.addr[0]+":"+str(self.addr[1])+"!")
            logger.info("Followup error info: "+str(e))
        else:
            logger.info("Connected to ROV successfully")
            
        return False
    
    def __send_packet(self) -> bytes:
        try:
            logger.debug(self.message)
            self.client.send(bytes(self.message))
        except Exception:
            logger.error("C2S packet failed transmission")

        try:
            message = self.client.recv(1024)
        except Exception:
            logger.error("S2C packet failed transmission")
            message = False
        
        self.message = []
        for i in range(1024):
            self.message.append(np.ubyte(0))
            
        return message
    
    def packet(self, message) -> bytes:
        for index, msg in enumerate(message):
            self.message[index] = np.ubyte(msg)
        
        if len(self.message) > 1024:
            logger.warning("Abnormal C2S packet length of "+str(len(self.message)))
            
        return self.__send_packet()