import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

i = range(20)

long_text = 'sometimes the search result could be rather long \
sometimes the search result could be rather long \
sometimes the search result could be rather long '

class ButtonILike(Button):
    
    def get_text(self):
        return long_text

class HomeScreen(Screen):
    scroll_view = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)
        layout1 = GridLayout(cols=1, spacing=0, size_hint=(1, None), \
            row_force_default=False, row_default_height=40)
        layout1.bind(minimum_height=layout1.setter('height'),
                     minimum_width=layout1.setter('width'))
        layout1.add_widget(ButtonILike())

        for result in i:

                def setting_function(instance, value):
                    btn2.text_size = (value-20, None)
                
                btn1 = Button(font_name="data/fonts/DejaVuSans.ttf", \
                    size_hint=(1, None), valign='middle',)#, \
                    #height=self.texture_size[1], text_size=(self.width-10, None))
                
                '''
                btn1.bind(size=btn1.setter('text_size'))
                btn1.bind(texture_size=btn1.setter('text_size'))
                #btn1.height = btn1.texture_size[1]
                texture_size_y = btn1.texture_size[1]
                #btn1.text_size[0] = btn1.width-10
                #btn1.texture_size[1] = btn1.text_size[1]
                #btn1.text_size[0] = btn1.setter('width')
                #btn1.bind(texture_size[1]=btn1.setter('height'))
                #btn1.text_size = (btn1.width-20, layout1.row_default_height)
                '''
                btn1.text = long_text

                btn2 = Button(font_name="data/fonts/DejaVuSans.ttf", \
                    size_hint=(1, None), valign='middle')
                btn2.bind(text_size=btn2.setter('size'))
                texture_size_y = btn2.texture_size[1]
                btn2.height = texture_size_y
                #btn2.bind(text_size=(btn2.width-20, None))
                btn2.text = 'or short'
                
                layout1.add_widget(btn1)
                layout1.add_widget(btn2)




        scrollview1 = self.scroll_view
        scrollview1.clear_widgets()
        scrollview1.add_widget(layout1)
    
    def setting_function(self, instance, value):
        btn2.text_size = (value-20, None)    

class mybuttonsApp(App):

    def build(self):

        return HomeScreen()



if __name__ == '__main__':
    mybuttonsApp().run()