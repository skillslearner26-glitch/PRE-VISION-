import os
import random
import webbrowser
import requests
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.network.urlrequest import UrlRequest

# 1. GRAPHICS FIX (Keep for PC, comment out for Phone)
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
os.environ['KIVY_GRAPHICS'] = 'gles'

# 2. FONT SETUP
# USE THIS LINE FOR PC:
# HINDI_FONT = "C:/Windows/Fonts/Nirmala.ttf"
# USE THIS LINE FOR PHONE (Colab):
HINDI_FONT = "Nirmala.ttf"

# 3. YOUR FIREBASE URL
FIREBASE_URL = "https://post-vision-default-rtdb.asia-southeast1.firebasedatabase.app/"

kv = """
WindowManager:
    Dashboard:
    Details:

<Dashboard>:
    name: "dash"
    canvas.before:
        Color:
            rgba: 0.05, 0.05, 0.05, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        padding: 0
        spacing: 15

        # --- HEADER ---
        BoxLayout:
            size_hint_y: 0.15
            padding: 10
            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.12, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 1, 0.8, 0, 0.5 
                Line:
                    points: [self.x, self.y, self.width, self.y]
                    width: 2

            Label:
                markup: True
                text: "[color=#ff3366]26[/color] [color=#ffd700]GURU[/color] [color=#33ccff]JODI[/color]"
                font_name: app.font_name
                font_size: 42
                bold: True
                outline_width: 3
                outline_color: 0, 0, 0, 1

        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: 20
                padding: 15

                GridLayout:
                    cols: 2
                    spacing: 15
                    size_hint_y: None
                    height: self.minimum_height
                    
                    # --- GAME BUTTONS ---

                    NeonButton:
                        text: "दिसावर"
                        sub_text: "786 SPECIAL\\n26 जोड़ी"
                        glow_color: (1, 0, 0.5, 1)
                        on_release: root.go_to_details("दिसावर")

                    NeonButton:
                        text: "फ़रीदाबाद"
                        sub_text: "SUPER LEAK\\n26 जोड़ी"
                        glow_color: (0, 1, 0, 1)
                        on_release: root.go_to_details("फ़रीदाबाद")

                    NeonButton:
                        text: "गाज़ियाबाद"
                        sub_text: "BLAST JODI\\n26 जोड़ी"
                        glow_color: (1, 0.8, 0, 1)
                        on_release: root.go_to_details("गाज़ियाबाद")

                    NeonButton:
                        text: "गली"
                        sub_text: "CONFIRM LEAK\\n26 जोड़ी"
                        glow_color: (0.5, 0, 1, 1)
                        on_release: root.go_to_details("गली")

                    NeonButton:
                        text: "दिल्ली बाज़ार"
                        sub_text: "VIP GAME\\n26 जोड़ी"
                        glow_color: (0, 1, 1, 1)
                        on_release: root.go_to_details("दिल्ली बाज़ार")

                    NeonButton:
                        text: "श्री गणेश"
                        sub_text: "TOP JODI\\n26 जोड़ी"
                        glow_color: (1, 0.5, 0, 1)
                        on_release: root.go_to_details("श्री गणेश")
                    
                    NeonButton:
                        text: "⭐ 5 स्टार रेटिंग दें"
                        sub_text: "और अपडेट चेक करें"
                        glow_color: (1, 1, 1, 1)
                        size_hint_x: 1
                        width: 500
                        on_release: root.open_link("https://play.google.com/store/apps")

                    # --- UPDATED TELEGRAM LINK HERE ---
                    NeonButton:
                        text: "🚀 टेलीग्राम चैनल"
                        sub_text: "सिंगल जोड़ी के लिए"
                        glow_color: (0, 0.5, 1, 1)
                        size_hint_x: 1
                        width: 500
                        on_release: root.open_link("https://t.me/GuruJodi26")

                Label:
                    text: "DISCLAIMER: Viewing This Application Is On Your Own Risk. All The information Shown On Application is Based on Numerology and Astrology for Information Purposes.. We Are Not Associated with Any Illegal Matka Business or Gamblers... We Warn You That Matka Gambling in Your Country May be Banned or Illegal... We Are Not Responsible For Any Issues or Scam.. We Respect All Country Rules/Laws.. If You Not Agree With Our Application Disclaimer... Please Quit Our Application Right Now. Copying/Promoting/Publishing Any of Our Content in Any Type Of Media or Other Source is prohibited."
                    font_size: 11
                    color: 0.6, 0.6, 0.6, 1
                    text_size: self.width, None
                    size_hint_y: None
                    height: self.texture_size[1] + 20
                    halign: 'center'

<NeonButton@ButtonBehavior+BoxLayout>:
    text: ""
    sub_text: ""
    glow_color: (1, 1, 1, 1)
    orientation: 'vertical'
    size_hint_y: None
    height: 140
    padding: 10
    canvas.before:
        Color:
            rgba: root.glow_color
        Line:
            width: 2
            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        Color:
            rgba: 0.1, 0.1, 0.1, 0.9
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
    
    Label:
        text: root.text
        font_name: app.font_name
        bold: True
        font_size: 24
        color: 1, 1, 1, 1
        size_hint_y: 0.5
    Label:
        text: root.sub_text
        font_name: app.font_name
        font_size: 15
        color: 1, 1, 0, 1
        size_hint_y: 0.5
        halign: 'center'

<Details>:
    name: "details"
    result_text: "प्रतीक्षा करें..."
    BoxLayout:
        orientation: "vertical"
        padding: 40
        spacing: 20
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        Label:
            text: root.country_name
            font_name: app.font_name
            font_size: 32
            color: 0, 1, 1, 1
            size_hint_y: 0.2
        
        Label:
            text: root.result_text
            font_size: 60
            bold: True
            color: 0, 1, 0, 1
            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.1, 1
                RoundedRectangle:
                    pos: self.x + 20, self.y
                    size: self.width - 40, self.height
                    radius: [20,]
        
        Button:
            text: "पीछे जाएं (BACK)"
            font_name: app.font_name
            size_hint_y: 0.15
            background_color: 1, 0, 0, 1
            on_release: root.manager.current = "dash"
"""

class Dashboard(Screen):
    def go_to_details(self, location):
        self.manager.current = "details"
        self.manager.get_screen("details").get_data(location)
    
    def open_link(self, url):
        webbrowser.open(url)

class Details(Screen):
    country_name = StringProperty("")
    result_text = StringProperty("...")
    
    db_keys = {
        "दिसावर": "DISAWAR",
        "फ़रीदाबाद": "FARIDABAD",
        "गाज़ियाबाद": "GAZIABAD",
        "गली": "GALI",
        "दिल्ली बाज़ार": "DELHI_BAZAAR",
        "श्री गणेश": "SHRI_GANESH"
    }

    # REPLACED "start_hacking_effect" WITH SIMPLE "get_data"
    def get_data(self, location):
        self.country_name = location
        self.result_text = "लोड हो रहा है..." # Shows "Loading..." immediately
        
        # Fetching from Firebase
        db_key = self.db_keys.get(location, "DISAWAR")
        UrlRequest(FIREBASE_URL + f"{db_key}.json", on_success=self.on_data_received, on_error=self.on_error)

    def on_data_received(self, req, result):
        if result:
            # SHOW RESULT INSTANTLY (No more looping)
            self.result_text = str(result).replace('"', '')
        else:
            self.result_text = "WAIT"

    def on_error(self, req, error):
        self.result_text = "No Net"

class WindowManager(ScreenManager):
    pass

class MyGuruApp(App):
    font_name = StringProperty(HINDI_FONT)
    def build(self):
        self.title = "26 GURU JODI"
        return Builder.load_string(kv)

if __name__ == "__main__":
    MyGuruApp().run()

