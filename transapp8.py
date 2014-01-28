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
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.texture import Texture
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from bidi.algorithm import get_display
import arabic_reshaper
from functools import partial

#import sys
#sys.path.append('../')
from eadict2 import PopulateDB, search_entries

Builder.load_string("""
<CustomButton1>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    halign: 'left'
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton2>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton3>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton4>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton5>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton6>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton7>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton8>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton9>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton10>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton11>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton12>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton13>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton14>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton15>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton16>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton17>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton18>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton19>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"
<CustomButton20>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "data/fonts/DejaVuSans.ttf"

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

<MyPopup>:
    size_hint: .9, .9

<MyContentLayout>:
    orientation: 'vertical'
    content_lbl: contentID
    done_btn: doneButtonID
    ScrollView:
        GridLayout:
            cols: 1
            spacing: 10
            size_hint_y: None
            height: contentID.texture_size[1]

            Label:
                id: contentID
                text_size: self.width, None
                text: 'whatever whatever whatever whatever whatever '
                size_hint: 1, None
                size: self.parent.width, self.texture_size[1]
    AnchorLayout:
        size_hint: 1, None
        height: 20
        anchor_x: 'center'
        anchor_y: 'center'
        Button:
            id: doneButtonID
            text: 'Done'
            size_hint: None, None
            size: 50, 20
            on_release: root.parent.parent.parent.dismiss()

<MyScrollView>:
    GridLayout:
        cols: 1
        spacing: 10
        size_hint_y: None
        height: thetb.texture_size[1]

        Label:
            id: thetb
            text: 'whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever whatever '
            text_size: self.width, None
            size_hint: (1, None)
            size: self.parent.width, self.texture_size[1]


<CustomDropDown>:
    id: cdd
    Button:
        text: 'Features'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.FeaturesButtonPressed()
    Button:
        text: 'Suggestions'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.SuggestionsButtonPressed()
    Button:
        text: 'Abbreviations'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.AbbreviationsButtonPressed()
    Button:
        text: 'Miscellaneous'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.MiscellaneousButtonPressed()

<HomeScreen>:
    id: home_screen
    translateInput: translateInputID
    translateButton: translateButtonID
    translateLabel: labelID
    top_layout: topLayoutID
    #notes_dropdown: notesDropDownID
    dd_btn: btn_ddID

    orientation: 'vertical'
    BoxLayout:
        id: topLayoutID
        size_hint: 1, None
        height: 25
        pos: 0, root.height-self.height
        Button:
            id: btn_ddID
            size_hint: 1, None
            height: 25
            text: 'Usage Notes'
            font_size: 12
            on_release: root.drop_down.open(self)
        Button:
            text: 'About'
            size_hint: 1, None
            height: 25
            font_size: 12
            on_release: root.AboutButtonPressed()

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, None
        height: root.height-root.top_layout.height

        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            Label:
                id: labelID
                size_hint: .9, 1
                text: 'Jordanian Translator'
                text_size: self.size
                valign: 'middle'
                halign: 'center'
                font_size: 18
                font_name: "data/fonts/DejaVuSans.ttf"
                #font_name: "simpo.ttf"
                #font_name: "5thgradecursive.ttf"
                #font_name: "AGA-Rasheeq-Regular.ttf"

        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            TextInput:
                id: translateInputID
                text: 'cove'
                font_name: "data/fonts/DejaVuSans.ttf"
                background_color: 1, 1, 1, 1
                size_hint: .75, None
                height: 28
                font_size: 14
                multiline: False
                text_size: self.size

        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            Button:
                id: translateButtonID
                text: 'Translate'
                font_size: 12
                size_hint: None, None
                size: 65, 25
                valign: 'middle'
                halign: 'center'
                text_size: self.size
                on_release: root.translateButtonPressed()

<ResultsScreen>:
    orientation: 'vertical'
    goHomeButton: goHomeID
    translate_input_2: translateInput2KV
    results_label: resultsLabelID
    scroll_view: scrollviewID
    anchor_layout_2: anchorLayout2
    top_layout: topLayoutID
    trans_btn_l: transBtnLID
    bottom_lay: bottomLayID
    
    #run_search_button: runSearchButtonID
    #entry_button: entryButtonID
    #verb_chart_button: verbChartButtonID

    AnchorLayout:
        id: topLayoutID
        size_hint: 1, None
        height: 35
        pos: 0, root.height-self.height
        anchor_x: 'center'
        anchor_y: 'center'
        TextInput:
        	id: translateInput2KV
        	text: 'cover'
            background_color: 1, 1, 1, 1
            multiline: False
            size_hint: .85, None
            height: 28
            font_size: 14
            font_name: "data/fonts/DejaVuSans.ttf"

    AnchorLayout:
        id: transBtnLID
        size_hint: 1, None
        height: 25
        pos: 0, root.height-(self.height+root.top_layout.height)
        anchor_x: 'center'
        anchor_y: 'top'
        Button:
            id: translateButtonKV
            text: 'Translate'
            size_hint: None, None
            height: 20
            width: 60
            font_size: 10
            on_release: root.translateButtonPressed()
	AnchorLayout:
        id: anchorLayout2
		anchor_x: 'left'
        anchor_y: 'bottom'
        size_hint: 1, None
        height: 20
        pos: 0, root.height-(self.height+root.top_layout.height+root.trans_btn_l.height)
		Label:
            id: resultsLabelID
			text: "Results:"
			size_hint: None, None
            height: 20
            width: 100
            font_size: 13
            halign: 'left'
    ScrollView:
        id: scrollviewID
    	orientation: 'vertical'
    	pos: 0, 25
    	size_hint: 1, None
        height: root.height-(root.bottom_lay.height+root.anchor_layout_2.height+\
            root.trans_btn_l.height+root.top_layout.height)
        bar_width: '8dp'
        
	BoxLayout:
        id: bottomLayID
		orientation: 'horizontal'
		pos_hint: {'x': 0, 'y': 0}
	    size_hint: 1, None
        height: 25
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
 
    label_for_pos: label1ID
    label_for_english: label2ID
    label_for_arabic: label3ID
    label_for_plural: label4ID
    label_for_alt_plural: label5ID
    label_for_fem_sin: label6ID
    label_for_fem_plural: label7ID

    ScrollView:
        pos: 0, 40
        size_hint: 1, None
        height: root.height-40
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: 300, 400
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
                    font_name: "data/fonts/DejaVuSans.ttf"
                    valign: 'middle'
                    halign: 'left'
            BoxLayout:
                orientation: 'vertical'
                size_hint: 1, .25
                pos_hint: {'x': 0, 'y': .7}
                BoxLayout:
                    id: floatlayout1ID
                    pos_hint: {'x': 0, 'y': .5}
                    Label:
                        text: '>>'
                        size_hint: None, None
                        height: root.label_for_english.height
                        width: 20
                    Label:
                        id: label2ID
                        text_size: self.width-25, None
                        size_hint: 1, None
                        height: self.texture_size[1]
                        halign: 'center'
                        valign: 'top'
                        text: 'entry.english'
                        font_name: "data/fonts/DejaVuSans.ttf"
                    Label:
                        text: ""
                        size_hint: None, 1
                        width: 20
                BoxLayout:
                    id: floatlayout2ID
                    pos_hint: {'x': 0, 'y': 0}
                    Label:
                        text: ""
                        size_hint: None, 1
                        width: 20
                    Label:
                        id: label3ID
                        text: 'entry.arabic'
                        font_name: "data/fonts/DejaVuSans.ttf"
                    Label:
                        text: '<<'
                        size_hint: None, 1
                        width: 20
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
                            pos: self.center_x-50, self.center_y-4
                            size: 100, 1
                    Label:
                        id: label4ID
                        text: 'entry.plural'
                        font_name: "data/fonts/DejaVuSans.ttf"
                    Label:
                        text: 'PLURAL'
                        font_size: 12
                BoxLayout:
                    id: boxlayout3ID
                    orientation: 'vertical'
                    pos_hint: {'x': 0, 'y': .5}
                    canvas:
                        Rectangle:
                            pos: self.center_x-50, self.center_y-4
                            size: 100, 1
                    Label:
                        id: label5ID
                        pos_hint: {'x': 0, 'y': 0}
                        text: 'entry.alt_plural'
                        font_name: "data/fonts/DejaVuSans.ttf"
                    Label:
                        text: 'ALTERNATIVE PLURAL'
                        font_size: 12
                BoxLayout:
                    id: boxlayout4ID
                    orientation: 'vertical'
                    pos_hint: {'x': 0, 'y': .25}
                    canvas:
                        Rectangle:
                            pos: self.center_x-50, self.center_y-4
                            size: 100, 1
                    Label:
                        id: label6ID
                        pos_hint: {'x': 0, 'y': 0}
                        text: 'entry.fem_sing'
                        font_name: "data/fonts/DejaVuSans.ttf"
                    Label:
                        text: 'FEMININE SINGULAR'
                        font_size: 12
                BoxLayout:
                    id: boxlayout5ID
                    orientation: 'vertical'
                    pos_hint: {'x': 0, 'y': 0}
                    canvas:
                        Rectangle:
                            pos: self.center_x-50, self.center_y-4
                            size: 100, 1
                    Label:
                        id: label7ID
                        pos_hint: {'x': 0, 'y': 0}
                        text: 'entry.fem_plural'
                        font_name: "data/fonts/DejaVuSans.ttf"
                    Label:
                        text: 'FEMININE PLURAL'
                        font_size: 12
    AnchorLayout:
        id: bottomBarID
        #pos_hint: {'x': 0, 'y': 0}
        #pos: 0, 0
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
<VerbChartScreen>:
    orientation: 'vertical'
    main_chart: mainChartID
    extras_box: extrasBoxID
    bottom_bar: bottomBarID
    big_box: bigBoxID
    done_button: doneButtonID
    chart_scroll: chartScrollID
    chart_label: chartLabelID

    ScrollView:
        id: chartScrollID
        pos: 0, root.bottom_bar.height
        size_hint: 1, None
        height: root.height-40
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            width: root.big_box.width
            height: root.big_box.height+40
            BoxLayout:
                size_hint: 1, None
                height: 40
                #pos: 0, root.chart_scroll.height-40
                Label:
                    id: chartLabelID
                    font_name: "data/fonts/DejaVuSans.ttf"
                    text: 'eng : arab word'
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
        #pos_hint: {'x': 0, 'y': 0}
        #pos: 0, 0
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

def run_search(input_to_translate, *args):
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


class CustomButton1(Button):
    #run_search_button = ObjectProperty(None)

    '''
    def __init__(self, word):
        self.input_to_translate = word

    
    def edit_button(self, button_label, word):
        self.run_search_button.text = button_label
    '''

    def CustomButton_pressed(self, word):
        run_search(word)

class CustomButton2(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton3(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton4(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton5(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton6(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton7(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton8(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton9(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton10(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton11(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton12(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton13(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton14(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton15(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton16(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton17(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton18(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton19(Button):
    def CustomButton_pressed(self, word):
        run_search(word)
class CustomButton20(Button):
    def CustomButton_pressed(self, word):
        run_search(word)

class EntryButton(Button):

    def EntryButton_pressed(self, entry):
        sm.get_screen("entry_viewer").replace_labels(entry)
        sm.current = 'entry_viewer'

class VerbChartButton(Button):

    def VerbChartButton_pressed(self, entry):
        sm.get_screen("verb_chart").refresh_verb_chart(entry)
        sm.current = 'verb_chmyrt'

class MyContentLayout(BoxLayout):
    content_lbl = ObjectProperty(None)

    def change_content_text(self, new_text):
        self.content_lbl.text = new_text

class MyPopup(Popup):
    my_content = MyContentLayout()

    def close_pu(self):
        self.dismiss()
    
class MyScrollView(ScrollView):
    pass

class CustomDropDown(DropDown):
    my_content = MyContentLayout()
    my_popup = MyPopup()
    #home_screen = HomeScreen()
    
    def FeaturesButtonPressed(self):
        new_text = "These are the features."
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Features'
        pup.content = self.my_content
        pup.open()

    def SuggestionsButtonPressed(self):
        new_text = "These are the suggestions."
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Suggestions'
        pup.content = self.my_content
        pup.open()

    def AbbreviationsButtonPressed(self):
        new_text = "These are the abbreviations."
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Abbreviations'
        pup.content = self.my_content
        pup.open()
        
    def MiscellaneousButtonPressed(self):
        new_text = "These are the miscellaneous things."
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Miscellaneous'
        pup.content = self.my_content
        pup.open()
        
    #def open_dropdown(self):


        #foo = 3


class HomeScreen(Screen):
    translateInput = ObjectProperty(None)
    translateButton = ObjectProperty(None)
    translateLabel = ObjectProperty(None)
    top_layout = ObjectProperty(None)
    dd_btn = ObjectProperty(None)
    drop_down = CustomDropDown()
    #notes_dropdown = ObjectProperty(None)
    my_content = MyContentLayout()
    my_popup = MyPopup()

    def NotesButtonPressed(self):
        dd = self.drop_down
        dd.open
        
    def AboutButtonPressed(self):
        new_text = "This app was made blah blah "
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'About'
        pup.content = self.my_content
        pup.open()

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
    anchor_layout_2 = ObjectProperty(None)

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

    def translateButtonPressed(self):
        input_to_translate_2 = self.translate_input_2.text
        return run_search(input_to_translate_2)
    
    def full_entry_button_pressed(self, entry, *args):
        sm.get_screen("entry_viewer").replace_labels(entry)
        sm.current = 'entry_viewer'

    def verb_chart_button_pressed(self, entry, *args):
        sm.get_screen("verb_chart").refresh_verb_chart(entry)
        sm.current = 'verb_chart'
    

    def getResultsButtons(self, results_list_tuples):
        layout1 = GridLayout(cols=2, spacing=0, size_hint=(1, None), \
            row_force_default=False, row_default_height=25)#, cols_minimum={0, 60})

        layout1.bind(minimum_height=layout1.setter('height'),
                     minimum_width=layout1.setter('width'))
        #print results_list_tuples
        result_labels = []
        for result in results_list_tuples:
            word = result[0]
            button_label = result[1]
            entry = result[2]

            reshaped_label = get_display(arabic_reshaper.reshape(button_label))#.decode('utf-8')
            #print reshaped_label
            if entry.part_of_speech == "v":
               
                btn1 = Button(font_name="data/fonts/DejaVuSans.ttf", \
                    size_hint=(1, None), valign='middle', halign='left')#, \
                    #height=root.texture_size[1])#, text_size=(root.width-10, None))#, width=300)
                btn1.bind(on_release=partial(run_search, word))
                btn1.bind(size=btn1.setter('text_size'))
                #btn1.text_size = (btn1.parent.width-10, None)
                btn1.height = btn1.texture_size[1]
                btn1.text = reshaped_label

                btn2 = Button(text="Verb Chart", size_hint_x=None,
                         width=(70), font_size=12, \
                         valign ='middle')
                btn2.text_size = (btn2.width-10, layout1.row_default_height)
                #text_size=(80, 40), 
                btn2.bind(on_release=partial(self.verb_chart_button_pressed, entry))
                
                layout1.add_widget(btn2)
                layout1.add_widget(btn1)
            else:
                btn3 = Button(text=reshaped_label, size_hint=(1, None), \
                    font_name="data/fonts/DejaVuSans.ttf")
                btn3.bind(on_release=partial(run_search, word))
                btn3.bind(size=btn3.setter('text_size'))
                btn3.height = btn3.texture_size[1]
                #btn3.text_size = (btn3.parent.width-10, None)

                btn4 = Button(text="Full Entry", size_hint_x=None,
                         width=(70), font_size=12, \
                         valign ='middle')
                btn4.text_size = (btn4.width-10, layout1.row_default_height)
                btn4.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                layout1.add_widget(btn4)
                layout1.add_widget(btn3)

        scrollview1 = self.scroll_view
        scrollview1.clear_widgets()
        scrollview1.add_widget(layout1)

    def getCloseResultsButtons(self, results_list):
        layout1 = GridLayout(cols=1, spacing=0, size_hint=(1, None), \
            row_force_default=False, row_default_height=25)#, cols_minimum={0, 60})

        layout1.bind(minimum_height=layout1.setter('height'),
                     minimum_width=layout1.setter('width'))

        layout1.clear_widgets()

        result_words = []
        for result in results_list:
            word = result[0]
            button_label = result[1]
            entry = result[2]

            if word in result_words:
                f = 3
            else:
                if len(result_words) == 0:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton1()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 1:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton2()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 2:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton3()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 3:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton4()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 4:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton5()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 5:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton6()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 6:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton7()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 7:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton8()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 8:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton9()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 9:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton10()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 10:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton11()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 11:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton12()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 12:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton13()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 13:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton14()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 14:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton15()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 15:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton16()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 16:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton17()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 17:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton18()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 18:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton19()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 19:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))
                    btn = RunSearchButton20()
                    btn.bind(on_release=partial(run_search, word))
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                else:
                    f = 4
            '''
            else:
                if word in result_words:
                    f=3
                else:
                    result_words.append(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(word))

                    btn = self.run_search_button% % len(result_words)
                    btn.text = reshaped_word

                    
                    btn = Button(text=reshaped_word, font_name="data/fonts/DejaVuSans.ttf", \
                        size_hint=(None, 1), halign='left', valign='middle', width=300)#, \
                        #on_press=partial(run_search, word))
                    #btn.texture_size = (btn.width-20, 40)
                    #btn.text_size = btn.size
                    btn.text_size = (btn.width-20, btn.height)
                    #btn.bind(on_press=run_search(word))
                    #btn.bind(on_press=partial(run_search, word))
                    
                    layout1.add_widget(btn)
            '''

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
        
        reshaped_arabic1 = get_display(arabic_reshaper.reshape(entry.arabic))
        self.label_for_arabic.text = reshaped_arabic1
        
        reshaped_arabic2 = get_display(arabic_reshaper.reshape(entry.plural))
        self.label_for_plural.text = reshaped_arabic2
        
        reshaped_arabic3 = get_display(arabic_reshaper.reshape(entry.alt_plural))
        self.label_for_alt_plural.text = reshaped_arabic3
        
        reshaped_arabic4 = get_display(arabic_reshaper.reshape(entry.fem_sing))
        self.label_for_fem_sin.text = reshaped_arabic4
        
        reshaped_arabic5 = get_display(arabic_reshaper.reshape(entry.fem_plural))
        self.label_for_fem_plural.text = reshaped_arabic5

    def done_button_pressed(self):
        sm.current = 'results_screen'

class VerbChartScreen(Screen):
    done_button = ObjectProperty(None)
    chart_label = ObjectProperty(None)
    main_chart = ObjectProperty(None)
    extras_box = ObjectProperty(None)

    def refresh_verb_chart(self, entry, *args):
        verb = entry.arabic
        reshaped_verb = get_display(arabic_reshaper.reshape(verb))
        english = entry.english
        self.chart_label.text = english + " : " + reshaped_verb
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