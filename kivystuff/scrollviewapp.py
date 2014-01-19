from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ScrollViewApp(App):

    def build(self):
        layout1 = GridLayout(cols=1, spacing=10, size_hint=(1, None))
        layout1.bind(minimum_height=layout1.setter('height'),
                     minimum_width=layout1.setter('width'))
        for i in range(40):
            btn = Button(text=str(i), size_hint=(1, None),
                         height=(110))
            layout1.add_widget(btn)
        scrollview1 = ScrollView(bar_width='2dp')
        scrollview1.add_widget(layout1)

        layout2 = GridLayout(cols=4, spacing=10, size_hint=(None, None))
        layout2.bind(minimum_height=layout2.setter('height'),
                     minimum_width=layout2.setter('width'))
        for i in range(40):
            btn = Button(text=str(i), size_hint=(None, None),
                         size=(200, 100))
            layout2.add_widget(btn)
        scrollview2 = ScrollView(scroll_type=['bars'],
                                 bar_width='9dp',
                                 scroll_wheel_distance=100)
        scrollview2.add_widget(layout2)

        root = GridLayout(cols=2)
        root.add_widget(scrollview1)
        root.add_widget(scrollview2)
        return root

ScrollViewApp().run()