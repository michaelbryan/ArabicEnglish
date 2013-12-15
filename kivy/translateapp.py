import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, ObjectProperty

import sys
sys.path.append('../')
from eadict import PopulateDB, search_entries

class TranslateScreen(BoxLayout):
	translateInputCode = ObjectProperty(None)
	translateButtonCode = ObjectProperty(None)
	translationCode = ObjectProperty(None)
	outputText = ""

	def translateButtonPressed(self, inputProvided, translationObject):
		#print("The button was pressed: %s" % inputProvided.text)
		search_result = search_entries(inputProvided.text)
		translationObject.text = "Hey yo! ... returned: %s" % search_result

class TranslateApp(App):
    def build(self):
        return TranslateScreen()

if __name__ == '__main__':
    PopulateDB("../indexforvocab.txt")
    TranslateApp().run()