import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from tracking import Tracker
import configs

class MainGrid:
	tracker = Tracker() # Static
	
	def __init__(self):
		self.grid = Gtk.Grid()
		self.grid.set_margin_top(10)
		self.grid.set_margin_bottom(10)
	
	def create(self):
		boxLabels = BoxLabels().create()
		boxAreas = BoxAreas().create()
		boxReasons = BoxReasons().create()
		btnTrack = BtnTrack.create()
		
		self.grid.attach(boxLabels, 0, 0, 1, 2)
		self.grid.attach(boxAreas, 1, 0, 2, 1)
		self.grid.attach(boxReasons, 1, 1, 2, 1)
		self.grid.attach(btnTrack, 3, 0, 1, 2)
		return self.grid
		
class BoxLabels:
	def __init__(self):
		self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
		self.box.set_margin_top(8)
		self.box.set_margin_left(10)
		self.box.set_margin_right(10)
		
	def create(self):
		labelArea = Gtk.Label(label='Area: ')
		labelArea.set_halign(Gtk.Align.END)
		labelArea.set_valign(Gtk.Align.CENTER)
		self.box.add(labelArea)
		
		labelReason = Gtk.Label(label='Reason: ')
		labelReason.set_halign(Gtk.Align.END)
		labelReason.set_valign(Gtk.Align.CENTER)
		self.box.add(labelReason)
		return self.box

class BoxAreas:
	def __init__(self):
		self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
		self.btns = []
		
	def create(self):
		areas = configs.AREAS
		
		last_btn = None
		for area in areas:
			self.btns.append(Gtk.RadioButton.new_with_label_from_widget(last_btn, area))
			self.btns[-1].set_mode(False)
			self.box.pack_start(self.btns[-1], True, True, 0)
			last_btn = self.btns[-1]
			
		self.init_events()
		return self.box
		
	def update_area(self, btn):
		if btn.get_active():
			MainGrid.tracker.stop_tracking()
			MainGrid.tracker.set_area_tracking(btn.get_label())
			BtnTrack.refresh_label()
		
	def init_events(self):
		if len(self.btns) > 0:
			MainGrid.tracker.set_area_tracking(self.btns[0].get_label())
		
		for btn in self.btns:
			btn.connect('clicked', self.update_area)
			
class BoxReasons:
	def __init__(self):
		self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
		self.btns = []
		
	def create(self):
		reasons = configs.REASONS
		
		last_btn = None
		for reason in reasons:
			self.btns.append(Gtk.RadioButton.new_with_label_from_widget(last_btn, reason))
			self.btns[-1].set_mode(False)
			self.box.pack_start(self.btns[-1], True, True, 0)
			last_btn = self.btns[-1]
			
		self.init_events()
		return self.box
		
	def update_reason(self, btn):
		if btn.get_active():
			MainGrid.tracker.stop_tracking()
			MainGrid.tracker.set_reason_tracking(btn.get_label())
			BtnTrack.refresh_label()
		
	def init_events(self):
		if len(self.btns) > 0:
			MainGrid.tracker.set_reason_tracking(self.btns[0].get_label())
			
		for btn in self.btns:
			btn.connect('clicked', self.update_reason)
		
class BtnTrack:
	btn = Gtk.Button(label='Track') # Static
		
	def create(): # Static
		BtnTrack.btn.set_margin_left(10)
		BtnTrack.btn.set_margin_right(10)
		BtnTrack.init_events()
		return BtnTrack.btn
		
	def refresh_label(): # Static
		BtnTrack.btn.set_label('Stop ' if MainGrid.tracker.tracking else 'Track')
		
	def toggle_tracking(btn): # Static
		MainGrid.tracker.toggle_tracking()
		BtnTrack.refresh_label()
		
	def init_events(): # Static
		BtnTrack.btn.connect('clicked', BtnTrack.toggle_tracking)
