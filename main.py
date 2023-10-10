from kivy.app import App
from kivy.app import Screen


class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self):
        return images[index]

    def advance(self):
        global index, image
        if index < len(images):
            index += 1
        else:
            index = 0




images = ["LoafofBread.jfif","Spork.jpg","SpongebobChair.jpg"]
index = 0

PhotoGalleryApp().run()
