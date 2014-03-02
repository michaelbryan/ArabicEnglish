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
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput, _textinput_list
import textinput
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
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton2>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton3>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton4>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton5>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton6>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton7>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton8>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton9>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton10>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton11>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton12>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton13>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton14>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton15>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton16>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton17>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton18>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton19>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton20>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton21>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton22>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton23>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton24>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton25>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton26>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton27>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton28>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton29>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'
<CustomButton30>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
    background_normal: 'tan2.png'
    background_down: 'tan1.png'

<CustomLabel1>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel2>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel3>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel4>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel5>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel6>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel7>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel8>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel9>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel10>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel11>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel12>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel13>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel14>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel15>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel16>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel17>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel18>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel19>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel20>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel21>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel22>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel23>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel24>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel25>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel26>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel27>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel28>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel29>:
    text_size: self.width-10, None
    size_hint: (1, None)
    height: self.texture_size[1]+8
    font_name: "DejaVuSans.ttf"
<CustomLabel30>:
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
        bar_width: '6dp'
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
        #color: .1686, .2745, .3372, 1 #Rainstorm
        background_normal: 'greenbutton2.png'
        background_down: 'greenbutton.png'
    Button:
        text: 'Suggestions'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.SuggestionsButtonPressed()
        #color: .1686, .2745, .3372, 1 #Rainstorm
        background_normal: 'greenbutton2.png'
        background_down: 'greenbutton.png'
    Button:
        text: 'Abbreviations'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.AbbreviationsButtonPressed()
        #color: .1686, .2745, .3372, 1 #Rainstorm
        background_normal: 'greenbutton2.png'
        background_down: 'greenbutton.png'
    Button:
        text: 'Miscellaneous'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.MiscellaneousButtonPressed()
        #color: .1686, .2745, .3372, 1 #Rainstorm
        background_normal: 'greenbutton2.png'
        background_down: 'greenbutton.png'

<CustomDropDown2>:
    Button:
        text: 'About Arabic'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.ArabicButtonPressed()
        #color: .1686, .2745, .3372, 1 #Rainstorm
        background_normal: 'greenbutton2.png'
        background_down: 'greenbutton.png'
    Button:
        text: 'Contact Info'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.ContactButtonPressed()
        #color: .1686, .2745, .3372, 1 #Rainstorm
        background_normal: 'greenbutton2.png'
        background_down: 'greenbutton.png'
    Button:
        text: 'App Info'
        font_size: 12
        size_hint_y: None
        height: 25
        on_release: root.AppInfoButtonPressed()
        #color: .1686, .2745, .3372, 1 #Rainstorm
        background_normal: 'greenbutton2.png'
        background_down: 'greenbutton.png'

<HomeScreen>:
    id: home_screen
    translateInput: translateInputID
    translateButton: translateButtonID
    translateLabel: labelID
    top_layout: topLayoutID
    dd_btn: btn_ddID

    orientation: 'vertical'
    canvas:
        Color:
            rgb: 0.73, 0.73, 0.73
        Rectangle:
            pos: self.pos
            size: self.size
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
            ##color: .1686, .2745, .3372, 1 #Rainstorm
            background_normal: 'greenbutton2.png'
            background_down: 'greenbutton.png'
            border: (16, 16, 16, 16)
            #background_color: .7451, .7333, .6666, 1
        Button:
            text: 'About'
            size_hint: 1, None
            height: 25
            font_size: 12
            on_release: root.drop_down2.open(self)
            ##color: .1686, .2745, .3372, 1 #Rainstorm
            background_normal: 'greenbutton2.png'
            background_down: 'greenbutton.png'
            border: (16, 16, 16, 16)

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
                color: 0, 0, 0, 1
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
                text: ''
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
                ##color: .1686, .2745, .3372, 1 #Rainstorm
                background_normal: 'greenbutton2.png'
                background_down: 'greenbutton.png'
                border: (16, 16, 16, 16)

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
    canvas:
        Color:
            rgb: 0.73, 0.73, 0.73
        Rectangle:
            pos: self.pos
            size: self.size
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
            background_normal: 'greenbutton2.png'
            background_down: 'greenbutton.png'
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
        bar_width: '6dp'
        
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
                background_normal: 'greenbutton2.png'
                background_down: 'greenbutton.png'
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
                background_normal: 'greenbutton2.png'
                background_down: 'greenbutton.png'
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
        bar_width: '6dp'
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
                        #text: '>>'
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
                        #text: '<<'
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
        bar_width: '6dp'
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
                    text: 'eng : arabic'
                    
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
    results_lbl_1 = " Results:"
    results_lbl_2 = " Did you mean:"
    #found = False
    for tupleOfEntryAndBool in search_result:
        the_entry = tupleOfEntryAndBool[0]
        responseCode = tupleOfEntryAndBool[1]
        #print "entry:", entry
        #print "response code:", responseCode
        if responseCode == 0:
            results_list_tuples.append((the_entry.arabic, the_entry.retrieve_just_arabic(), \
                the_entry, the_entry.english))
        elif responseCode == 1:
            results_list_tuples.append((the_entry.english, the_entry.retrieve_english(), \
                the_entry))
        elif responseCode == 2:
            real_entry = the_entry[0]
            word = the_entry[1]
            results_list_tuples.append((real_entry.english, real_entry.retrieve_english(), \
                real_entry, real_entry.arabic))
        elif responseCode == 3:
            real_entry = the_entry[0]
            word = the_entry[1]
            part_of_sp = real_entry.part_of_speech
            button_label = " " + part_of_sp + ": " + word
            results_list_tuples.append((word, button_label, real_entry))
            
    if search_result[0][1] == 0:
        sm.get_screen("results_screen").getArabicResults(results_list_tuples, results_lbl_1)
        sm.current = 'results_screen'
    elif search_result[0][1] == 1:
        sm.get_screen("results_screen").getCloseEnglishResults(results_list_tuples, results_lbl_2)
        sm.current = 'results_screen'
    elif search_result[0][1] == 2:
        sm.get_screen("results_screen").getEnglishResults(results_list_tuples, results_lbl_1)
        sm.current = 'results_screen'
    elif search_result[0][1] == 3:
        sm.get_screen("results_screen").getCloseArabicResults(results_list_tuples, results_lbl_2)
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
class CustomButton21(Button):
    pass
class CustomButton22(Button):
    pass
class CustomButton23(Button):
    pass
class CustomButton24(Button):
    pass
class CustomButton25(Button):
    pass
class CustomButton26(Button):
    pass
class CustomButton27(Button):
    pass
class CustomButton28(Button):
    pass
class CustomButton29(Button):
    pass
class CustomButton30(Button):
    pass

class CustomLabel1(Label):
    pass
class CustomLabel2(Label):
    pass
class CustomLabel3(Label):
    pass
class CustomLabel4(Label):
    pass
class CustomLabel5(Label):
    pass
class CustomLabel6(Label):
    pass
class CustomLabel7(Label):
    pass
class CustomLabel8(Label):
    pass
class CustomLabel9(Label):
    pass
class CustomLabel10(Label):
    pass
class CustomLabel11(Label):
    pass
class CustomLabel12(Label):
    pass
class CustomLabel13(Label):
    pass
class CustomLabel14(Label):
    pass
class CustomLabel15(Label):
    pass
class CustomLabel16(Label):
    pass
class CustomLabel17(Label):
    pass
class CustomLabel18(Label):
    pass
class CustomLabel19(Label):
    pass
class CustomLabel20(Label):
    pass
class CustomLabel21(Label):
    pass
class CustomLabel22(Label):
    pass
class CustomLabel23(Label):
    pass
class CustomLabel24(Label):
    pass
class CustomLabel25(Label):
    pass
class CustomLabel26(Label):
    pass
class CustomLabel27(Label):
    pass
class CustomLabel28(Label):
    pass
class CustomLabel29(Label):
    pass
class CustomLabel30(Label):
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
    '''
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        mytextinput = self.translateInput
        mytextinput.bind(text=self.on_text)

    def on_text(self, value, *args):
        n = 1
        k = 2
        n = n + 1
        #print('The widget', self, 'have:', value)
        text = value.text
        print text
        reshaped_text = get_display(arabic_reshaper.reshape(text))
        print reshaped_text
        mytextinput = self.translateInput
        #print _textinput_list
        #text_list = textinput._textinput_list
        #print text_list
        #if n % k == 0:
            ### evaluates true if and only if n is an exact \
            ### multiple of k. In elementary maths this is known \
            ### as the remainder from a division.
            #mytextinput._refresh_text(reshaped_text)
            #mytextinput.text = reshaped_text
    '''

    def translateButtonPressed(self):
    	input_to_translate = self.translateInput.text
        if len(input_to_translate) >= 1:
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
            font_size=10, text='More', background_normal='greenbutton2.png', \
            background_down='greenbutton.png')
        btn.bind(on_release=self.moreButton_pressed)
        self.more_btn_lay.add_widget(btn)
        alignment = 'left'
        self.change_results_label(new_results_label)
        self.getResultsButtons(results_list, alignment)

    def getCloseEnglishResults(self, results_list, new_results_label):
        alignment = 'left'
        self.change_results_label(new_results_label)
        self.getCloseResultsButtons(results_list, alignment)

    def getEnglishResults(self, results_list, new_results_label):
        btn = Button(size_hint=(None, None), height=20, width=40, \
            font_size=10, text='More', background_normal='greenbutton2.png', \
            background_down='greenbutton.png')
        btn.bind(on_release=self.moreButton_pressed)
        self.more_btn_lay.add_widget(btn)
        alignment = 'right'
        self.change_results_label(new_results_label)
        self.getResultsButtons(results_list, alignment)

    def getCloseArabicResults(self, results_list, new_results_label):
        alignment = 'right'
        self.change_results_label(new_results_label)
        self.getCloseResultsButtons(results_list, alignment)

    def translateButtonPressed(self):
        input_to_translate_2 = self.text_input_2.text
        if len(input_to_translate_2) >= 1:
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
        searches.append(search_term)
        #print search_term
        results = all_regex_searches(search_term)
        #print results
        results_separator(results)

    def goHome(self):
        sm.current = 'home'

    def getResultsButtons(self, results_list_tuples, alignment):
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
            matched_string = result[3]

            #if button_label in result_labels:
            #    f = 3
            #else:
            if len(result_labels) == 0:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton1()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                #btn.bind(halign=partial(get_alignment, alignment))

                lbl2 = Label(size_hint_x=None, width=70, text= "1.")
                lbl = CustomLabel1()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "2.")
                lbl = CustomLabel2()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "3.")
                lbl = CustomLabel3()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "4.")
                lbl = CustomLabel4()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "5.")
                lbl = CustomLabel5()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "6.")
                lbl = CustomLabel6()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "7.")
                lbl = CustomLabel7()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "8.")
                lbl = CustomLabel8()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "9.")
                lbl = CustomLabel9()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "10.")
                lbl = CustomLabel10()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "11.")
                lbl = CustomLabel11()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "12.")
                lbl = CustomLabel12()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "13.")
                lbl = CustomLabel13()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "14.")
                lbl = CustomLabel14()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "15.")
                lbl = CustomLabel15()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "16.")
                lbl = CustomLabel16()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "17.")
                lbl = CustomLabel17()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "18.")
                lbl = CustomLabel18()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "19.")
                lbl = CustomLabel19()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
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
                
                lbl2 = Label(size_hint_x=None, width=70, text= "20.")
                lbl = CustomLabel20()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 20:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton21()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "21.")
                lbl = CustomLabel21()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 21:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton22()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "22.")
                lbl = CustomLabel22()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 22:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton23()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "23.")
                lbl = CustomLabel23()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 23:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton24()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "24.")
                lbl = CustomLabel24()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 24:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton25()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "25.")
                lbl = CustomLabel25()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 25:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton26()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "26.")
                lbl = CustomLabel26()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 26:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton27()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "27.")
                lbl = CustomLabel27()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 27:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton28()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "28.")
                lbl = CustomLabel28()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 28:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton29()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "29.")
                lbl = CustomLabel29()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
            elif len(result_labels) == 29:
                result_labels.append(button_label)
                filtered_label = filter_main_diacritics(button_label)
                reshaped_label = get_display(arabic_reshaper.reshape(filtered_label))
                btn = CustomButton30()
                #btn.width = layout1.width
                btn.bind(on_release=partial(self.result_button_pressed, word))
                btn.text = reshaped_label
                
                lbl2 = Label(size_hint_x=None, width=70, text= "30.")
                lbl = CustomLabel30()
                filtered_lbl = filter_main_diacritics(matched_string)
                reshaped_lbl = get_display(arabic_reshaper.reshape(filtered_lbl))
                lbl.text = "  " + reshaped_lbl
                lbl.halign = alignment
                layout1.add_widget(lbl2)
                layout1.add_widget(lbl)
                
                if entry.part_of_speech == "v":
                    btn_v = Button(text="Verb Chart", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_v.text_size = (btn_v.width-10, layout1.row_default_height)
                    btn_v.bind(on_release=partial(self.verb_chart_button_pressed, entry))

                    layout1.add_widget(btn_v)
                else:
                    btn_e = Button(text="Full Entry", size_hint_x=None,
                             width=(70), font_size=12, \
                             valign ='middle', background_normal='tan2.png', \
                             background_down='tan1.png')
                    btn_e.text_size = (btn_e.width-10, layout1.row_default_height)
                    btn_e.bind(on_release=partial(self.full_entry_button_pressed, entry))
                
                    layout1.add_widget(btn_e)
                layout1.add_widget(btn)
                #else:
                    #f = 4

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
                elif len(result_words) == 20:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton21()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 21:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton22()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 22:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton23()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 23:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton24()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 24:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton25()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 25:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton26()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 26:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton27()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 27:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton28()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 28:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton29()
                    btn.bind(on_release=partial(self.result_button_pressed, word))
                    btn.halign = alignment
                    btn.text = reshaped_word
                    layout1.add_widget(btn)
                elif len(result_words) == 29:
                    result_words.append(word)
                    filtered_word = filter_main_diacritics(word)
                    reshaped_word = get_display(arabic_reshaper.reshape(filtered_word))
                    btn = CustomButton30()
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
        self.label_for_pos.text = " " + "Part of Speech: "+ entry.part_of_speech
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
    PopulateDB("jordict.txt")
    TransApp().run()