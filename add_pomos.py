from pomo import Pomo
import datetime

def add_pomos():
	num_added = 0
	task = input("Describe your task briefly:\n")
	print("How many pomos would you like to dedicate to this task?\n")
	while num_added not in [1,2,3,4]:
		try:
			num_added = int(input("Please input a number between 1 and 4.\n"))
		except:
			continue
	time_created = datetime.datetime.now()
	pomos = [Pomo(id_no=i+1,task=task,completed=False,time_created=time_created,time_finished=0,time_remaining=5) for i in range(num_added)]
	return pomos