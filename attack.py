
class Attack:
    """
    A class representing an attack

    Attributes:
        name (int): Name of attack
        power (int): Power of attack
        accuracy (int): Accuracy of attack, out of 100.
        range (int): Number of squares 
        cooldown (int): Number of turns before next use (0 => no cooldown)
    
    Constructor: (attack_id)

    Methods: TODO
        getInfo(self): Returns the info.
    """
    # Attributes
    __name = None
    __power = None
    __accuracy = None
    __range = None
    __cooldown = None

    # Constructor
    def __init__(self, attack_id):
        # Interpreting file with attack_id to get attack_info
        with open('gameinfostorage/attack_id.txt', 'r') as attack_file:
                str_to_find = '!!' + attack_id # !!{ID} marker
                file_lines = attack_file.readlines()
                for line in file_lines:
                    if str_to_find in line: # if line contains attack id
                        attack_info = [i for i in line.split('~')[1].split('/')] # Attack information split into a list: [image, name, ]
                        break
        
        try: # error handling if attack_info does not exist
            bool(attack_info)
        except:
            raise Exception(f"No attack with ID {attack_id} found, or attack file info corrupted")

        name, power, accuracy, range, cooldown = attack_info # unpacks all attack information
        
        # Initialising attack object.
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
