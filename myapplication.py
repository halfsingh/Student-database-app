import pandas as pd
from typing import Text
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from matplotlib.pyplot import text
from pyrsistent import s
from kivy.uix.button import Button


class mygrid(GridLayout):

    def __init__(self, **kwargs):
        self.df1 = []
        super(mygrid, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Student Name:"))

        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks:"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender:"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.storebutton = Button(text="Store in df")
        self.storebutton.bind(on_press=self.store)
        self.add_widget(self.storebutton)

        self.exportbutton = Button(text="Export in excel")
        self.exportbutton.bind(on_press=self.export)
        self.add_widget(self.exportbutton)

    def store(self, instance):
        temp = [self.s_name.text, self.s_marks.text, self.s_gender.text]
        self.df1.append(temp)

    def export(self, instance):
        df2 = pd.DataFrame(self.df1)
        df2.to_excel("output.xlsx")


class myapp(App):

    def build(self):
        return mygrid()
