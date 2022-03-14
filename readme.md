# March Madness 2022 Bracket Simulator

A little program to fill out my bracket for the 2022 NCAA Tournament. This is for a league with an upset bonus, so I'm using Elo to calculate an expected value for points from each matchup, and choosing the team with the highest EV.

## Output Example

Round 1 Game 1
Gonzaga (2769) vs. Georgia State (2138)
97% vs. 3%
0.97pts vs. 0.41pts
Best choice: Gonzaga

Round 1 Game 2
Boise State (2588) vs. Memphis (2468)
67% vs. 33%
0.67pts vs. 0.67pts
Best choice: Memphis

Round 1 Game 3
UConn (2637) vs. New Mexico State (2362)
83% vs. 17%
0.83pts vs. 1.36pts
Best choice: New Mexico State

.
.
.


Round 4 Game 4
Creighton (2604) vs. Iowa State (2509)
63% vs. 37%
5.07pts vs. 3.67pts
Best choice: Creighton

Round 5 Game 1
Gonzaga (2769) vs. Indiana (2453)
86% vs. 14%
13.77pts vs. 3.77pts
Best choice: Gonzaga

Round 5 Game 2
Arizona (2826) vs. Creighton (2604)
78% vs. 22%
12.51pts vs. 5.23pts
Best choice: Arizona

Round 6 Game 1
Gonzaga (2769) vs. Arizona (2826)
42% vs. 58%
13.40pts vs. 18.60pts
Best choice: Arizona