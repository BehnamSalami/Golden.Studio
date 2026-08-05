from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

from kivymd.uix.textfield import MDTextField

from app.database import save_project, create_database


# ایجاد دیتابیس در شروع برنامه
create_database()


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        title = MDLabel(
            text="Golden Studio\n\nپروژه‌ها",
            halign="center"
        )

        create_button = MDRaisedButton(
            text="ایجاد پروژه جدید",
            pos_hint={"center_x": 0.5}
        )

        create_button.bind(
            on_press=self.open_create_project
        )

        layout.add_widget(title)
        layout.add_widget(create_button)

        self.add_widget(layout)


    def open_create_project(self, *args):

        self.manager.current = "create_project"



class CreateProjectScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        title = MDLabel(
            text="ایجاد پروژه جدید",
            halign="center"
        )


        self.project_name = MDTextField(
            hint_text="نام پروژه"
        )


        self.python_code = MDTextField(
            hint_text="دستورات پایتون پروژه",
            multiline=True
        )


        save_button = MDRaisedButton(
            text="ذخیره پروژه",
            pos_hint={"center_x": 0.5}
        )


        save_button.bind(
            on_press=self.save
        )


        layout.add_widget(title)
        layout.add_widget(self.project_name)
        layout.add_widget(self.python_code)
        layout.add_widget(save_button)


        self.add_widget(layout)


    def save(self, *args):

        save_project(
            self.project_name.text,
            self.python_code.text
        )

        self.project_name.text = ""
        self.python_code.text = ""

        self.manager.current = "home"