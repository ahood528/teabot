# teabot code
import TeabotNavigation
import TeaDispensary

class TeabotInit :
    # this class gets passed to Teabot constructor
    def __init__(self) :
        print("teabot init data made")

class TeabotPercept :
    def __init__(self) :
        print("teabot percept made")

class TeabotAction :
    def __init__(self) :
        print("teabot action made")

class Teabot :
    teas_served = 0
    teabot_moves = 0
    def __init__(self, init) :
        print("Teabot made")
        # initialize using init
        self.dispensary = TeaDispensary.Dispensary(init)
        self.navigation = TeabotNavigation.TNavigation(init)
        self.action = TeabotAction()

    def perceive(self, percept) :
        self.dispensary.perceive(percept, self.action)
        self.navigation.perceive(percept, self.action)

    def act(self) :
        teas_served += self.dispensary.tea_served()
        teabot_moves += self.navigation.teabot_moves()
        return self.action
