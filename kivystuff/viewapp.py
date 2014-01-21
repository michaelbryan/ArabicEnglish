import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

import random


class ViewApp(App):

    def build(self):
        # create a default grid layout with custom width/height
        layout = GridLayout(cols=1, spacing=10, size_hint=(None, None),
                            width=Window.width)

        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required to
        # contain all the childs. (otherwise, we'll child outside the bounding
        # box of the childs)
        layout.bind(minimum_height=layout.setter('height'))

        # add button into that grid
        for i in range(30):
            btn = Button(text=str(i * random.random()) + '\n' + str(i * random.random()),
                         size=(300, 40),
                         size_hint=(None, None),
                         halign='left')
            #btn.text_size = (300, 40)
            btn.text_size = (btn.width, btn.height)
            #btn.bind(size=btn.setter('text_size'))
            #btn.bind(text_size=btn.setter('size'))
            layout.add_widget(btn)

        # create a scroll view, with a size < size of the grid
        root = ScrollView(size_hint=(None, None))
        root.size = (Window.width, Window.height)
        root.center = Window.center
        root.add_widget(layout)

        return root

if __name__ == '__main__':

    ViewApp().run()