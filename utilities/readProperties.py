import configparser

config = configparser.RawConfigParser()
configFilePath = r'C:\Users\kumarmu\Documents\pythonSelenium\nopcommerceapp\Configurations\config.ini'
print(configFilePath)
config.read(configFilePath)

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commoninfo','baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('commoninfo','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('commoninfo', 'password')
        return password