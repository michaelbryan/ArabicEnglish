from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2
		
		self.add_widget(Label(text='User Name'))
		self.username = TextInput(text='Hello world', multiline=False)
		print "textinput options:", dir(self.username)
		self.add_widget(self.username)
		
		self.add_widget(Label(text='password'))
		self.password = TextInput(text='Hello world', password=True, multiline=False)
		self.add_widget(self.password)
		
		clickMeButton = Button(text='ClickMe')
		self.add_widget(clickMeButton)
		clickMeButton.bind(on_press=self.clickMeButtonMethod)

	def clickMeButtonMethod(self, instance):
		print("The button was pressed: %s" % instance.text)
		print("The button was pressed: %s" % dir(instance))
		print("username: %s" % dir(self.username))
		print("username: %s" % self.username.text)
		self.username.insert_text("Cups")
		self.username.text = "midnight is past"

class ClarkApp(App):
	def build(self):
		return LoginScreen()

if __name__ == '__main__':
	ClarkApp().run()