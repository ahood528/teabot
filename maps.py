# Maps classes and code


# class used to represent all the objects found when parsing the map files
class ParsedMap :
    def __init__(self) :
        self.human_init = []
        self.teabot_init = []
        self.rooms_init = []
        self.obstacles_init = [] # furniture, etc

# takes a list of file names
# returns instance of ParsedMap
def parse_maps(maps_to_parse) :
    print('parse_maps called')
    x = ParsedMap()
    return x
