from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from app.screens import HomeScreen, CreateProjectScreen


class GoldenStudioApp(MDApp):

    def build(self):

        self.title = "Golden Studio"

        self.theme_cls.primary_palette = "Blue"

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(
                name="home"
            )
        )

        manager.add_widget(
            CreateProjectScreen(
                name="create_project"
            )
        )

        manager.current = "home"

        return manager