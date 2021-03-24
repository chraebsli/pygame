# Instructions
## Login
Here you can login with your account. If you don't have one, you can create an account with the sign up button.

## Registration
You can sign you up with a username and a password. If the username is taken, the filed will clear and you have to enter an other one.

## Titlescreen
Here you can choose between 'Play' to start the game, 'Leaderboard' to see the current local Leaderboard (we are working to make it global), skins to choose an other skin if you have enought coins on your account, the menu button for the ingame instructions or the color settings or you can quit the game.

## Skins
Here you can select an other skin. But you have to play a few rounds before to get points to unlock skins.

## Quit
You can easy quit the game.

## Options
On the first screen from the options page, you can see the instructions.  
On the second one, you can choose the colors for the walls and the trail. You can choose between rainbow (we don't recomend this for people with epilepsis), a random color, red, blue, green or on the empty field you can write an other color if the box is green. The colors have to be from the pygame colors or they can be a hexadecimal color (like #363636)

## Play
To play the game, you have to click on this button. After a 3 seconds timer, the game starts. See #Gameplay for more.  


# Gameplay
## Goal
The goal in this game is to get as many points in a short time. The points is the most important for the ranking but the time you need to get thoose points also matters.

## Rules
- Don't touch a wall
- Don't touch you trial
- To save your points: 
    - get 150 points
    - reach the end


## Controls
Button  | Action
------------- | -------------
W / &#8593;  | move up
A / &#8592;  | move left
S / &#8595;  | move down
D / &#8595;  | move right
Q            | show points/time
esc          | go to titlescreen

# More 
## Actual
We are working on it for a global Leaderboard and a gloabl SQL Server for the login and the points that you can login from any device

## Versions
### 1.0
- move player with WASD
- background
- animated end
### 2.0
- random walls
- titlescreen
- trial 
### 3.0
- collisiondetect for walls
- better sprites
- add playername on titlescreen
### 4.0 
- local leaderboard with json
- screen for leaderboard
### 5.0 
- global leaderboard with git 
- leaderboard has better design
- website for leaderboard
- ingame instructions
### 6.0
- only local leaderboard
- no global leaderboard
### 6.1
- loginscreen
- leaderboard with sql
