from openai import OpenAI


def transcribe_audio(audio_file_path):
    client = OpenAI(api_key='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')
    audio_file = open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_file.close()
    return transcription.text

def write_transcription_to_file(audio_file_path, output_file_path):
    transcription = transcribe_audio(audio_file_path)
    with open(output_file_path, "w") as output_file:
        output_file.write(transcription)
    return transcription

if __name__ == '__main__':
    print(write_transcription_to_file('output.mp3', 'transcription.txt'))  # Output: "Hello, how are you?"
