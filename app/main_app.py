from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


from app.screens import (
    ProjectsScreen,
    CreateProjectScreen,
    ProjectDetailScreen
)


class GoldenStudioApp(MDApp):


    def build(self):

        self.title="Golden Studio"

        manager=ScreenManager()


        manager.add_widget(
            ProjectsScreen(
                name="projects"
            )
        )


        manager.add_widget(
            CreateProjectScreen(
                name="create"
            )
        )


        manager.add_widget(
            ProjectDetailScreen(
                name="detail"
            )
        )


        manager.current="projects"


        return manager