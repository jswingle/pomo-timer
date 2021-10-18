# Defaults: 25-minute timer period, but should be customizable with a CLI option
# 5-minute break period, but should be customizable
# 30-minute break after completing 4 pomos, but should be customizable time and number required
# Toggle option for the user to give a "warning" when a certain number of minutes remain on the timer

# A "pomo" is an object which contains a "task message" for the pomo
# The user can define the message upon the creation of each pomo, OR can pre-define pomos and select one from a list to tackle

# The program should "alert" at time periods - pre-defined sound effect, but can be customized to any sound file
# The program should display a timer as it counts down
# Give the user the option to type "do-later" notes if something pops into their head while working on their task

# Statistics: the user can see lifetime usage statistics, pomos per day, pomos per week, etc.

# Use YAML to hold user settings

from timers import display_timer,break_timer
from pomo import Pomo
from add_pomos import add_pomos

i = 0
pomos = add_pomos()
for pomo in pomos:
	print(pomo.id_no,pomo.task)
for pomo in pomos:
	i += 1
	display_timer(pomo)
	if i != len(pomos):
		input("Hit ENTER to start the break timer.")
		break_timer(5)
		input("Hit ENTER to start the next pomo.")
	else:
		print("All pomos completed!")