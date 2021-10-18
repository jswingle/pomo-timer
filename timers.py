import time
from pomo import Pomo

def display_timer(pomodoro):
	print("Press CTRL+C to pause.")
	while pomodoro.time_remaining:
		try:
			minutes, seconds = divmod(pomodoro.time_remaining,60)
			time_format = 'Time remaining: {:02d}:{:02d}'.format(minutes,seconds)
			print(time_format, end='\r')
			time.sleep(1)
			pomodoro.time_remaining -= 1
		except KeyboardInterrupt:
			print('\nPomo stopped! (You can resume the same pomo by running "pomo start" again)')
			break

	if not pomodoro.time_remaining:
		print("Time remaining: 00:00\n\nTimer over!\n")
		pomodoro.completed = True

def break_timer(time_remaining):
	print("Press CTRL+C to skip break.")
	while time_remaining:
		try:
			minutes, seconds = divmod(time_remaining,60)
			time_format = 'Time remaining: {:02d}:{:02d}'.format(minutes,seconds)
			print(time_format, end='\r')
			time.sleep(1)
			time_remaining -= 1
		except KeyboardInterrupt:
			print('\nBreak skipped!')
			break	

	if not time_remaining:
		print("Time remaining: 00:00\n\nTimer over!\n")