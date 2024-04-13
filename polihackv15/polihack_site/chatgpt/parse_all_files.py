import pdf_parser as pp
import speech_to_text.speech_to_text as stt
import speech_to_text.convert_to_mp3 as ctm


def parse_all_available_files(videos, pdfs, output_folder):
    materials_text = ""
    for pdf in pdfs:
        materials_text += pp.extract_text_from_pdf(pdf)
    for video in videos:
        materials_text += stt.write_transcription_to_file(video, f'{output_folder}')
    return materials_text


if __name__ == '__main__':
    videos = ['speech_to_text/input.mp4']
    pdfs = ['C6_slides_rom.pdf']
    output_folder = 'output'
    audios = []
    for video in videos:
        audio = video.replace(".mp4", ".mp3")
        ctm.convert_to_mp3(video, audio)
        audios.append(audio)
    print(parse_all_available_files(audios, pdfs, output_folder))
