class EmailClient(object):

    def __init__(self, config):
        self.__config = config
        self.connect(self.__config)

    def connect(self, config):
        #Implement function here
        pass