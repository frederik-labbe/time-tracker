import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import UI

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Time Tracker")
		
	def create(self):
		self.add(
			UI.MainGrid().create()
		)
		self.init_events()
		
	def init_events(self):
		self.connect('destroy', Gtk.main_quit)
		
if __name__ == '__main__':
	win = MainWindow()
	win.create()
	win.show_all()
	Gtk.main()
