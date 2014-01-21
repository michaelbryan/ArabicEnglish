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
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.texture import Texture

from bidi.algorithm import get_display
import arabic_reshaper
from functools import partial

#import sys
#sys.path.append('../')
from eadict2 import PopulateDB, search_entries

Builder.load_string("""
<RunSearchButton>:
    #run_search_button: runSearchButtonID
    #id: runSearchButtonID
    #size_hint: None, None
    #size_x: self.width-60
    size_y: 100
    on_release: root.RunSearchButton_pressed()

<EntryButton>:
    #size_hint: None, None
    #size_x: 60
    size_y: 100
    text: "Full Entry"
    on_release: root.EntryButton_pressed()

<VerbChartButton>:
    #size_hint: None, None
    #size_x: 60
    size_y: 100
    text: "Verb Chart"
    on_release: root.VerbChartButton_pressed()

<HomeScreen>:
    id: home_screen
    translateInput: translateInputID
    translateButton: translateButtonID
    translateLabel: labelID

    orientation: 'vertical'
    FloatLayout:
        size_hint: 1, .95
        TextInput:
            id: translateInputID
            text: 'cove'
            #text: 'ﻰﺸَﻣ'
            font_name: "data/fonts/DejaVuSans.ttf"
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
            text: 'Bedouin مُتَرْجِم'
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
    results_label: resultsLabelID
    #results_layout: resultsLayoutID
    #translationTextInput: translationID
    #result_button: resultButtonID
    scroll_view: scrollviewID
    #stack_layout: StackLayoutID
    anchor_layout_2: anchorLayout2
    
    #run_search_button: runSearchButtonID
    #entry_button: entryButtonID
    #verb_chart_button: verbChartButtonID

    AnchorLayout:
        size_hint: 1, .1   
        pos_hint: {'x': 0, 'y': .9}
        anchor_x: 'center'
        anchor_y: 'center'
        TextInput:
        	id: translateInput2KV
        	text: 'cover'
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
			Label:
                id: resultsLabelID
				text: "Results:"
				size_hint: None, None
	            height: 20
	            width: 100
	            font_size: 13
                halign: 'left'
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
        bar_width: '8dp'
        
        #BoxLayout:
            #id: resultsLayoutID
            #size_hint: 1, None
        #StackLayout:
            #id: StackLayoutID
            ######if I change the y size hint from None to 1, more buttons will be created, why?
            #size_hint: 1, None
            #orientation: 'lr-tb'
            #pos_hint: {'x': 0, 'y': 0}
            
            #RunSearchButton:
                #id: runSearchButtonID
            
            #EntryButton:
                #id: entryButtonID

            #VerbChartButton:
                #id: verbChartButtonID

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
 
    label_for_pos: label1ID
    label_for_english: label2ID
    label_for_arabic: label3ID
    label_for_plural: label4ID
    label_for_alt_plural: label5ID
    label_for_fem_sin: label6ID
    label_for_fem_plural: label7ID

    BoxLayout:
        id: boxlayout1ID
        orientation: 'horizontal'
        size_hint: 1, .05
        pos_hint: {'x': 0, 'y': .95}
        Label:
            id: label1ID
            size_hint: 1, 1
            pos_hint: {'x': 0, 'y': 0}
            text: 'entry.part_of_speech'
            text_size: self.size
            valign: 'middle'
            halign: 'left'
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, .25
        pos_hint: {'x': 0, 'y': .7}
        FloatLayout:
            id: floatlayout1ID
            pos_hint: {'x': 0, 'y': .5}
            Label:
                id: label2ID
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
                id: label3ID
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
                id: label4ID
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
                id: label5ID
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
                id: label6ID
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
                id: label7ID
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
<VerbChartScreen>:
    orientation: 'vertical'
    main_chart: mainChartID
    extras_box: extrasBoxID
    bottom_bar: bottomBarID
    big_box: bigBoxID
    done_button: doneButtonID
    chart_scroll: chartScrollID
    chart_label: chartLabelID
    BoxLayout:
        size_hint: 1, None
        height: 40
        pos: 0, root.bottom_bar.height + root.main_chart.height
        Label:
            id: chartLabelID
            font_name: "data/fonts/DejaVuSans.ttf"
            text: 'eng : arab word'
            halign: 'center'
            valign: 'middle'
    ScrollView:
        id: chartScrollID
        pos: 0, root.bottom_bar.height
        BoxLayout:
            id: bigBoxID
            size_hint: None, None
            height: root.main_chart.height
            width: root.main_chart.width + root.extras_box.width
            GridLayout:
                id: mainChartID
                size_hint: None, None
                pos_hint: {'x': 0, 'y': 0}
                cols: 6
                col_default_width: 100
                rows: 9
                row_force_default: True
                row_default_height: 40
                height: self.rows * self.row_default_height
                width: self.cols * self.col_default_width
                minimum_height: self.height
                minimum_width: self.width

            BoxLayout:
                id: extrasBoxID
                label_1: label1ID
                orientation: 'vertical'
                size_hint: None, None
                height: root.main_chart.height
                width: self.label_1.width
                #pos_hint: {'x': .75, 'y': 0}
                pos: root.main_chart.width, 0
                Label:
                    id: label1ID
                    font_name: "data/fonts/DejaVuSans.ttf"
                    #size_hint: 1, 1
                    #pos_hint: {'x': 0, 'y': 0}
                    text: 'ism faail: yadayada'
                    text_size: self.size
                    valign: 'middle'
                    halign: 'center'

    AnchorLayout:
        id: bottomBarID
        orientation: 'vertical'
        #pos_hint: {'x': 0, 'y': 0}
        pos: 0, 0
        size_hint: 1, None
        height: 40
        anchor_x: 'center'
        anchor_y: 'center'
        Button:
            id: doneButtonID
            text: 'Done'
            size_hint: None, None
            height: 20
            width: 40
            font_size: 10
            on_release: root.done_button_pressed()

""")

#class Dictionary:

def run_search(input_to_translate):
    search_result = search_entries(input_to_translate)
    print "search_result:", search_result

    results_list_tuples = []
    #found = False
    for tupleOfEntryAndBool in search_result:
        entry = tupleOfEntryAndBool[0]
        responseCode = tupleOfEntryAndBool[1]
        #print "entry:", entry
        #print "response code:", responseCode
        if responseCode == 0:
            results_list_tuples.append((entry.arabic, entry.retrieve_just_arabic(), entry))
            new_results_label = " Results:"
            sm.get_screen("results_screen").getArabicResults(results_list_tuples, new_results_label)
            sm.current = 'results_screen'
            #found = True
        elif responseCode == 1:
            results_list_tuples.append((entry.english, entry.retrieve_english(), entry))
            new_results_label = " Did you mean:"
            sm.get_screen("results_screen").getCloseEnglishResults(results_list_tuples, new_results_label)
            sm.current = 'results_screen'
        elif responseCode == 2:
            results_list_tuples.append((entry.english, entry.retrieve_english(), entry))
            new_results_label = " Results:"
            sm.get_screen("results_screen").getEnglishResults(results_list_tuples, new_results_label)
            sm.current = 'results_screen'
        elif responseCode == 3:
            real_entry = entry[0]
            word = entry[1]
            part_of_sp = real_entry.part_of_speech
            button_label = " " + part_of_sp + ": " + word
            results_list_tuples.append((word, button_label, real_entry))
            new_results_label = " Did you mean:"
            sm.get_screen("results_screen").getCloseArabicResults(results_list_tuples, new_results_label)
            sm.current = 'results_screen'
        else:
            results_list_tuples.append(("", "response code was 4", ""))
            sm.get_screen("results_screen").getResultsButtons(results_list_tuples)
            sm.current = 'results_screen'
    #num_results = len(results_list)

    #if found:

        #displayText = "".join(results_list)

    #results_scrollview = ResultsScreen.ScrollView()
    #PROVIDED_USER_INPUT = input_to_translate


class RunSearchButton(Button):
    #run_search_button = ObjectProperty(None)

    '''
    def __init__(self, word):
        self.input_to_translate = word

    
    def edit_button(self, button_label, word):
        self.run_search_button.text = button_label
    '''

    def RunSearchButton_pressed(self):
        run_search(self.input_to_translate)

class EntryButton(Button):

    def EntryButton_pressed(self, entry):
        sm.get_screen("entry_viewer").replace_labels(entry)
        sm.current = 'entry_viewer'

class VerbChartButton(Button):

    def VerbChartButton_pressed(self, entry):
        sm.get_screen("verb_chart").refresh_verb_chart(entry)
        sm.current = 'verb_chart'

class HomeScreen(Screen):
    translateInput = ObjectProperty(None)
    translateButton = ObjectProperty(None)
    translateLabel = ObjectProperty(None)

    def translateButtonPressed(self):
    	print "input to translate:", self.translateInput.text
        #new_label = unicode(self.translateLabel.text, encoding='utf-8')
    	#arabic_text = get_display(arabic_reshaper.reshape(new_label))#(u'العربية Hello World')).encode('utf-8')
    	#self.translateLabel.text = arabic_text

    	input_to_translate = self.translateInput.text
        run_search(input_to_translate)

        #sm.get_screen("results_screen").getGoHomeButton().text = self.translateInput.text

    def getInputText(self):
    	return self.translateInput.text

class ResultsScreen(Screen):
    translationTextInput = ObjectProperty(None)
    goHomeButton = ObjectProperty(None)
    result_button = ObjectProperty(None)
    scroll_view = ObjectProperty(None)
    translate_input_2 = ObjectProperty(None)
    results_label = ObjectProperty(None)
    #results_layout = ObjectProperty(None)
    anchor_layout_2 = ObjectProperty(None)
    #stack_layout = ObjectProperty(None)

    #run_search_button = ObjectProperty(None)
    #entry_button = ObjectProperty(None)
    #verb_chart_button = ObjectProperty(None)

    def getArabicResults(self, results_list, new_results_label):
        self.change_results_label(new_results_label)
        self.getResultsButtons(results_list)

    def getCloseEnglishResults(self, results_list, new_results_label):
        self.change_results_label(new_results_label)
        self.getCloseResultsButtons(results_list)

    def getEnglishResults(self, results_list, new_results_label):
        self.change_results_label(new_results_label)
        self.getResultsButtons(results_list)


    def getCloseArabicResults(self, results_list, new_results_label):
        self.change_results_label(new_results_label)
        self.getCloseResultsButtons(results_list)

    def goHome(self):
        sm.current = 'home'
        #self.goHomeButton.text = HomeScreen.translateInput.text

    #def getGoHomeButton(self):
        #return self.goHomeButton

    def translateButtonPressed(self):
        #scrollview1 = self.scroll_view
        #scrollview1.clear_widgets()
        input_to_translate_2 = self.translate_input_2.text
        return run_search(input_to_translate_2)

    
    def full_entry_button_pressed(self, entry):
        sm.get_screen("entry_viewer").replace_labels(entry)
        sm.current = 'entry_viewer'

    def verb_chart_button_pressed(self, entry):
        sm.get_screen("verb_chart").refresh_verb_chart(entry)
        sm.current = 'verb_chart'
    

    def getResultsButtons(self, results_list_tuples):
        layout1 = GridLayout(cols=2, spacing=0, size_hint=(1, None), \
            row_force_default=True, row_default_height=40)#, cols_minimum={0, 60})
        
        #layout1 = GridLayout(cols=2, spacing=0, size_hint=(1, None))
        #layout1 = StackLayout(orientation="lr-tb", spacing=0, size_hint=(1, None))
        #layout1 = self.stack_layout
        layout1.bind(minimum_height=layout1.setter('height'),
                     minimum_width=layout1.setter('width'))

        for result in results_list_tuples:
            word = result[0]
            button_label = result[1]
            entry = result[2]
            #print button_label

            reshaped_label = get_display(arabic_reshaper.reshape(button_label))#.decode('utf-8')
            print reshaped_label
            if entry.part_of_speech == "v":
                '''
                #RunSearchButton().text = button_label
                btn1 = RunSearchButton()
                #RunSearchButton.edit_button(RunSearchButton(word), button_label, word)
                btn2 = VerbChartButton()
                
                btn1 = Button(text=reshaped_label, size_hint=(1, None), font_name="data/fonts/DejaVuSans.ttf",
                         height=(30), size_x=(self.width-60))#, on_release=self.result_button_pressed_v(entry))
                btn2 = Button(text="Verb Chart", size_hint=(None, None),
                         height=(30), width=(100))#, on_release=self.result_button_pressed_v(entry))
                '''
                btn1 = Button(font_name="data/fonts/DejaVuSans.ttf", \
                    size_hint=(1, 1), valign='middle')#, width=300)
                         #, on_release=self.result_button_pressed_v(entry))
                #btn1.text_size = (btn1.width-20, layout1.row_default_height)
                btn1.text = reshaped_label

                btn2 = Button(text="Verb Chart", size_hint_x=None,
                         width=(70), font_size=12, \
                         valign ='middle')#, on_release=self.result_button_pressed_v(entry))
                btn2.text_size = (btn2.width-10, layout1.row_default_height)
                #text_size=(80, 40), 
                #btn1.bind(on_press=run_search(word))
                btn2.bind(on_press=self.verb_chart_button_pressed(entry))
                
                layout1.add_widget(btn2)
                layout1.add_widget(btn1)
            else:
                '''
                btn3 = RunSearchButton()
                btn4 = EntryButton()
                
                btn3 = Button(text=reshaped_label, size_hint=(1, None), font_name="data/fonts/DejaVuSans.ttf",
                         height=(30), size_x=(self.width-60))#, on_release=run_search(word))
                btn4 = Button(text="Full Entry", size_hint=(None, None),
                         height=(30), width=(100))#, on_release=self.result_button_pressed(entry))
                '''
                btn3 = Button(text=reshaped_label, font_name="data/fonts/DejaVuSans.ttf")
                         #, on_release=run_search(word))
                btn4 = Button(text="Full Entry", size_hint_x=None,
                         width=(70), font_size=12, \
                         valign ='middle')#, on_release=self.result_button_pressed_v(entry))
                btn4.text_size = (btn4.width-10, layout1.row_default_height)

                #btn3.bind(on_press=run_search(word))
                #btn4.bind(on_press=self.full_entry_button_pressed(entry))
                
                layout1.add_widget(btn4)
                layout1.add_widget(btn3)

        scrollview1 = self.scroll_view
        scrollview1.clear_widgets()
        scrollview1.add_widget(layout1)

    def getCloseResultsButtons(self, results_list):
        layout1 = GridLayout(cols=1, spacing=0, size_hint=(None, None), \
            row_force_default=False, row_default_height=40)#, cols_minimum={0, 60})

        layout1.bind(minimum_height=layout1.setter('height'),
                     minimum_width=layout1.setter('width'))

        layout1.clear_widgets()

        result_words = []
        for result in results_list:
            word = result[0]
            button_label = result[1]
            entry = result[2]

            if word in result_words:
                f=3
            else:
                result_words.append(word)
                reshaped_word = get_display(arabic_reshaper.reshape(word))

                btn = Button(text=reshaped_word, font_name="data/fonts/DejaVuSans.ttf", \
                    size_hint=(None, 1), halign='left', valign='middle', width=300)#, \
                    #on_press=partial(run_search, word))
                #btn.texture_size = (btn.width-20, 40)
                #btn.text_size = btn.size
                btn.text_size = (btn.width-20, btn.height)
                #btn.bind(on_press=run_search(word))
                #btn.bind(on_press=partial(run_search, word))
                layout1.add_widget(btn)

        scrollview1 = self.scroll_view
        scrollview1.clear_widgets()
        scrollview1.add_widget(layout1)

    def change_results_label(self, new_results_label):
        print "Current Page Label: ", self.results_label.text
        self.results_label.text = new_results_label


        '''
        layout_of_label = self.anchor_layout_2
        layout_of_label.clear_widgets()
        new_label = Label(text=str(new_results_label), size_hint=(None, None), height=20, width=100, font_size=13)
        layout_of_label.add_widget(new_label)
        '''

        #new_label = Label(text=new_results_label)

    def getTranslationTextInput(self):
        return self.translationTextInput

class EntryScreen(Screen):
    label_for_pos = ObjectProperty(None)
    label_for_english = ObjectProperty(None)
    label_for_arabic = ObjectProperty(None)
    label_for_plural = ObjectProperty(None)
    label_for_alt_plural = ObjectProperty(None)
    label_for_fem_sin = ObjectProperty(None)
    label_for_fem_plural = ObjectProperty(None)

    def replace_labels(self, entry):
        self.label_for_pos.text = " " + entry.part_of_speech
        self.label_for_english.text = entry.english
        self.label_for_arabic.text = entry.arabic
        self.label_for_plural.text = entry.plural
        self.label_for_alt_plural.text = entry.alt_plural
        self.label_for_fem_sin.text = entry.fem_sing
        self.label_for_fem_plural.text = entry.fem_plural

class VerbChartScreen(Screen):
    done_button = ObjectProperty(None)
    chart_label = ObjectProperty(None)
    main_chart = ObjectProperty(None)
    extras_box = ObjectProperty(None)

    def refresh_verb_chart(self, entry):
        verb = entry.arabic
        english = entry.english
        self.chart_label.text = english + " : " + verb
        chart_stuff_tuple = entry.some_verb_chart()
        all_conjugations = chart_stuff_tuple[0]
        chart_extras = chart_stuff_tuple[1]

        self.main_chart.clear_widgets()
        self.extras_box.clear_widgets()

        for conj in all_conjugations:
            reshaped_conj = get_display(arabic_reshaper.reshape(conj))
            print reshaped_conj
            lbl1 = Label(text=reshaped_conj, font_name="data/fonts/DejaVuSans.ttf")#, halign="center")
            self.main_chart.add_widget(lbl1)

        for info in chart_extras:
            reshaped_info = get_display(arabic_reshaper.reshape(info))
            print reshaped_info
            lbl2 = Label(text=reshaped_info, font_name="data/fonts/DejaVuSans.ttf")#, halign="right")
            self.extras_box.add_widget(lbl2)

    def done_button_pressed(self):
        sm.current = 'results_screen'


# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ResultsScreen(name='results_screen'))
sm.add_widget(EntryScreen(name='entry_viewer'))
sm.add_widget(VerbChartScreen(name='verb_chart'))

PROVIDED_USER_INPUT = ""

class TransApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    # populate our dictionary before we do anything...
    PopulateDB("indexforvocab.txt")
    TransApp().run()