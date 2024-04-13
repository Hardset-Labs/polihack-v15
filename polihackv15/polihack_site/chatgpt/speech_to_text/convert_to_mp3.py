import os
import moviepy.editor as mp


def convert_to_mp3(input_file, output_file):
    # Load the input file
    clip = mp.VideoFileClip(input_file)

    # Calculate target bitrate dynamically based on desired file size
    max_file_size_bytes = 25 * 1024 * 1024  # 25 MB in bytes
    target_bitrate = max_file_size_bytes / (clip.duration * 1024)  # in kbps

    # Convert to audio and write to output file
    clip.audio.write_audiofile(output_file, bitrate=str(target_bitrate) + 'k')

    # Close the clip
    clip.close()


def main(input_file, output_file):
    # Check if input file exists
    if not os.path.exists(input_file):
        print("Input file does not exist.")
        return

    # Convert input file to mp3
    try:
        convert_to_mp3(input_file, output_file)
        print("Conversion successful.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    input_file = input("input.mp4")
    output_file = input("output.mp3")
    main(input_file, output_file)
