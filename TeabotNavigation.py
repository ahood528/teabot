import teabot

class TNavigation :
    def __init__(self,init) :
        print("TNavigation made")

    def perceive(self, percept, action) :
        assert type(percept) is teabot.TeabotPercept
        assert type(action) is teabot.TeabotAction
        # modify action based on percept
        print("nav percept received")

    def teabot_moves() :
        # return number of moves since call to this method
        return 0
