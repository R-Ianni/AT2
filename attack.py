class Attack:
    # Attributes
    __name = None
    __power = None
    __accuracy = None
    __range = None
    __cooldown = None

    # Constructor
    def __init__(self, name, power, accuracy, range, cooldown):
        self.setName(name)
        self.setPower(power)
        self.setAccuracy(accuracy)
        self.setRange(range)
        self.setCooldown(cooldown)

    # Getters
    def getName(self):
        return self.__name
    def getPower(self):
        return self.__power
    def getAccuracy(self):
        return self.__accuracy
    def getRange(self):
        return self.__range
    def getCooldown(self):
        return self.__cooldown

    # Setters
    def setName(self, name):
        self.__name = name
    def setPower(self, power):
        self.__power = power
    def setAccuracy(self, accuracy):
        self.__accuracy = accuracy
    def setRange(self, range):
        self.__range = range
    def setCooldown(self, cooldown):
        self.__cooldown = cooldown
