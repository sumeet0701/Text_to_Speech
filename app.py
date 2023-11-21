import gradio as gr
from utils.helper import TextToSpeech

def convert_text_to_speech(text):
    audio_filename = "Output.mp3"
    text_to_speech = TextToSpeech(text=text, filename= audio_filename)

    if text_to_speech.convert():
        return "Text is converted to Speech Sucessfully"
    else:
        return "An Error Occured During conversion"
    
iface = gr.Interface(
    fn = convert_text_to_speech,
    inputs ="text",
    outputs = 'text',
)
iface.launch()
