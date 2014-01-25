# -*- coding: utf-8 -*- 

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from bidi.algorithm import get_display
import arabic_reshaper

arabic_word_with_diacritics = u'\u0648\u064e\u0642\u0651\u064e\u0641'
arabic_word_without_diacritics = u'\u0648\u0642\u0641'

reshaped_with_diacritics = get_display(arabic_reshaper.reshape(arabic_word_with_diacritics))
reshaped_without_diacritics = get_display(arabic_reshaper.reshape(arabic_word_without_diacritics))

class Arabic_DisplayApp(App):
    def build(self):
    	bl = BoxLayout(orientation='vertical')
    	btn1 = Button(text=arabic_word_with_diacritics, font_size=30, \
    		font_name='DejaVuSans.ttf')
    	btn2 = Button(text=arabic_word_with_diacritics, font_size=30, \
    		font_name='DejaVuSans.ttf', text_size=(600, None))
    	btn3 = Button(text=arabic_word_without_diacritics, font_size=30, \
    		font_name='DejaVuSans.ttf', text_size=(600, None))
    	btn4 = Button(text=reshaped_with_diacritics, font_size=30, \
    		font_name='DejaVuSans.ttf')
    	btn5 = Button(text=reshaped_with_diacritics, font_size=30, \
    		font_name='DejaVuSans.ttf', text_size=(600, None))
    	btn6 = Button(text=reshaped_without_diacritics, font_size=30, \
    		font_name='DejaVuSans.ttf', text_size=(600, None))

    	bl.add_widget(btn1)
    	bl.add_widget(btn2)
    	bl.add_widget(btn3)
    	bl.add_widget(btn4)
    	bl.add_widget(btn5)
    	bl.add_widget(btn6)
        return bl

if __name__ == '__main__':
    Arabic_DisplayApp().run()