from google.cloud.texttospeech_v1.types import SynthesisInput, VoiceSelectionParams, AudioConfig
from google.cloud.texttospeech_v1.gapic.enums import AudioEncoding
from google.cloud.texttospeech import TextToSpeechClient
import os
import env


class Synthesizer:

    def __init__(self, text, path):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/vladimir/Documents/LegionReddit/Legion-be765195b4f3.json'
        self.text = text
        self.path = env.AUDIO_PATH + path
        # Instantiates a client
        self.client = TextToSpeechClient()

        # Set the text input to be synthesized
        self.synthesis_input = SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        self.voice = VoiceSelectionParams(
            language_code='en-US',
            name='en-US-Wavenet-F'
        )

        # Select the type of audio file you want returned
        self.audio_config = AudioConfig(
            audio_encoding= AudioEncoding.LINEAR16)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type

    def create_voice(self):
        response = self.client.synthesize_speech(self.synthesis_input, self.voice, self.audio_config)

        # The response's audio_content is binary.
        with open(self.path, 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to ' + self.path)

    def play_voice(self):
        # output.save('test.mp3')
        print(self.path)
        os.system("afplay '" + self.path + "'")

