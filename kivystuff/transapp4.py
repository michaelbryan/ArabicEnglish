#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pdb
import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from bidi.algorithm import get_display
import arabic_reshaper
#from functools import partial

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
            #text: 'مَشى'
            background_color: .8, .8, 0, 1
            size_hint: .75, .1
            multiline: False
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
    orientation: 'vertical'
    goHomeButton: goHomeID
    translate_input_2: translateInput2KV
    #results_label: resultsLabelID
    #translationTextInput: translationID
    #result_button: resultButtonID
    scroll_view: scrollviewID
    #stack_layout: StackLayoutID
    anchor_layout_2: anchorLayout2

    AnchorLayout:
        size_hint: 1, .1   
        pos_hint: {'x': 0, 'y': .9}
        anchor_x: 'center'
        anchor_y: 'center'
        TextInput:
        	id: translateInput2KV
        	text: 'happy'
            background_color: 1, 1, 1, 1
            multiline: False
            size_hint: .75, None
            height: 28
            font_size: 14
	BoxLayout:
		orientation: 'horizontal'
		size_hint: 1, .12   
	    pos_hint: {'x': 0, 'y': .78}
		AnchorLayout:
            id: anchorLayout2
			anchor_x: 'left'
	        anchor_y: 'bottom'
			#Label:
                #id: resultsLabelID
				#text: 'Results:'
				#size_hint: None, None
	            #height: 20
	            #width: 100
	            #font_size: 13
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
	            on_release: root.translateButtonPressed()
	    AnchorLayout:
	    	anchor_x: 'right'
	        anchor_y: 'bottom'
    ScrollView:
        id: scrollviewID
    	orientation: 'vertical'
    	pos_hint: {'x': 0, 'y': 0.1}
    	size_hint: 1, .68
        bar_width: '4dp'
        #StackLayout:
            #id: StackLayoutID
            ######if I change the y size hint from None to 1, more buttons will be created, why?
            #size_hint: 1, 1
            #orientation: 'tb-lr'
            #Button:
                #id: resultButtonID
                #size_hint: 1, None
                #text: 'result'

	BoxLayout:
		orientation: 'horizontal'
		pos_hint: {'x': 0, 'y': 0}
	    size_hint: 1, .1
	    AnchorLayout:
	    	anchor_x: 'left'
	        anchor_y: 'center'
	        Button:
	        	id: goHomeID
            	on_release: root.goHome()
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
<EntryScreen>:
    orientation: 'vertical'
    layout_for_pos: boxlayout1ID
    layout_for_english: floatlayout1ID
    layout_for_arabic: floatlayout2ID
    layout_for_plural: boxlayout2ID
    layout_for_alt_plural: boxlayout3ID
    layout_for_fem_sin: boxlayout4ID
    layout_for_fem_plural: boxlayout5ID

    BoxLayout:
        id: boxlayout1ID
        orientation: 'horizontal'
        size_hint: 1, .05
        pos_hint: {'x': 0, 'y': .95}
        Label:
            size_hint: 1, 1
            pos_hint: {'x': 0, 'y': 0}
            text: 'entry.part_of_speech'
            text_size: self.size
            valign: 'middle'
            halign: 'center'
        Label:
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, .25
        pos_hint: {'x': 0, 'y': .7}
        FloatLayout:
            id: floatlayout1ID
            pos_hint: {'x': 0, 'y': .5}
            Label:
                size_hint: 1, 1
                pos_hint: {'x': 0, 'y': 0}
                text: 'entry.english'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
            Label:
                size_hint: .2, 1
                pos_hint: {'x': .1, 'y': 0}
                text: '>>'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
        FloatLayout:
            id: floatlayout2ID
            pos_hint: {'x': 0, 'y': 0}
            Label:
                size_hint: 1, 1
                pos_hint: {'x': 0, 'y': 0}
                text: 'entry.arabic'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
            Label:
                size_hint: .2, 1
                pos_hint: {'x': .7, 'y': 0}
                text: '<<'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, .7
        pos_hint: {'x': 0, 'y': 0}
        BoxLayout:
            id: boxlayout2ID
            orientation: 'vertical'
            pos_hint: {'x': 0, 'y': .75}
            canvas:
                Rectangle:
                    pos: self.center_x-50, self.center_y-6
                    size: 100, 1
            Label:
                size_hint: 1, 1
                pos_hint: {'x': 0, 'y': 0}
                text: 'entry.plural'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
            Label:
                size_hint: 1, 1
                text: 'PLURAL'
                font_size: 12
        BoxLayout:
            id: boxlayout3ID
            orientation: 'vertical'
            pos_hint: {'x': 0, 'y': .5}
            canvas:
                Rectangle:
                    pos: self.center_x-50, self.center_y-6
                    size: 100, 1
            Label:
                size_hint: 1, 1
                pos_hint: {'x': 0, 'y': 0}
                text: 'entry.alt_plural'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
            Label:
                size_hint: 1, 1
                text: 'ALTERNATIVE PLURAL'
                font_size: 12
        BoxLayout:
            id: boxlayout4ID
            orientation: 'vertical'
            pos_hint: {'x': 0, 'y': .25}
            canvas:
                Rectangle:
                    pos: self.center_x-50, self.center_y-6
                    size: 100, 1
            Label:
                size_hint: 1, 1
                pos_hint: {'x': 0, 'y': 0}
                text: 'entry.fem_sing'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
            Label:
                size_hint: 1, 1
                text: 'FEMININE SINGULAR'
                font_size: 12
        BoxLayout:
            id: boxlayout5ID
            orientation: 'vertical'
            pos_hint: {'x': 0, 'y': 0}
            canvas:
                Rectangle:
                    pos: self.center_x-50, self.center_y-6
                    size: 100, 1
            Label:
                size_hint: 1, 1
                pos_hint: {'x': 0, 'y': 0}
                text: 'entry.fem_plural'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
            Label:
                size_hint: 1, 1
                text: 'FEMININE PLURAL'
                font_size: 12
""")

#class Dictionary:

def run_search(input_to_translate):
    search_result = search_entries(input_to_translate)
    print "search_result:", search_result

    results_list = []
    found = False
    for tupleOfEntryAndBool in search_result:
        entry = tupleOfEntryAndBool[0]
        responseCode = tupleOfEntryAndBool[1]
        print "entry:", entry
        print "response code:", responseCode
        if responseCode == 0:
            results_list.append((entry.retrieve_just_arabic(), entry))
            new_results_label = "Results:"
            ResultsScreen().change_results_label(new_results_label)
            found = True
        elif responseCode == 1:
            results_list.append((entry.retrieve_english(), entry))
            new_results_label = "Did you mean:"
            ResultsScreen().change_results_label(new_results_label)
        elif responseCode == 2:
            results_list.append((entry.retrieve_english(), entry))
            new_results_label = "Results:"
            ResultsScreen().change_results_label(new_results_label)
        elif responseCode == 3:
            entry = entry[0]
            word = entry[1]
            part_of_speech = entry.retrieve_pos
            button_label = " " + part_of_speech + " " + word
            results_list.append((button_label, entry))
            new_results_label = "Did you mean:"
            ResultsScreen().change_results_label(new_results_label)
        else:
            results_list.append("response code was 4")

    #num_results = len(results_list)

    #if found:

        #displayText = "".join(results_list)

    #results_scrollview = ResultsScreen.ScrollView()

    sm.get_screen("translation").getResultButton(results_list)#.text = displayText
    PROVIDED_USER_INPUT = input_to_translate
    sm.current = 'translation'

class HomeScreen(Screen):
    translateInput = ObjectProperty(None)
    translateButton = ObjectProperty(None)
    translateLabel = ObjectProperty(None)

    def translateButtonPressed(self):
    	print "input to translate:", self.translateInput.text
    	arabic_text = get_display(arabic_reshaper.reshape(u'العربية Hello World')).encode('utf-8')
    	self.translateLabel.text = arabic_text

    	input_to_translate = self.translateInput.text
        run_search(input_to_translate)

        #sm.get_screen("translation").getGoHomeButton().text = self.translateInput.text

    def getInputText(self):
    	return self.translateInput.text

class ResultsScreen(Screen):
    translationTextInput = ObjectProperty(None)
    goHomeButton = ObjectProperty(None)
    result_button = ObjectProperty(None)
    scroll_view = ObjectProperty(None)
    translate_input_2 = ObjectProperty(None)
    #results_label = ObjectProperty(None)
    anchor_layout_2 = ObjectProperty(None)
    #stack_layout = ObjectProperty(None)

    def goHome(self):
        sm.current = 'home'
        #self.goHomeButton.text = HomeScreen.translateInput.text

    def getGoHomeButton(self):
        return self.goHomeButton

    def translateButtonPressed(self):
        #scrollview1 = self.scroll_view
        #scrollview1.clear_widgets()
        input_to_translate_2 = self.translate_input_2.text
        return run_search(input_to_translate_2)

    def result_button_pressed(self, entry):
        sm.get_screen("entry_viewer").replace_labels(entry)
        sm.current = 'entry_viewer'


    def getResultButton(self, results_list):
        layout1 = GridLayout(cols=1, spacing=10, size_hint=(1, None))
        layout1.bind(minimum_height=layout1.setter('height'),
                     minimum_width=layout1.setter('width'))

        for result, entry in results_list:
            btn = Button(text=str(result), size_hint=(1, None),
                         size_y=(100), on_release=self.result_button_pressed(entry))
            layout1.add_widget(btn)
        scrollview1 = self.scroll_view
        scrollview1.clear_widgets()
        scrollview1.add_widget(layout1)

    def change_results_label(self, new_results_label):
        layout_of_label = self.anchor_layout_2
        layout_of_label.clear_widgets()
        new_label = Label(text=str(new_results_label), size_hint=(None, None), height=20, width=100, font_size=13)
        layout_of_label.add_widget(new_label)

        #new_label = Label(text=new_results_label)

    def getTranslationTextInput(self):
        return self.translationTextInput

class EntryScreen(Screen):
    layout_for_pos = ObjectProperty(None)
    layout_for_english = ObjectProperty(None)
    layout_for_arabic = ObjectProperty(None)
    layout_for_plural = ObjectProperty(None)
    layout_for_alt_plural = ObjectProperty(None)
    layout_for_fem_sin = ObjectProperty(None)
    layout_for_fem_plural = ObjectProperty(None)

    def replace_labels(self, entry):
        pos_layout = self.layout_for_pos



# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ResultsScreen(name='translation'))
sm.add_widget(EntryScreen(name='entry_viewer'))

PROVIDED_USER_INPUT = ""

class TransApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    # populate our dictionary before we do anything...
    PopulateDB("../indexforvocab.txt")
    TransApp().run()