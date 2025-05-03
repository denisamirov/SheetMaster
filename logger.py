import logging

def logger_setup():
    logging.basicConfig(level=logging.INFO, filename="app.log",filemode="a", format="%(asctime)s %(levelname)s %(message)s" )

