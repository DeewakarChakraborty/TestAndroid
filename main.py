
#Test

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.lang import Builder
from kivy.uix.image import AsyncImage

from plyer import filechooser
from kivy.properties import ListProperty
from kivy.uix.button import Button


class Main(Widget):

    selection = ListProperty([])

    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection
        #print(str(selection))


    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        self.b_t.ii = self.selection[0]
        self.box.ii = self.selection[0]

class RunApp(App):
    def build(self):
        game = Main()
        return game

if __name__ == '__main__':
    RunApp().run()