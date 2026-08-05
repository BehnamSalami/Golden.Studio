from kivy.uix.screenmanager import Screen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


from app.database import *
from app.python_runner import run_code


create_database()



class ProjectsScreen(Screen):


    def __init__(self,**kw):

        super().__init__(**kw)


        self.layout=MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )


        self.refresh()


        self.add_widget(self.layout)



    def refresh(self):

        self.layout.clear_widgets()


        title=MDLabel(
            text="📁 پروژه‌ها",
            halign="center"
        )

        self.layout.add_widget(title)



        for p in get_projects():

            btn=MDRaisedButton(
                text="📁 "+p[1]
            )


            btn.bind(
                on_press=lambda x,p=p:
                self.open_project(p[0])
            )


            self.layout.add_widget(btn)



        add=MDRaisedButton(
            text="+ پروژه جدید"
        )


        add.bind(
            on_press=lambda x:
            setattr(self.manager,"current","create")
        )


        self.layout.add_widget(add)



    def open_project(self,id):

        screen=self.manager.get_screen("detail")

        screen.project_id=id

        self.manager.current="detail"





class CreateProjectScreen(Screen):


    def __init__(self,**kw):

        super().__init__(**kw)


        layout=MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        self.name=MDTextField(
            hint_text="نام پروژه"
        )


        self.code=MDTextField(
            hint_text="کد پایتون تحلیل",
            multiline=True
        )


        save=MDRaisedButton(
            text="ساخت پروژه"
        )


        save.bind(
            on_press=self.save
        )


        layout.add_widget(self.name)
        layout.add_widget(self.code)
        layout.add_widget(save)


        self.add_widget(layout)



    def save(self,*args):

        create_project(
            self.name.text,
            self.code.text
        )


        self.manager.get_screen(
            "projects"
        ).refresh()


        self.manager.current="projects"





class ProjectDetailScreen(Screen):


    project_id=None



    def __init__(self,**kw):

        super().__init__(**kw)


        layout=MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        self.financial=MDTextField(
            hint_text="صورت مالی شرکت",
            multiline=True
        )


        self.result=MDLabel(
            text="نتیجه تحلیل"
        )


        run=MDRaisedButton(
            text="▶ اجرای تحلیل"
        )


        run.bind(
            on_press=self.execute
        )


        layout.add_widget(
            self.financial
        )


        layout.add_widget(run)

        layout.add_widget(
            self.result
        )


        self.add_widget(layout)




    def execute(self,*args):


        project=get_project(
            self.project_id
        )


        result=run_code(
            project[2],
            self.financial.text
        )


        self.result.text=result


        save_financial(
            self.project_id,
            self.financial.text,
            result
        )