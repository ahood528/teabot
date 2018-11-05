# Environment class and code
import humans
import teabot

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

    def make_human_percept(self,human) :
        assert type(human) is humans.Human
        retrunValue = humans.HumanPercept()
        return returnValue

    def receive_human_action(self, human, action) :
        assert type(action) is humans.HumanAction
        print("received h action")

    def make_teabot_percept(self, teabot) :
        assert type(teabot) is teabot.Teabot
        returnValue = teabot.TeabotPercept()
        return returnValue;

    def receive_teabot_action(self, teabot, action) :
        assert type(teabot) is teabot.Teabot
        assert type(action) is teabot.TeabotAction
        print("received t action")
