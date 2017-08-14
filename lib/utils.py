
from ConfigParser import SafeConfigParser

class Config:
    def __init__(self):
        parser = SafeConfigParser()
        parser.read('lib/config.ini')
        self.uri = parser.get('Config', 'uri')
        # self.user = parser.get('Config', 'admin_login')
        # self.password = parser.get('Config', 'admin_password')

    def print_config(self):
        for prop in self.__dict__:
            print('%s = %s' % (prop, self.__dict__.get(prop)))

