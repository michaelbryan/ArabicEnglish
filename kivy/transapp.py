#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from bidi.algorithm import get_display
import arabic_reshaper

import sys
sys.path.append('../')
from eadict import PopulateDB, search_entries

Builder.load_string("""
<HomeScreen>:
    translateInput: translateInputID
    translateButton: translateButtonID
    translateLabel: labelID

    orientation: 'vertical'
    FloatLayout:
        size_hint: 1, .95
        TextInput:
            id: translateInputID
            text: 'walk'
            background_color: .8, .8, 0, 1
            size_hint: .75, .1
            multiline: True
            pos_hint: {'x': .125, 'y': .45}
            text_size: self.size
            valign: 'middle'
            halign: 'center'
            padding: 5
            
        Button:
            id: translateButtonID
            text: 'Translate'
            pos_hint: {'x': .35, 'y': .35}
            size_hint: .3, .08
            valign: 'middle'
            halign: 'center'
            text_size: self.size
            on_release: root.translateButtonPressed()
            #on_press: root.manager.current = 'resultsscreen'

        Label:
        	id: labelID
            text: 'Bedouin مُخْتَبَر'
            text_size: self.size
            valign: 'middle'
            halign: 'center'
            pos_hint: {'x': .3, 'y': .75}
            size_hint: .4, .2
            #font_name: "simpo.ttf"
            #font_name: "5thgradecursive.ttf"
            #font_name: "AGA-Rasheeq-Regular.ttf"
            font_name: "data/fonts/DejaVuSans.ttf"
            font_size: 50

    BoxLayout:
        size_hint: 1, .05
        pos_hint: {'x': 0, 'y': .95}
        Button:
            text: 'Usage Notes'
        Button:
            text: 'About'

<ResultsScreen>:
	goHomeButton: goHomeID
	translationTextInput: translationID

	orientation: 'vertical'
    AnchorLayout:
        size_hint: 1, .1   
        pos_hint: {'x': 0, 'y': .9}
        anchor_x: 'center'
        anchor_y: 'center'
        TextInput:
        	id: translateInputKV
        	text: 'Arabic or English'
            background_color: 1, 1, 1, 1
            multiline: True
            size_hint: .75, None
            height: 28
            font_size: 14
	BoxLayout:
		orientation: 'horizontal'
		size_hint: 1, .12   
	    pos_hint: {'x': 0, 'y': .78}
		AnchorLayout:
			anchor_x: 'left'
	        anchor_y: 'bottom'
			Label:
				text: 'Did you mean:'
				size_hint: None, None
	            height: 20
	            width: 100
	            font_size: 13
	    AnchorLayout:
	        anchor_x: 'center'
	        anchor_y: 'top'
	        Button:
	        	id: translateButtonKV
	        	text: 'Translate'
	            size_hint: None, None
	            height: 20
	            width: 70
	            font_size: 10
	            on_press: root.translateButtonPressed()
	    AnchorLayout:
	    	anchor_x: 'right'
	        anchor_y: 'bottom'
    ScrollView:
    	orientation: 'vertical'
    	pos_hint: {'x': 0, 'y': 0.1}
    	size_hint: 1, .68
        TextInput:
            id: translationID
            background_color: .8811, .8811, .8811, 1
            foreground_color: 0, 0, 0, 1
            font_name: 
            font_size: 14
            text: "The translation will be displayed here"
            size_hint: 1, 1
            height:
	BoxLayout:
		orientation: 'horizontal'
		pos_hint: {'x': 0, 'y': 0}
	    size_hint: 1, .1
	    AnchorLayout:
	    	anchor_x: 'left'
	        anchor_y: 'center'
	        Button:
	        	id: goHomeID
            	on_press: root.goHome()
	    		text: 'Back'
	            size_hint: None, None
	            height: 20
	            width: 40
	            font_size: 10
	    AnchorLayout:
	    	anchor_x: 'center'
	        anchor_y: 'center'
	        Button:
	    		text: 'More'
	            size_hint: None, None
	            height: 20
	            width: 40
	            font_size: 10
	    AnchorLayout:
	    	anchor_x: 'right'
	        anchor_y: 'center'
""")

class HomeScreen(Screen):
    translateInput = ObjectProperty(None)
    translateButton = ObjectProperty(None)
    translateLabel = ObjectProperty(None)

    def translateButtonPressed(self):
    	print "input to translate:", self.translateInput.text
    	arabic_text = get_display(arabic_reshaper.reshape(u'العربية Hello World')).encode('utf-8')
    	self.translateLabel.text = arabic_text

    	#sm.get_screen("translation").getGoHomeButton().text = self.translateInput.text
    	search_result = search_entries(self.translateInput.text)
    	print "search_result:", search_result

    	displayTextList = []
    	found = False
    	for tupleOfEntryAndBool in search_result:
    		entry = tupleOfEntryAndBool[0]
    		responseCode = tupleOfEntryAndBool[1]
    		print "entry:", entry
    		print "response code:", responseCode
    		if responseCode == 0:
    			displayTextList.append(entry.retrieve_arabic())
    			found = True
		else:
			displayText = "response code was not 0"

		if found:
			displayText = "\n".join(displayTextList)

    	sm.get_screen("translation").getTranslationTextInput().text = displayText
    	PROVIDED_USER_INPUT = self.translateInput.text
    	sm.current = 'translation'
    
    def getInputText(self):
    	return self.translateInput.text

class ResultsScreen(Screen):
	translationTextInput = ObjectProperty(None)
	goHomeButton = ObjectProperty(None)

	def goHome(self):
		sm.current = 'home'
		#self.goHomeButton.text = HomeScreen.translateInput.text

	def getGoHomeButton(self):
		return self.goHomeButton

	def getTranslationTextInput(self):
		return self.translationTextInput

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ResultsScreen(name='translation'))

PROVIDED_USER_INPUT = ""

class TransApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    # populate our dictionary before we do anything...
    PopulateDB("../indexforvocab.txt")
    TransApp().run()