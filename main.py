print('Welcome to CS 528 Teabot')

# import modules
import maps
import enviro
import teabot
import humans

# hard-coded values for testing
maps_to_parse = ['map1.svg']
simulation_loops = 10

# variables

# parse command line arguments and
# override hard-coded values

# initialize task environment
# load maps
parsed_map = maps.parse_maps(maps_to_parse)
humans = []
teabots = []
rooms = []
obstacles = [] # furniture, etc.

for hinit in parsed_map.human_init :
    humans.append(human.Human(hinit))

for tinit in parsed_map.teabot_init :
    teabots.append(teabot.Teabot(tinit))

for rinit in parsed_map.rooms_init :
    rooms.append(enviro.Room(rinit))

for oinit in parsed_map.obstacles_init :
    obstacles.append(enviro.Obstacle(oinit))

# create environment
envi = enviro.Environment(humans, teabots, rooms, obstacles)

# run simulation
for i in range(simulation_loops) :
    for h in envi.humans :
        h.perceive(envi.make_human_percept(h))
        envi.receive_human_action(h, h.act())
    for t in envi.teabots :
        t.perceive(envi.make_teabot_percept(t))
        envi.receive_teabot_action(t, t.act())
    print('sim loop', i)

# print stats
print("teas served:", teabot.Teabot.teas_served)
print("teabot distance:", teabot.Teabot.teabot_moves)
