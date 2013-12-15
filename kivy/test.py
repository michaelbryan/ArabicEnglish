# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from bidi.algorithm import get_display
import arabic_reshaper

Builder.load_string(
'''
<TI>
    but: but
    Button:
        id: but
        font_name: 'data/fonts/DejaVuSans.ttf'
        font_size: '45dp'
	
''')

class TI(FloatLayout):
    def __init__(self, **kwargs):
        super(TI, self).__init__(**kwargs)
        self.but.text = get_display(arabic_reshaper.reshape(u'العربية Hello World'))
        '''
        fatha = "\xd9\x8e"
        damma = "\xd9\x8f"
        kasra = "\xd9\x90"
        shadda = "\xd9\x91"
        sukun = "\xd9\x92"
        maddah = "\xd9\x93"
        hamza_above = "\xd9\x94"
        hamza_below = "\xd9\x95"
        yah = "\xd9\x8a"
        waw = "\xd9\x88"
        alif = "\xd8\xa7"
        alif_hamza_above = "\xd8\xa3"
        alif_hamza_below = "\xd8\xa5"
        meem = "\xd9\x85"
        bah = "\xd8\xa8"
        tah = "\xd8\xaa"
        tah_marbuuta = "\xd8\xa9"
        noon = "\xd9\x86"
        hah = "\xd9\x87"
        kaaf = "\xd9\x83"
        hah_heavy = "\xd8\xad"

        #foo = 'لعربية'
        z = unicode("العربية", 'utf-8')
        self.but.text = get_display(arabic_reshaper.reshape(z))
        '''

class MyApp(App):

    def build(self):
        return TI()


if __name__ == '__main__':
    MyApp().run()
