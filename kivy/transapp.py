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

Builder.load_string("""
<HomeScreen>:
    translateInput: translateInputID
    translateButton: translateButtonID

    orientation: 'vertical'
    FloatLayout:
        size_hint: 1, .95
        TextInput:
            id: translateInputID
            text: 'funny stuff'
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
            text: '*Bedouin مُخْتَبَر*'
            text_size: self.size
            valign: 'middle'
            halign: 'center'
            pos_hint: {'x': .3, 'y': .75}
            size_hint: .4, .2

    BoxLayout:
        size_hint: 1, .05
        pos_hint: {'x': 0, 'y': .95}
        Button:
            text: 'Usage Notes'
        Button:
            text: 'About'

<ResultsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'homescreen'
""")

class HomeScreen(Screen):
    translateInput = ObjectProperty(None)
    translateButton = ObjectProperty(None)

    def translateButtonPressed(self):
    	print "input to translate:", self.translateInput.text
    	sm.current = 'translation'

class ResultsScreen(Screen):
	pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ResultsScreen(name='translation'))

class TransApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TransApp().run()