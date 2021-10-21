# A "pomo" is an object which contains a "task message" for the pomo
# The user can define the message upon the creation of each pomo, OR can pre-define pomos and select one from a list to tackle

# The program should display a timer as it counts down
# Give the user the option to type "do-later" notes if something pops into their head while working on their task

# Statistics: the user can see lifetime usage statistics, pomos per day, pomos per week, etc.

from timers import display_timer,break_timer
from pomo import Pomo
from add_pomos import add_pomos
import yaml
from yaml.loader import SafeLoader

with open("./config.yaml") as f:
	data = yaml.load(f,Loader=SafeLoader)
	print(data)

current_pomos = data.get('pomodoros')

for pomo in current_pomos:
	

i = 0
pomos = add_pomos()
for pomo in pomos:
	i += 1
	display_timer(pomo)
	if i != len(pomos):
		input("Hit ENTER to start the break timer.")
		break_timer(5)
		input("Hit ENTER to start the next pomo.")
	else:
		print("All pomos completed!")