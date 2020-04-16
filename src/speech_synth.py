from google.cloud import texttospeech
import os


class Synthesizer:

    def __init__(self, text, path):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/vladimir/Documents/LegionReddit/Legion-be765195b4f3.json'
        self.text = text
        self.path = path
        # Instantiates a client
        self.client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        self.synthesis_input = texttospeech.types.SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            name='en-US-Wavenet-F',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE
        )

        # Select the type of audio file you want returned
        self.audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type

    def create_voice(self):
        response = self.client.synthesize_speech(self.synthesis_input, self.voice, self.audio_config)

        # The response's audio_content is binary.
        with open(self.path, 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "output.wav"')

    def play_voice(self):
        # output.save('test.mp3')
        os.system(self.path)
