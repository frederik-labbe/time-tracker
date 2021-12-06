import threading
import time
import datetime
import os
import configs

class TimeTracking:
	def __init__(self):
		self.active = False
		self.area = None
		self.reason = None
		t = threading.Thread(target=self.tracking_thread_func, args=(1,))
		t.start()
		
	def tracking_thread_func(self, name):
		while True:
			time.sleep(configs.WRITE_INTERVAL_SEC)
			
			if self.active:
				dateNow = datetime.datetime.now()
				
				if dateNow.hour >= configs.WORKING_HOUR_START and dateNow.hour < configs.WORKING_HOUR_END:			
					output_file = os.path.join(configs.OUTPUT_FOLDER, f'{self.area}-{self.reason}.data')
					
					tracked_time = configs.WRITE_INTERVAL_SEC
					
					if os.path.exists(output_file):
						with open(output_file, 'r') as f:
							tracked_time = tracked_time + int(f.read())
						
					with open(output_file, 'w') as f:
						f.write(str(tracked_time))
		
	def start(self, area, reason):
		self.active = False
		self.area = area
		self.reason = reason
		self.active = True
		
	def stop(self):
		self.active = False
		
