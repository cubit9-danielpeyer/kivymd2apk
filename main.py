from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

    def build(self):
        self.title = 'Sample Apk'


MainApp().run()
