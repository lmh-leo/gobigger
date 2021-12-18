import random
from gobigger.server import Server
from gobigger.render import EnvRender

server = Server()
render = EnvRender(server.map_width, server.map_height)
server.set_render(render)
server.start()
player_names = server.get_player_names_with_team()
# get [[team1_player1, team1_player2], [team2_player1, team2_player2], ...]
for i in range(10000):
    actions = {player_name: [random.uniform(-1, 1), random.uniform(-1, 1), -1] \
               for team in player_names for player_name in team}
    if not server.step(actions):
        global_state, screen_data_players = server.obs()
        print('[{}] leaderboard={}'.format(i, global_state['leaderboard']))
    else:
        print('finish game!')
        break
server.close()
hzq = []