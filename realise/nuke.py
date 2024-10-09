from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from PyPDF2 import PdfReader
from kivy.uix.boxlayout import BoxLayout



class ReaderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        load_button = Button(text="Load PDF", size_hint=(1, 0.1))
        load_button.bind(on_press=self.load_pdf)
        self.layout.add_widget(load_button)

        self.scroll_view = ScrollView(size_hint=(1, 0.9))
        self.page_label = Label(text='Книга не завантажена', size_hint_y=None)

        self.scroll_view.add_widget(self.page_label)
        self.layout.add_widget(self.scroll_view)
        
        self.page_label.bind(texture_size=self.page_label.setter('size'))
        self.page_label.bind(width=self.update_text_size)

        nav_layout = BoxLayout(size_hint=(1, 0.1))

        self.prev_button = Button(text="Previous", disabled=True)
        self.prev_button.bind(on_press=self.prev_page)
        nav_layout.add_widget(self.prev_button)

        self.next_button = Button(text="Next", disabled=True)
        self.next_button.bind(on_press=self.next_page)
        nav_layout.add_widget(self.next_button)

        self.layout.add_widget(nav_layout)

        self.pdf_reader = None
        self.current_page = 0
        self.tottal_pages = 0
        return self.layout

    def load_pdf(self, instance):
        filechooser = FileChooserIconView(filters=["*.pdf"])
        popup = Popup(title="Select PDF", content=filechooser, size_hint=(0.9, 0.9))
        filechooser.bind(on_submit=lambda filechooser, selection, touch: self.load_selected_pdf(selection, popup))
        popup.open()
    
    def load_selected_pdf(self, selection, popup):
        if selection:
            pdf_path = selection[0]
            popup.dismiss()
            self.pdf_reader = PdfReader(pdf_path)
            self.tottal_pages = len(self.pdf_reader.pages)
            self.current_page = 0
            self.show_page(self.current_page)
            self.update_navigation_buttons()

    def show_page(self, page_number):
        if self.pdf_reader:
            page = self.pdf_reader.pages[page_number]
            text = page.extract_text()
            self.page_label.text = text

    def update_navigation_buttons(self):
        self.prev_button.disabled = self.current_page == 0 
        self.next_button.disabled = self.current_page == self.tottal_pages -1

    def next_page(self, instance):
        if self.current_page < self.tottal_pages -1:
            self.current_page += 1
            self.show_page(self.current_page)
            self.update_navigation_buttons()

    def prev_page(self,instance):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)
            self.update_navigation_buttons()

    def update_text_size(self, instance, value):
        instance.text_size = (value, None)


if __name__ == "__main__":
    ReaderApp().run()







app = ReaderApp()
app.run()