from configparser import ConfigParser


def read_configuration(catagory, key):
    config = ConfigParser()
    config.read("configuration/config.ini")
    return config.get(catagory, key)