from pomo import Pomo
import datetime
import yaml
from yaml import SafeLoader


def add_pomos():
	with open('./config.yaml', 'r') as f:
		data = yaml.load(f,Loader=SafeLoader)

	task = input("Describe your task briefly:\n")
	num_added = 0
	print("How many pomos would you like to dedicate to this task?\n")
	while num_added not in [1,2,3,4]:
		try:
			num_added = int(input("Please input a number between 1 and 4.\n"))
		except:
			continue
	time_created = datetime.datetime.now()
	next_id = data.get('settings').get('next_id')
	time_set = data.get('settings').get('pomodoro_time')

	for new_pomo in len(num_added):
		attributes = {'id_no':next_id,'task':task,'completed':False,'time_created':time_created,'time_finished':0,'time_remaining':time_set}
		data['pomodoros'].append(attributes)
		next_id += 1

	data['next_id'] = next_id

	with open('./config.yaml', 'w') as f:
		yaml.dump(data, f)

if __name__ == '__main__':
	add_pomos()