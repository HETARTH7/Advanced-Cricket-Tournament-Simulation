# ADVANCED CRICKET TOURNAMENT SIMULATION

## Features

- Classes and Objects:

  The code defines several classes such as Player, Team, Field, Umpire, Commentator, and Match. These classes represent different entities in a cricket match and contain relevant attributes and methods.

- Randomization:

  The random module is imported to introduce randomness in the simulation. It is used to simulate the toss outcome, choose batting or bowling, and generate random outcomes for runs scored, wickets taken, and dismissals.

- Data Structures:

  The deque class from the collections module is imported to create a queue-like structure for the list of players.
  Dictionary is used to maintain the toss result

- Player, Team, and Field Initialization:

  The code initializes player objects with attributes such as name, batting rating, bowling rating, fielding rating, running rating, and experience.
  Two teams, "India" and "Australia," are created using the Team class. Each team consists of a list of player objects.
  The Team class also has methods to select a team captain and determine the next batsman and bowler.

- Umpire and Commentator:

  The Umpire class simulates the scoring and wicket-taking process. It assigns ratings to batting, bowling, fielding, and running attributes of players to calculate the total rating. Based on the rating, it generates random outcomes for runs scored and wickets taken.
  The Commentator class provides commentary for various events in the match.

- Match Simulation:

  The Match class simulates the entire match. It starts with a toss simulation, where a random outcome is chosen for the toss, and the winning team decides whether to bat or bowl.
  The match progresses with each team taking turns to bat and bowl. The start_match method simulates the batting innings, while the change_innings method switches the roles of the teams for the second innings.
  The end_match method displays the final scoreboard and determines the winning team based on the target and total runs scored.

- Output:

  The code includes print statements to provide commentary and display the match results, including individual player statistics and the winning team.

## Run the project

Clone the project

```bash
  git clone https://github.com/HETARTH7/Advanced-Cricket-Tournament-Simulation.git
```

Go to the project directory

```bash
  cd Advanced-Cricket-Tournament-Simulation
```

Run the script

```bash
  py cricket.py
```
