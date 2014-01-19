import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class VerbChartScreen(BoxLayout):



	#class HomeScreen(FloatLayout):

		#results_screen = ResultsScreen()


		'''def __init__(self, **kwargs):
			super(HomeScreen, self).__init__(**kwargs)
			searchbar = TextInput()
			welcomelabel = Label()'''
			#self.rows = 3
			#welcomelabel = Label(text='Bedouin Translater')
			#self.add_widget(welcomelabel)
			#translatebutton = Button(text='Translate')
			#self.add_widget(translatebutton)
			#funnybutton = Button(text='funny')
			#weirdbutton = Button(test='weird')
			#welcomelabel = Label()
				


class verbchartApp(App):

    def build(self):

        return VerbChartScreen()



if __name__ == '__main__':
    verbchartApp().run()
