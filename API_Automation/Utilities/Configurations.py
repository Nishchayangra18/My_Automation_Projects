import configparser


def Get_Config():
    config = configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    return config
