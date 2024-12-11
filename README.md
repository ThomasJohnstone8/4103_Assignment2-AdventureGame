# 4103_Assignment2-AdventureGame


# Introduction

In this assignment I aim to make an adventure game where 2 player face each other in a 5x5 grid trying to reach the treasure. The treasure is randomly placed in the 5x5 grid and both player start at (0,0), the top left corner of the grid. Additionally, there are traps in the grid that the player must avoid because if the player hits too many traps then the will continue to loose health until they die. Once the player is dead the other player automatically wins. There are also power ups in the grid that allow the player to gain health or a hint to where the treasure is. Lastly, there is obstacles that the player cannot interact with and their purpose in the grid is to diversify the route to the treasure.


# Project Overview

During this project I used a Trello board to track my progress. Trello boards use the Kanban methodology. This is a scrum methodology which its main ideology is having 3 columns that you follow; To Do & Backlog, In progress and Done Tasks. With these 3 key concept I was able to visualise and see my progress being made as I was working on the project.

Other methodologies I considered was Waterfall. The waterfall methodology has you following a strict, linear step-by-step process that is easy to grasp. The reason I picked Kanban over waterfall is because I wanted the freedom to return to my backlog of tasks and do multiple parts of my project at once, so if i got stuck somewhere, I can shift my focus to one of my other tasks that are in my in progress column. This differs from waterfall where you follow a linear waterfall-like method that paths down.

Another methodology I decided not to use was scrum. Scrum focuses on small workloads in manageable chunks. These tasks are then followed in sprints. These sprints are quick hence the name "sprints" and can vary in time. Usually these times are discussed in the collaboration section of the methodology however, this is a solo project and therefore I would set them myself if i were to use scrum.


# Challenges and Solutions 

Some challenges I faced when making this project was the lack of time to collaborate with my tutor. This project was started during the first semester however, finished in the winter holidays meaning there was little to ask and collaborate with the tutor. In addition to this, another challenge I faced was migrating to a laptop from the virtual machine, this was quite easy but still took me some time to transfer files and more. Another challenges I dealt with was the searching algorithms. A lot of the coding of the functions and main gameplay loop were familiar after experiencing the lab activity and just a general increase in my knowledge of python. However, the searching algorithms were difficult and the way I solved it was I spent a lot of time revising notes and referring to Moodle documents for help understanding it. Another challenge I faced was some of the validation. At first my game would let the player move outside of the grid and the game would end. This was because of the validation I made that if only 1 person is in the grid the game ended. I then had to introduce validation so that only moves inside the grid were permitted and if the player tried to exit the grid, the questions would repeat in a while loop until a valid move was made.


# Search Algorithms

In this project I added 3 searching algorithms that can be used by the player to narrow down or find the treasure in the grid. I will talk about them one by one and the first one is BFS.

BFS or Breadth First Search is a searching algorithm that search all of everything before traversing to the next level. In my case the BFS is searching all of the top row that being (0,0) (0,1) (0,2) (0,3) (0,4) which is the 5 points in the top row. Then it will search the row under that until it reaches the treasure. As it is searching for the treasure it will determine the shortest path to get to the desired location (treasure) whilst also avoid any dependencies which in my game are the obstacles.

The next searching algorithm is Binary search. When using the Binary search, it is constantly splitting the selected row or column down until it finds the treasure. This algorithm divides and conquers the row or column continues to divide until the treasure is found. Binary search is also efficient in larger dataset and its as useful in this scenario as it would in another.

Lastly, DFS or Depth First Search is a searching algorithm that explores each cell in a row then backtracks and starts at the beginning then next row down until the treasure is reached. Additionally is an obstacle is on the path it will backtrack to just before the obstacle and continue its search for the treasure.


# Pseudocode and Flowchart

Flowchart? 
Psuedocode?

![image](https://github.com/user-attachments/assets/e755f9ea-89ee-445b-974e-95570b1944d0)



# Testing Evidence

| Test No. | Test Data | Expected Outcome | Actual Outcome | Pass/Fail? |
|:--------:|-----------|------------------|----------------|------------|
| 1 | What will happen when the player moves outside of the grid? | An appropriate error message is displayed | An error message stating "Invalid move. Please stay within grid boundaries. Try again." was displayed | Pass |
| 2 | What will happen when a trap is stepped on? | When a trapped is stepped on, the player will lose 2 health | The player lost 2 health and the counter went from the starting 10 down to 8 | Pass |
| 3 | What will happen when the user changes there mind and wants to change their move? | The player will an extra option for the player to return to the previous question | There is no option to return and change your move, once a move has been selected, the player must complete their turn | Fail |
| 4 | What happens when the user reaches the treasure? | The player will win and the game will end and display a congratulation message | The game only ends after the next player has completed their turn, this could be due to the gameplay loop however, the game still registers that the user is on top of the treasure and has won the game | Fail |
| 5 | What will happen when the player health reaches zero? | The game will recognise that a player has died and only 1 player is left and end the game | Similar to the treasure test, the game only recognises that the player has died after the next players turn has concluded | Fail |
| 6 | What will happen when a player tries to move into an obstacle | The game will recognise the obstacle and make the player take their turn again | The player didn't move to the obstacle and was made to take their turn again and also displayed this error message "Invalid move. You can't move into an obstacle or another player. Try again." | Pass |
| 7 | What will happen when a player tries to move on top of another player | The game will recognise a player is already taking up the square and will make the player take their turn again | Similar to the obstacle being hit, the player is make to retake their turn and an appropriate error message is displayed "Invalid move. You can't move into an obstacle or another player. Try again." | Pass |
| 8 | When the game starts is a 5x5 grid generated? | The grid is generate and have empty spaces, Power ups (P), Traps (X) and Obstacles (O) | The grid is generated with all relevant pieces randomly placed inside | Pass |
| 9 | When the game starts how many treasures are on the grid? | I expect there to be only 1 treasure on the grid | Only 1 treasure is on the grid at a time | Pass |
| 10 | Are the players are both starting at (0,0)? | The expected result is that the players both start at (0,0) in the grid | Both players start at the same point in the grid being (0,0) | Pass |
| 11 | Does the BFS give the player to shortest path to the treasure whilst also ensuring they don't die getting there? | Yes the BFS gives the shortest path to the player with directions as well | The BFS gives the shortest route to the player and also displays it in directions (up, down, left, right) | Pass |
| 12 | If the user enters the number 5 (which isn't an option), what will happen? | I think that the program will give an error message and repeat the question again | An error message appeared and the program repeated the question again which loops until a correct answer is given (1-4) | Pass |
| 13 | What happens when a player picks up a health power up when at 10 health points? | I expect the player to have 12 health and exceed the 10 they start with, thus giving the player an overheal | The player was given the extra 2 health and the health total was now 12 | Pass |
| 14 | What happens when the hint power up is picked up and the treasure is not nearby at all? | The hint will tell the user that the treasure is not nearby is but instead quiet a distance away | The power up hint will always say that the treasure is nearby even if it is not | Fail |
| 15 | Does the Binary search allow the user to search certain row or columns to narrow the search for the treasure? | I expect the Binary search to allow the player to search rows and columns to try find the treasure | The Binary search does allow the user to search for the treasure however, I am unsure how necessary this is because the BFS directs the player straight to the treasure | Fail |


# Conclusions

Overall this project was enjoyable and also a challenging experience. I feel as if a whole the project has improved my python skills at developing functions, loops, lists and more. Additionally, the searching algorithms were a surprising challenge that interested me and caught my curiosity.


# References

Refered to the Moodle documentation for the searching algorithms.



