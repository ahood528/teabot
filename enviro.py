# Environment class and code

class ObstacleInit :
    def __init__() :
        print ('obstacle init made')

class Obstacle :
    def __init__(self, init) :
        print ('obstacle made')

class RoomInit :
    def __init__(self) :
        print ('room made')

class Room :
    def __init__(self, init) :
        print ('room made')

class Environment :
    def __init__(self, humans, teabots, rooms, obstacles) :
        print("Environment made")
        self.humans = humans
        self.teabots = teabots
        self.rooms = rooms
        self.obstacles = obstacles

