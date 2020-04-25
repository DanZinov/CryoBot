import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser


class Main:
    def __init__(self):
        self.r = sr.Recognizer()

    def main(self):
        with sr.Microphone() as source:
            print("Ready!")
            self.r.pause_threshold = 1
            self.audio = self.r.listen(source)
            try:
                print("You said: " +
                      self.r.recognize_google(self.audio, language="ru-RU"))
                self.final_text = self.r.recognize_google(
                    self.audio, language="ru-RU")
                if(self.final_text in ["Hello", "Hey", "hey", "hello", "good morning", "Good Morning", "Good Day", "good day", "good evening", "good afternoon"]):
                    self.greet(self.final_text)
                elif(self.final_text in ["how are you", "how's it going", "how is it going", "what's up", "what is up", "how are you doing"]):
                    self.well_being(self.final_text)
                elif(self.final_text in ["what is the weather today", "weather", "weather today", "weather tommorow", "what is the weather tommorow"]):
                    self.weather(self.final_text)
                elif("plus" in self.final_text or "+" in self.final_text or "minus" in self.final_text or "-" in self.final_text
                     or "divided" in self.final_text or "/" in self.final_text or "*" in self.final_text or "times" in self.final_text or "multiplied by" in self.final_text):
                    self.calculate(self.final_text)
            except sr.UnknownValueError:
                print("Could not understand what you said :(")

    def calculator(self):
        pass

    def talk(self, final_text):
        myobj = gTTS(text=final_text, lang="en", slow=False)
        myobj.save("welcome.mp3")
        playsound("welcome.mp3")

    def weather(self, final_text):
        if(final_text in ["what is the weather today", "weather", "weather today"]):
            myobj = gTTS(text=final_text, lang="en", slow=False)
        if(final_text in ["weather tommorow", "what is the weather tommorow"]):
            myobj = gTTS(text=final_text, lang="en", slow=False)
        myobj.save("welcome.mp3")
        playsound("welcome.mp3")

    def website(self, final_text):
        myobj = gTTS(text=final_text, lang="en", slow=False)
        myobj.save("welcome.mp3")
        playsound("welcome.mp3")

    def well_being(self, final_text):
        myobj = gTTS(text="I am fine thank you, how are you?",
                     lang="en", slow=False)
        myobj.save("welcome.mp3")
        playsound("welcome.mp3")

    def greet(self, final_text):
        myobj = gTTS(text="Hey, how are you today?", lang="en", slow=False)
        myobj.save("welcome.mp3")
        playsound("welcome.mp3")

    def calculate(self, final_text):
        solution = ""
        myobj = gTTS(text=solution, lang="en", slow=False)
        myobj.save("welcome.mp3")
        playsound("welcome.mp3")

    def open_youtube(self):
        webbrowser.open_new("https://www.youtube.com")

    def open_google(self):
        webbrowser.open_new("https://www.google.com")

    def open_rbc(self):
        webbrowser.open_new(
            "https://www1.royalbank.com/cgi-bin/rbaccess/rbunxcgi?F6=1&F7=IB&F21=IB&F22=IB&REQUEST=ClientSignin&LANGUAGE=ENGLISH")


if __name__ == "__main__":
    Main().main()
