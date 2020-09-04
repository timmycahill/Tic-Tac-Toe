# Menu Controller
from menu import Menu

class MenuController:
	def __init__(self):
		self.menu = Menu()
		pass

	def get_title(self):
		return self.menu.get_title()

	def get_image_path(self):
		return self.menu.get_image_path()
