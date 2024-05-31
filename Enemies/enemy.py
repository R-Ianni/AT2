import pygame
import random

class Enemy:
# Attributes
    __surf = None
    __rect = None
    __name = None
    __attack = None
    __defence = None
    __level = None
    __weapon = None
    __hit_points = None
    __max_health = None
    __is_alive = None
    __world_speed = None
    __movement_points = None
    __movement_pattern = None
    __experience_yield = None
    __board_position = None

    # Constructor
    def __init__(self, surf, rect, name, attack, defence, level, weapon, hit_points, max_health, is_alive, world_speed, movement_points, movement_pattern, experience_yield, board_position):
        self.setSurf(surf)
        self.setRect(rect)
        self.setName(name)
        self.setAttack(attack)
        self.setDefence(defence)
        self.setLevel(level)
        self.setWeapon(weapon)
        self.setHit_points(hit_points)
        self.setMaxHealth(max_health)
        self.setIsAlive(is_alive)
        self.setWorldSpeed(world_speed)
        self.setMovementPoints(movement_points)
        self.setMovementPattern(movement_pattern)
        self.setExperienceYield(experience_yield)
        self.setBoardPosition(board_position)

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getName(self):
        return self.__name
    def getAttack(self):
        return self.__attack
    def getDefence(self):
        return self.__defence
    def getLevel(self):
        return self.__level
    def getWeapon(self):
        return self.__weapon
    def getHit_points(self):
        return self.__hit_points
    def getMaxHealth(self):
        return self.__max_health
    def getIsAlive(self):
        return self.__is_alive
    def getWorldSpeed(self):
        return self.__world_speed
    def getMovementPoints(self):
        return self.__movement_points
    def getMovementPattern(self):
        return self.__movement_pattern
    def getExperienceYield(self):
        return self.__experience_yield
    def getBoardPosition(self):
        return self.__position

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setName(self, name):
        self.__name = name
    def setAttack(self, attack):
        self.__attack = attack
    def setDefence(self, defence):
        self.__defence = defence
    def setLevel(self, level):
        self.__level = level
    def setWeapon(self, weapon):
        self.__weapon = weapon
    def setHit_points(self, hit_points):
        self.__hit_points = hit_points
    def setMaxHealth(self, max_health):
        self.__max_health = max_health
    def setIsAlive(self, is_alive):
        self.__is_alive = is_alive
    def setWorldSpeed(self, world_speed):
        self.__world_speed = world_speed
    def setMovementPoints(self, movement_points):
        self.__movement_points = movement_points
    def setMovementPattern(self, movement_pattern):
        self.__movement_pattern = movement_pattern
    def setExperienceYield(self, experience_yield):
        self.__experience_yield = experience_yield
    def setBoardPosition(self, position):
        self.__position = position

# TODO methods

    def draw(self):
        # Adjust the position to ensure the image does not overflow the window boundaries
        adjusted_position = [
            max(0, min(self.window.get_width() - self.image.get_width(), self.position[0])),
            max(0, min(self.window.get_height() - self.image.get_height(), self.position[1]))
        ]
        
        # Draw the enemy image on the window at the adjusted position
        self.window.blit(self.image, adjusted_position)
