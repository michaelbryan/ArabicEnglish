import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class HomeScreen(AnchorLayout):

	def __init__(self, **kwargs):
		searchbar = TextInput(multiline=False)

		super(HomeScreen, self).__init__(**kwargs)
		#translatebutton = Button(text='Translate')
		#self.add_widget(translatebutton)

class MyApp(App):

    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    MyApp().run()
