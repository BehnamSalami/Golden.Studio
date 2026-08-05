from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

from app.database import save_project, create_database



create_database()


class HomeScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )


        button = MDRaisedButton(
            text="ایجاد پروژه جدید"
        )


        button.bind(
            on_press=self.open_create
        )


        layout.add_widget(button)

        self.add_widget(layout)



    def open_create(self, *args):

        self.manager.current = "create"



class CreateProjectScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        self.name_input = MDTextField(
            hint_text="نام پروژه"
        )


        self.code_input = MDTextField(
            hint_text="دستورات پایتون پروژه",
            multiline=True
        )


        save = MDRaisedButton(
            text="ذخیره پروژه"
        )


        save.bind(
            on_press=self.save
        )


        layout.add_widget(self.name_input)
        layout.add_widget(self.code_input)
        layout.add_widget(save)


        self.add_widget(layout)



    def save(self, *args):

        save_project(
            self.name_input.text,
            self.code_input.text
        )

        self.manager.current = "home"