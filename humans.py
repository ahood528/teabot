# code for the other agents in simulation, Humans

class HumanPercept :
    def __init__(self) :
        print("human percept made")

class HumanAction :
    def __init__(self) :
        print("human action made")

class HumanInit :
    def __init__(self):
        print('human init made')

class Human :
    def __init__(self, human_init) :
        print('made human')

    def perceive(self, percept) :
        print('h percept perceived')

    def act(self) :
        returnValue = HumanAction()
        return returnValue
