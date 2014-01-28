import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial

i = ['some', 'words']

class HomeScreen(Screen):
    grid_l = ObjectProperty(None)
    top_lbl = ObjectProperty(None)

    def search_btn_pressed(self):
        grid = self.grid_l
        grid.bind(minimum_height=grid.setter('height'),
                     minimum_width=grid.setter('width'))

        for result in i:

                btn1 = Button(size_hint=(1, None))
                btn1.text = '%r' % result
                btn1.bind(on_release=partial(self.btn1_pressed, result))

                btn2 = Button(size_hint=(1, None))
                btn2.text = 'Remove result buttons'
                btn2.bind(on_release=self.btn2_pressed)

                grid.add_widget(btn1)
                grid.add_widget(btn2)

    def btn1_pressed(self, result, *args):
        new_text = result
        self.top_lbl.text = new_text

    def btn2_pressed(self, *args):
        self.grid_l.clear_widgets()
        #pass

class buttons_pressedApp(App):

    def build(self):

        return HomeScreen()

if __name__ == '__main__':
    buttons_pressedApp().run()