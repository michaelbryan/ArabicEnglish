import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class AppBase(Widget):

    def Launcher(self, launchapp):
        os.system(launchapp)

    def BuildLayout(self):
        layout = GridLayout( rows=4, row_force_default = True, row_default_height = 100, \
            col_force_default = True, col_default_width = 300 )
        with open('config.txt', 'rb') as f:
            reader = csv.reader(f, delimiter="|")
            for row in reader:
                launchbutton = Button( text = row[0], background_normal = 'tile.png')#, \
                    #on_press = self.Launcher(row[1]) )
                ##### ANSWER BELOW
                #launchbutton.bind( on_press = lambda Widget, appname=row[1]: self.Launcher( appname ) )
                ##### ANSWER ABOVE
                layout.add_widget(launchbutton)
        return layout


class MyApp(App):

    def build(self):
        Config.set('graphics', 'width', 1920)
        Config.set('graphics', 'height', 400)
        return AppBase().BuildLayout()

if __name__ == '__main__':
    MyApp().run()

##### THIS IS THE ANSWER:
##### launchbutton.bind( on_press = lambda widget, appname=row[1]: self.Launcher( appname ) )