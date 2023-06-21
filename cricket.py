import random

toss = ["Heads", "Tails"]
choose_to = ["Bat", "Bowl"]


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
        pass


class Commentator:
    def __init__(self):
        pass

    def provide_commentary(self, comment):
        print(comment)


class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.commentator = Commentator()

    def toss_coin(self):
        self.commentator.provide_commentary(
            "What a beautiful day today! It's a "+field.size+" & "+field.pitch_conditions+" field. Both captains walking into the field for the toss.")
        call = random.choice(toss)
        self.commentator.provide_commentary(
            call+" is the call by "+team1.captain.name)
        coin_outcome = random.choice(toss)
        self.commentator.provide_commentary("And it's "+coin_outcome)
        choose = random.choice(choose_to)
        if call == coin_outcome:
            self.commentator.provide_commentary(
                team1.captain.name+" chooses to "+choose)
        else:
            self.commentator.provide_commentary(
                team2.captain.name+" chooses to "+choose)

    def start_match(self):
        pass

    def change_innings(self):
        pass

    def end_match(self):
        pass


# Team India
player1 = Player("Rohit Sharma", 0.8, 0.2, 0.99, 0.8, 0.9)
player2 = Player("Shikhar Dhawan", 0.8, 0.2, 0.99, 0.8, 0.9)
player3 = Player("Virat Kohli", 0.8, 0.2, 0.99, 0.8, 0.9)
player4 = Player("Rishabh Pant", 0.8, 0.2, 0.99, 0.8, 0.9)
player5 = Player("Hardik Pandya", 0.8, 0.2, 0.99, 0.8, 0.9)
player6 = Player("MS Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9)
player7 = Player("Ravindra Jadeja", 0.8, 0.2, 0.99, 0.8, 0.9)
player8 = Player("Jasprit Bumrah", 0.8, 0.2, 0.99, 0.8, 0.9)
player9 = Player("Kuldeep Yadav", 0.8, 0.2, 0.99, 0.8, 0.9)
player10 = Player("Bhuvaneshwar Kumar", 0.8, 0.2, 0.99, 0.8, 0.9)
player11 = Player("Yuzvendra Chahal", 0.8, 0.2, 0.99, 0.8, 0.9)

# Team Australia
player12 = Player("David Warner ", 0.8, 0.2, 0.99, 0.8, 0.9)
player13 = Player("Aaron Finch", 0.8, 0.2, 0.99, 0.8, 0.9)
player14 = Player("Steven Smith", 0.8, 0.2, 0.99, 0.8, 0.9)
player15 = Player("Usman Khawaja", 0.8, 0.2, 0.99, 0.8, 0.9)
player16 = Player("Glenn Maxwell", 0.8, 0.2, 0.99, 0.8, 0.9)
player17 = Player("Marcus Stoinis", 0.8, 0.2, 0.99, 0.8, 0.9)
player18 = Player("Alex Carey", 0.8, 0.2, 0.99, 0.8, 0.9)
player19 = Player("Nathan Coulter-Nile", 0.8, 0.2, 0.99, 0.8, 0.9)
player20 = Player("Pat Cummins", 0.8, 0.2, 0.99, 0.8, 0.9)
player21 = Player("Mitchell Starc", 0.8, 0.2, 0.99, 0.8, 0.9)
player22 = Player("Adam Zampa", 0.8, 0.2, 0.99, 0.8, 0.9)
team1 = Team("India", [player1, player2, player3, player4, player5,
             player6, player7, player8, player9, player10, player11])
team1.select_captain(player6)

team2 = Team("Australia", [player12, player13, player14, player15, player16,
             player17, player18, player19, player20, player21, player22])
team2.select_captain(player13)


field = Field("Large", 0.8, "Dry", 0.1)

match = Match(team1, team2, field)
match.toss_coin()
