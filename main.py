from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
#from kivy.graphics.vertex_instructions import Rectangle
#from kivy.graphics.context_instructions import Color

class PhotoGalleryApp(App):
    pass
class MouseTouch(Widget):
    def on_touch_down(self,touch):
        print("\nMouse Button Pressed")
        coords = touch.pos
        print("x coordinte: "+str(int(coords[0])))
    def on_touch_move(self,touch):
        print("\nMouse Moving")
        coords = touch.pos
        print("x coordinate: " + str())
    def on_touch_up(self,touch):

class Display(Screen):
    def display_image(self):
        return images[index]

    def advance(self):
        global index, image
        if index < len(images):
            index += 1
        else:
            index = 0




images = ["CheeseBlock.jpg","spork.jpg","SpongebobChair.jpg"]
index = 0

PhotoGalleryApp().run()
