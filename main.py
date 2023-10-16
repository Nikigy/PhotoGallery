from kivy.app import App
from kivy.uix.screenmanager import Screen

class PhotoGalleryApp(App):
    pass

class PhotoGallery(Screen):
    images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']
    index = 0

    def display_image(self):
        return self.images[self.index]

    def next_image(self):
        if self.index < len(self.images) - 1:
            self.index += 1
            self.ids.index.text = str(self.index)
            self.ids.image.source = self.display_image()

    def previous_image(self):
        if self.index > 0:
            self.index -= 1
            self.ids.index.text = str(self.index)
            self.ids.image.source = self.display_image()

PhotoGalleryApp().run()