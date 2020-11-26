from googletrans import Translator
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
lang = "uk"

class my(GridLayout, Widget):
    def __init__ (self, **kwargs):
       super(my, self).__init__( **kwargs)
       self.cols = 1
       self.inside= GridLayout()
       self.inside.cols=2

       self.inside.add_widget(Label(text= "Text:"))
       self.Text_that_we_need_to_translate = TextInput(multiline=True)
       self.inside.add_widget(self.Text_that_we_need_to_translate)

       self.add_widget(self.inside)
       self.submit= Button(text="submit", font_size=40)
       self.submit.bind(on_press=self.press)
       self.inside.add_widget(self.submit)
       self.clear = Button(text= "clear")
       self.clear.bind(on_press= self.clear_all)
       self.inside.add_widget(self.clear)

    def popup(self, res):
        self.popup_ = Popup(title='Translation:', content=Label(
            text = str(res.text)), size=(100,150))
        print(res.text)
        self.popup_.open(res)

    def clear_all(self,some):
        self.Text_that_we_need_to_translate.text= ""
        self.user_text = ""

    def press(self, of):
        global res
        text_ = str(self.Text_that_we_need_to_translate.text)
        tr = Translator()
        res = tr.translate(text_, dest=lang)
        self.popup(res)

class MyApp(App):
    def build(self):
        return my()

if __name__== "__main__":
    MyApp().run()
