from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen


class Main(MDApp):
	def __init__(self):
		self.book = '1 john'
		self.chapter = 4
		self.verse = 19

	def build(self):
		screen = MDScreen()
		btn = MDRectangleFlatButton(text=self.pullVerse('1 john', 4, 19),
			pos_hint={'center_x': 0.5, 'center_y': 0.5}
			)
		screen.add_widget(btn) 
		return screen

	def pullVerse(self, book, chapter, verse):
		verse = "We love because he first loved us."
		return verse

Main().run()