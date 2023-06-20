import random


class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batsmen = []
        self.bowlers = []

    def select_captain(self, captain):
        self.captain = captain

    def choose_batsmen(self, count):
        self.batsmen = random.sample(self.players, count)

    def choose_bowler(self):
        self.bowlers = random.choice(self.players)


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


class Umpire:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def simulate_ball(self, batsman, bowler):
        # Perform simulations based on player stats, field conditions, etc.
        # Update the score, wickets, overs, and other relevant information
        pass


class Commentator:
    def __init__(self):
        pass

    def provide_commentary(self, ball_result):
        # Generate commentary based on the ball_result and match stats
        pass


class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire()
        self.commentator = Commentator()

    def start_match(self):
        # Perform toss, choose batting/bowling order, etc.
        # Start the match and simulate ball-by-ball actions
        pass

    def change_innings(self):
        # Change the batting and bowling teams for the second innings
        pass

    def end_match(self):
        # Display final score, result, and any other relevant information
        pass


# Usage example:
player1 = Player("MS Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.85, 0.1, 0.95, 0.7, 0.95)
team1 = Team("India", [player1, player2])
team1.select_captain(player1)
team1.choose_batsmen(2)
team1.choose_bowler()

team2 = Team("Australia", [player1, player2])
team2.select_captain(player1)
team2.choose_batsmen(2)
team2.choose_bowler()

field = Field("Large", 0.8, "Dry", 0.1)

match = Match(team1, team2, field)
match.start_match()
