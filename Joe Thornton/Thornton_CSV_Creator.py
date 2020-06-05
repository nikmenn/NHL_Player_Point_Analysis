from nhlscrapi.games.game import Game, GameKey, GameType
from nhlscrapi.games.eventsummary import EventSummary
import csv


def point_counter(start, end):
    season = 2010
    game_type = GameType.Regular
    san_jose = 'SAN JOSE SHARKS'

    csv_file = open('joe_thornton_points_summary.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Points', 'Vs_Team', 'Home/Away'])

    for i in range(start, end):
        game_num = i
        game_key = GameKey(season, game_type, game_num)

        game = Game(game_key)
        event_summary = EventSummary(game_key)

        if game.matchup is not None:
            # Check if San Jose was the home team
            if game.matchup['home'] == san_jose:
                # If the home team is San Jose assign the home_players attribute to home_players
                # This assigns a dictionary of players to home_players
                home_players = event_summary.home_players

                # Check if Joe Thornton played that game by checking if his number is in the dictionary
                # His number is 19
                if 19 in home_players:
                    # Points earned in that game is within the home_players dictionary
                    points = home_players[19]['p']
                    # Setting the vs_team variable to the team the Sharks played against
                    vs_team = game.matchup['away']
                    home_or_away = 'Home'

                    csv_writer.writerow([points, vs_team, home_or_away])

            # Check if San Jose was the away team
            if game.matchup['away'] == san_jose:
                # If the away team is San Jose assign the away_players attribute to away_players
                # This assigns a dictionary of players to home_players
                away_players = event_summary.away_players

                # Check if Joe Thornton played that game by checking if his number is in the dictionary
                # His number is 19
                if 19 in away_players:
                    # Points earned in that game is within the home_players dictionary
                    points = away_players[19]['p']
                    # Setting the vs_team variable to the team the Sharks played against
                    vs_team = game.matchup['home']
                    home_or_away = 'Away'

                    csv_writer.writerow([points, vs_team, home_or_away])

    csv_file.close()


# 1230 games in the NHL regular season
point_counter(1, 1231)
