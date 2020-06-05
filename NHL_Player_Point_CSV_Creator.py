from nhlscrapi.games.game import Game, GameKey, GameType
from nhlscrapi.games.eventsummary import EventSummary
import csv


def point_counter(start, end, team_name, season_year, player_num, file_name):
    '''
    This function creates a csv of a player's game log from the nhlcrapi.
    start - enter the number of the game you want to start getting data from
    end - enter the number of the game you want to end on
    The start/end number correspond to specific game numbers. So for example if you want
    to get data for the whole season then enter 1 for start and 1231 for end. (1230 games played in 30 team NHL season)

    team_name - Name of the player's team given as a string in all capitals and spaces included
    season_year - Enter the season year as a number using the year that season ended on.
    For example, for the 2009-2010 season you would enter 2010.
    player_num - Enter the number of player
    file_name - Enter in a string of what you want the output file name to be.
    For example, 'red.csv'
    '''
    season = season_year
    game_type = GameType.Regular
    team = team_name
    file = file_name

    csv_file = open(file, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Points', 'Vs_Team', 'Home/Away'])

    for i in range(start, end):
        game_num = i
        game_key = GameKey(season, game_type, game_num)

        game = Game(game_key)
        event_summary = EventSummary(game_key)

        if game.matchup is not None:
            if game.matchup['home'] == team:
                # If the home team is the supplied team, assign the home_players attribute to home_players
                # This assigns a dictionary of players to home_players
                home_players = event_summary.home_players

                # Check if the player played in said game by using his number(player_num)
                if player_num in home_players:
                    # Points earned in that game is within the home_players dictionary
                    points = home_players[19]['p']
                    # Setting the vs_team variable to the opponent
                    vs_team = game.matchup['away']
                    home_or_away = 'Home'

                    csv_writer.writerow([points, vs_team, home_or_away])

            if game.matchup['away'] == team:
                # If the away team is is the supplied team, assign the away_players attribute to away_players
                # This assigns a dictionary of players to home_players
                away_players = event_summary.away_players

                # Check if the player played in said game by using his number(player_num)
                if player_num in away_players:
                    # Points earned in that game is within the home_players dictionary
                    points = away_players[player_num]['p']
                    # Setting the vs_team variable to the opponent
                    vs_team = game.matchup['home']
                    home_or_away = 'Away'

                    csv_writer.writerow([points, vs_team, home_or_away])

    csv_file.close()
