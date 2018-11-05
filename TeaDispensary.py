import teabot # to access TeabotPercept and TeabotAction

class Dispensary :
    def __init__(self,init) :
        print("dispensary made")

    def perceive(self, percept, action) :
        assert type(percept) is teabot.TeabotPercept
        assert type(action) is teabot.TeabotAction
        # modify action based on percept
        print("disp percept received")

    def tea_served() :
        # return teas served since last call of this method
        return 0
