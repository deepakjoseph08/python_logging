import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='app.log',level=logging.DEBUG)
def test():
    logging.info("test")
    logging.error("asd")



test()

