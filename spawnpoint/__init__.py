from mcdreforged.api.all import *
import minecraft_data_api

def spawnpoint(server: ServerInterface,player: str):
    if player != '(Console)':
        pos = minecraft_data_api.get_player_info(player, 'Pos')
        server.execute('spawnpoint {} {}'.format(player, ' '.join(pos)))

def player_name(is_player: bool,player: str):
    if is_player:
        return player
    else:
        return '(Console)'

def on_load(server: PluginServerInterface, old):
    server.register_help_message('!!sp','设置重生点')
    server.register_command(
        Literal('!!sp')
        .runs(lambda src: spawnpoint(server,player_name(src.is_player,src.player)))
    )
