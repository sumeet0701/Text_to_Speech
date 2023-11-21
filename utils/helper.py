from gtts import gTTS

class TextToSpeech:
    def __init__(self,text, filename):
        self.text = text
        self.filename = filename

    def convert(self):
        try:
            tts = gTTS(text= self.text, lang= 'en')
            tts.save(self.filename)
            return True
        except Exception as e:
            print("An Erro Occurreed: ", str(e))
    