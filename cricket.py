import random
from collections import deque

toss = ["Heads", "Tails"]
choose_to = ["Bat", "Bowl"]
run = [-1, 0, 1, 2, 3, 4, 6]


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
        self.batsmen = players
        self.bowlers = players[6:]

    def select_captain(self, captain):
        self.captain = captain

    def next_batsman(self, pos):
        return self.batsmen[pos]

    def next_bowler(self, pos):
        return self.bowlers[pos]


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


class Umpire:
    def __init__(self, overs):
        self.score = 0
        self.wickets = 0
        self.overs = overs

    def simulate_ball(self):
        outcome = random.choice(run)
        if outcome > -1:
            self.score += outcome
        else:
            self.wickets += 1
        return outcome


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
        self.umpire = Umpire(5)
        self.commentator = Commentator()
        self.stricker = None
        self.non_stricker = None
        self.bowler = None

    def toss_coin(self):
        self.commentator.provide_commentary(
            "What a beautiful day today! It's a "+field.size+" & "+field.pitch_conditions+" field. Both captains walking into the field for the toss.")
        call = random.choice(toss)
        self.commentator.provide_commentary(
            call+" is the call by "+team1.captain.name)
        coin_outcome = random.choice(toss)
        self.commentator.provide_commentary("And it's "+coin_outcome)
        choose = random.choice(choose_to)
        toss_res = {}
        if call == coin_outcome:
            self.commentator.provide_commentary(
                team1.name+" wins the toss. " + team1.captain.name+" chooses to "+choose)
            if choose == "Bat":
                toss_res["Bat"] = team1
                toss_res["Bowl"] = team2
            else:
                toss_res["Bat"] = team2
                toss_res["Bowl"] = team1
        else:
            self.commentator.provide_commentary(
                team2.name+" wins the toss. " + team2.captain.name+" chooses to "+choose)
            if choose == "Bat":
                toss_res["Bat"] = team2
                toss_res["Bowl"] = team1
            else:
                toss_res["Bat"] = team1
                toss_res["Bowl"] = team2
        return toss_res

    def start_match(self, res, target):
        self.stricker = res['Bat'].next_batsman(0)
        self.non_stricker = res['Bat'].next_batsman(1)
        self.umpire.score = 0
        self.umpire.wickets = 0
        over = 0
        end = False

        self.bowler = res['Bowl'].next_bowler(over)
        for i in range(self.umpire.overs):
            for j in range(6):
                if self.umpire.wickets == 10:
                    end = True
                    break
                outcome = self.umpire.simulate_ball()
                if outcome == -1:
                    print(self.stricker.name+" is OUT")
                    self.stricker = res['Bat'].next_batsman(
                        self.umpire.wickets+1)

                else:
                    print(self.stricker.name + " scores "+str(outcome)+" runs")
                    if self.umpire.score >= target:
                        end = True
                        break
                    if outcome % 2 != 0:
                        temp = self.stricker
                        self.stricker = self.non_stricker
                        self.non_stricker = temp
            over += 1
            if end | over == self.umpire.overs:
                print("Innings over")
                break
            temp = self.stricker
            self.stricker = self.non_stricker
            self.non_stricker = temp
            print("Over change")
        print("Total runs scored: "+str(self.umpire.score))
        return self.umpire.score

    def change_innings(self, res, target):
        print("Next innings")
        temp = res['Bowl']
        res['Bowl'] = res['Bat']
        res['Bat'] = temp
        return self.start_match(res, target)

    def end_match(self, res, target, chase):
        if chase >= target:
            print(res['Bat'].name+" wins")
        else:
            print(res['Bowl'].name+" wins")

            # Team India
player1 = Player("Rohit Sharma", 0.8, 0.2, 0.99, 0.8, 0.9)
player2 = Player("Shikhar Dhawan", 0.8, 0.2, 0.99, 0.8, 0.9)
player3 = Player("Virat Kohli", 0.8, 0.2, 0.99, 0.8, 0.9)
player4 = Player("Rishabh Pant", 0.8, 0.2, 0.99, 0.8, 0.9)
player5 = Player("MS Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9)
player6 = Player("Hardik Pandya", 0.8, 0.2, 0.99, 0.8, 0.9)
player7 = Player("Ravindra Jadeja", 0.8, 0.2, 0.99, 0.8, 0.9)
player8 = Player("Jasprit Bumrah", 0.8, 0.2, 0.99, 0.8, 0.9)
player9 = Player("Kuldeep Yadav", 0.8, 0.2, 0.99, 0.8, 0.9)
player10 = Player("Bhuvaneshwar Kumar", 0.8, 0.2, 0.99, 0.8, 0.9)
player11 = Player("Yuzvendra Chahal", 0.8, 0.2, 0.99, 0.8, 0.9)

# Team Australia
player12 = Player("David Warner", 0.8, 0.2, 0.99, 0.8, 0.9)
player13 = Player("Aaron Finch", 0.8, 0.2, 0.99, 0.8, 0.9)
player14 = Player("Steven Smith", 0.8, 0.2, 0.99, 0.8, 0.9)
player15 = Player("Usman Khawaja", 0.8, 0.2, 0.99, 0.8, 0.9)
player16 = Player("Marcus Stoinis", 0.8, 0.2, 0.99, 0.8, 0.9)
player17 = Player("Glenn Maxwell", 0.8, 0.2, 0.99, 0.8, 0.9)
player18 = Player("Alex Carey", 0.8, 0.2, 0.99, 0.8, 0.9)
player19 = Player("Nathan Coulter-Nile", 0.8, 0.2, 0.99, 0.8, 0.9)
player20 = Player("Pat Cummins", 0.8, 0.2, 0.99, 0.8, 0.9)
player21 = Player("Mitchell Starc", 0.8, 0.2, 0.99, 0.8, 0.9)
player22 = Player("Adam Zampa", 0.8, 0.2, 0.99, 0.8, 0.9)
team1 = Team("India", [player1, player2, player3, player4, player5,
             player6, player7, player8, player9, player10, player11])
team1.select_captain(player5)

team2 = Team("Australia", [player12, player13, player14, player15, player16,
             player17, player18, player19, player20, player21, player22])
team2.select_captain(player13)


field = Field("Large", 0.8, "Dry", 0.1)

match = Match(team1, team2, field)
toss_res = match.toss_coin()
target = match.start_match(toss_res, 99999)
chase = match.change_innings(toss_res, target+1)
match.end_match(toss_res, target, chase)
