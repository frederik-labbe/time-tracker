import tracking_thread

class Tracker:
	def __init__(self):
		self.tracking = False
		self.tracked_area = None
		self.tracked_reason = None
		self.tracking_thread = tracking_thread.TimeTracking()

	def toggle_tracking(self):
		self.tracking = not self.tracking
		
		if self.tracking:
			self.start_tracking()
		else:
			self.stop_tracking()
			
	def set_area_tracking(self, area):
		self.tracked_area = area
			
	def set_reason_tracking(self, reason):
		self.tracked_reason = reason
			
	def start_tracking(self):
		if not self.tracking_thread.active:
			self.tracking_thread.start(self.tracked_area, self.tracked_reason)
		
	def stop_tracking(self):
		if self.tracking_thread.active:
			self.tracking_thread.stop()
