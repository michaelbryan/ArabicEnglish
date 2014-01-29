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
from eadict2 import PopulateDB, search_entries, \
filter_main_diacritics, all_regex_searches

Builder.load_string("""
<CustomButton1>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton2>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton3>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton4>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton5>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton6>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton7>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton8>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton9>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton10>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton11>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton12>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton13>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton14>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton15>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton16>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton17>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton18>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton19>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomButton20>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"

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

<NotFoundLayout>:
    the_lbl: theLblID
    cols: 1
    spacing: 0
    size_hint_y: None
    height: theLblID.texture_size[1]

    Label:
        id: theLblID
        size_hint: (1, None)
        size: self.parent.width, self.texture_size[1]
        text: 'whatever whatever whatever whatever whatever whatever whatever whatever whatever '
        text_size: self.width, None
        halign: 'center'

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

<CustomDropDown2>:
    Button:
        text: 'About Arabic'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.ArabicButtonPressed()
    Button:
        text: 'Contact Info'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.ContactButtonPressed()
    Button:
        text: 'App Info'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.AppInfoButtonPressed()

<HomeScreen>:
    id: home_screen
    translateInput: translateInputID
    translateButton: translateButtonID
    translateLabel: labelID
    top_layout: topLayoutID
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
            on_release: root.drop_down2.open(self)

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
                font_name: "DejaVuSans.ttf"
                #font_name: "simpo.ttf"
                #font_name: "5thgradecursive.ttf"
                #font_name: "AGA-Rasheeq-Regular.ttf"

        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            TextInput:
                id: translateInputID
                text: 'cove'
                font_name: "DejaVuSans.ttf"
                background_color: 1, 1, 1, 1
                size_hint: .75, None
                height: 28
                font_size: 14
                multiline: False
                text_size: self.size
                on_text_validate: root.translateButtonPressed()

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
    text_input_2: textInput2ID
    results_label: resultsLabelID
    scroll_view: scrollviewID
    more_btn_lay: moreBtnLayID
    anchor_layout_2: anchorLayout2
    top_layout: topLayoutID
    trans_btn_l: transBtnLID
    bottom_lay: bottomLayID
    
    AnchorLayout:
        id: topLayoutID
        size_hint: 1, None
        height: 35
        pos: 0, root.height-self.height
        anchor_x: 'center'
        anchor_y: 'center'
        TextInput:
        	id: textInput2ID
        	text: 'cover'
            background_color: 1, 1, 1, 1
            multiline: False
            size_hint: .85, None
            height: 28
            font_size: 14
            font_name: "DejaVuSans.ttf"
            text_size: self.size
            on_text_validate: root.translateButtonPressed()

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
	        	#id: goBackID
            	on_release: root.goBack()
	    		text: 'Back'
	            size_hint: None, None
	            height: 20
	            width: 40
	            font_size: 10
	    AnchorLayout:
            id: moreBtnLayID
	    	anchor_x: 'center'
	        anchor_y: 'center'
	    AnchorLayout:
	    	anchor_x: 'right'
	        anchor_y: 'center'
            Button:
                text: 'Home'
                on_release: root.goHome()
                size_hint: None, None
                height: 20
                width: 40
                font_size: 10
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
        GridLayout:
            #orientation: 'vertical'
            cols: 1
            minimum_width: 200
            size_hint: None, None
            height: 400
            width: (label3ID.texture_size[0] / 2.2) + 200
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
                    font_name: "DejaVuSans.ttf"
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
                        font_name: "DejaVuSans.ttf"
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
                        font_name: "KacstOne.ttf"
                        font_size: 20
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
                        font_name: "KacstOne.ttf"
                        font_size: 20
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
                        font_name: "KacstOne.ttf"
                        font_size: 20
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
                        font_name: "KacstOne.ttf"
                        font_size: 20
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
                        font_name: "KacstOne.ttf"
                        font_size: 20
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
                    font_name: "DejaVuSans.ttf"
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
                        font_name: "DejaVuSans.ttf"
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

searches = []

def run_search(input_to_translate, *args):
    search_result = search_entries(input_to_translate)
    sm.get_screen("results_screen").update_TI(input_to_translate)
    #print "search_result:", search_result
    results_separator(search_result)

def results_separator(search_result):
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
            sm.get_screen("results_screen").run_not_found()
            sm.current = 'results_screen'

class CustomButton1(Button):
    pass
class CustomButton2(Button):
    pass
class CustomButton3(Button):
    pass
class CustomButton4(Button):
    pass
class CustomButton5(Button):
    pass
class CustomButton6(Button):
    pass
class CustomButton7(Button):
    pass
class CustomButton8(Button):
    pass
class CustomButton9(Button):
    pass
class CustomButton10(Button):
    pass
class CustomButton11(Button):
    pass
class CustomButton12(Button):
    pass
class CustomButton13(Button):
    pass
class CustomButton14(Button):
    pass
class CustomButton15(Button):
    pass
class CustomButton16(Button):
    pass
class CustomButton17(Button):
    pass
class CustomButton18(Button):
    pass
class CustomButton19(Button):
    pass
class CustomButton20(Button):
    pass

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

class NotFoundLayout(GridLayout):
    the_lbl = ObjectProperty(None)

    def change_lbl_text(self, new_text):
        self.the_lbl.text = new_text

class CustomDropDown(DropDown):
    my_content = MyContentLayout()
    my_popup = MyPopup()
    
    def FeaturesButtonPressed(self):
        file_object = open('features_content.txt', 'r')
        new_text = file_object.read()
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Features'
        pup.content = self.my_content
        pup.open()

    def SuggestionsButtonPressed(self):
        file_object = open('suggestions_content.txt', 'r')
        new_text = file_object.read()
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Suggestions'
        pup.content = self.my_content
        pup.open()

    def AbbreviationsButtonPressed(self):
        file_object = open('abbreviations_content.txt', 'r')
        new_text = file_object.read()
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Abbreviations'
        pup.content = self.my_content
        pup.open()
        
    def MiscellaneousButtonPressed(self):
        file_object = open('miscellaneous_content.txt', 'r')
        new_text = file_object.read()
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Miscellaneous'
        pup.content = self.my_content
        pup.open()

class CustomDropDown2(DropDown):
    my_content = MyContentLayout()
    my_popup = MyPopup()
    
    def ArabicButtonPressed(self):
        file_object = open('arabic_content.txt', 'r')
        new_text = file_object.read()
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'About Arabic'
        pup.content = self.my_content
        pup.open()

    def ContactButtonPressed(self):
        file_object = open('contact_content.txt', 'r')
        new_text = file_object.read()
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'Contact Info'
        pup.content = self.my_content
        pup.open()

    def AppInfoButtonPressed(self):
        file_object = open('appinfo_content.txt', 'r')
        new_text = file_object.read()
        self.my_content.change_content_text(new_text)
        pup = self.my_popup
        pup.title = 'App Info'
        pup.content = self.my_content
        pup.open()  

class HomeScreen(Screen):
    translateInput = ObjectProperty(None)
    translateButton = ObjectProperty(None)
    translateLabel = ObjectProperty(None)
    top_layout = ObjectProperty(None)
    dd_btn = ObjectProperty(None)
    drop_down = CustomDropDown()
    drop_down2 = CustomDropDown2()

    def translateButtonPressed(self):
    	input_to_translate = self.translateInput.text
        searches.append(input_to_translate)
        run_search(input_to_translate)

class ResultsScreen(Screen):
    scroll_view = ObjectProperty(None)
    text_input_2 = ObjectProperty(None)
    results_label = ObjectProperty(None)
    more_btn_lay = ObjectProperty(None)
    not_found_lay = NotFoundLayout()

    def run_not_found(self):
        new_results_label = ""
        self.change_results_label(new_results_label)

        new_text = "Word not found." + "\n" + \
        "Please see the suggestions under 'Usage Notes' on the home page."
        self.not_found_lay.change_lbl_text(new_text)
        scrollview1 = self.scroll_view
        scrollview1.clear_widgets()
        scrollview1.add_widget(self.not_found_lay)

    def change_results_label(self, new_results_label):
        #print "Current Page Label: ", self.results_label.text
        self.results_label.text = new_results_label

    def update_TI(self, input_to_translate):
        self.text_input_2.text = input_to_translate
        
    def getArabicResults(self, results_list, new_results_label):
        btn = Button(size_hint=(None, None), height=20, width=40, \
            font_size=10, text='More')
        btn.bind(on_release=self.moreButton_pressed)
        self.more_btn_lay.add_widget(btn)
        alignment = 'right'
        self.change_results_label(new_results_label)
        self.getResultsButtons(results_list)

    def getCloseEnglishResults(self, results_list, new_results_label):
        alignment = 'left'
        self.change_results_label(new_results_label)
        self.getCloseResultsButtons(results_list, alignment)

    def getEnglishResults(self, results_list, new_results_label):
        btn = Button(size_hint=(None, None), height=20, width=40, \
            font_size=10, text='More')
        btn.bind(on_release=self.moreButton_pressed)
        self.more_btn_lay.add_widget(btn)
        alignment = 'left'
        self.change_results_label(new_results_label)
        self.getResultsButtons(results_list)

    def getCloseArabicResults(self, results_list, new_results_label):
        alignment = 'right'
        self.change_results_label(new_results_label)
        self.getCloseResultsButtons(results_list, alignment)

    def translateButtonPressed(self):
        input_to_translate_2 = self.text_input_2.text
        searches.append(input_to_translate_2)
        return run_search(input_to_translate_2)
    
    def full_entry_button_pressed(self, entry, *args):
        sm.get_screen("entry_viewer").replace_labels(entry)
        sm.current = 'entry_viewer'

    def verb_chart_button_pressed(self, entry, *args):
        sm.get_screen("verb_chart").refresh_verb_chart(entry)
        sm.current = 'verb_chart'

    def result_button_pressed(self, word, *args):
        searches.append(word)
        run_search(word)

    def goBack(self):
        if len(searches) == 0:
            sm.current = 'home'
        else:
            if searches[-1] == self.text_input_2.text:
                del searches[-1]

            if len(searches) == 0:
                sm.current = 'home'
            else:
                new_search = searches[-1]
                #print new_search
                del searches[-1]
                #print searches
                run_search(new_search)

    def moreButton_pressed(self, *args):
        self.more_btn_lay.clear_widgets()
        search_term = self.text_input_2.text
        #print search_term
        results = all_regex_searches(search_term)
        #print results
        results_separator(results)

    def goHome(self):
        sm.current = 'home'

    def getResultsButtons(self, results_list_tuples):
        # I use repetitive custom buttons here, created in Kivy, 
        # because I cannot achieve the same behavior in Python.

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

            if button_label in result_labels:
                f = 3
            else:
                if len(result_labels) == 0:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton1()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    #btn.bind(halign=partial(get_alignment, alignment))
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 1:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton2()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 2:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton3()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 3:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton4()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 4:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton5()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 5:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton6()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 6:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton7()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 7:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton8()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 8:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton9()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 9:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton10()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 10:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton11()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 11:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton12()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 12:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton13()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 13:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton14()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 14:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton15()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 15:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton16()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 16:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton17()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 17:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton18()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 18:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton19()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                elif len(result_labels) == 19:
                    result_labels.append(button_label)
                    filtered_label = filter_main_diacritics(button_label)
                    reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                    btn = CustomButton20()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.text = reshaped_label
                    
                    if entry.part_of_speech == "v":
                        btn_v = Button(text="Verb Chart", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                        btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                        layout1.add_widget(btn_v)
                    else:
                        btn_e = Button(text="Full Entry", size_hint_x=None,
                                 width=(70), font_size=12, \
                                 valign ='middle')
                        btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                        btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                    
                        layout1.add_widget(btn_e)
                    layout1.add_widget(btn)
                else:
                    f = 4

        scrollview1 = self.scroll_view
        scrollview1.clear_widgets()
        scrollview1.add_widget(layout1)

    def getCloseResultsButtons(self, results_list, alignment):
        # I use repetitive custom buttons here, created in Kivy, 
        # because I cannot achieve the same behavior in Python.
        
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
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton1()
                    #btn.width = layout1.width
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 1:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton2()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 2:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton3()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 3:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton4()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 4:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton5()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 5:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton6()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 6:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton7()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 7:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton8()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 8:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton9()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 9:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton10()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 10:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton11()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 11:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton12()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 12:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton13()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 13:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton14()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 14:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton15()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 15:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton16()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 16:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton17()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 17:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton18()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 18:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton19()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 19:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton20()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
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

                    
                    btn = Button(text=reshaped_word, font_name="DejaVuSans.ttf", \
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
        titles = chart_stuff_tuple[0]
        all_conjugations = chart_stuff_tuple[1]
        chart_extras = chart_stuff_tuple[2]

        self.main_chart.clear_widgets()
        self.extras_box.clear_widgets()

        for title in titles:
            reshaped_title = get_display(arabic_reshaper.reshape(title))
            #print reshaped_title
            lbl1 = Label(text=reshaped_title, font_name="DejaVuSans.ttf", \
                font_size=14)
            self.main_chart.add_widget(lbl1)

        for conj in all_conjugations:
            reshaped_conj = get_display(arabic_reshaper.reshape(conj))
            #print reshaped_conj
            lbl1 = Label(text=reshaped_conj, font_name="KacstOne.ttf", \
                font_size=22)
            self.main_chart.add_widget(lbl1)

        for info in chart_extras:
            reshaped_info = get_display(arabic_reshaper.reshape(info))
            #print reshaped_info
            lbl2 = Label(text=reshaped_info, font_name="KacstOne.ttf", \
                font_size=22)
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