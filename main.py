import whisper
import pypinyin
import argparse
import tqdm
import os

parser = argparse.ArgumentParser(description="Convert audio files to .lab files with pinyin using whisper")
parser.add_argument("-m", "--model", type=str, choices=["tiny", "base", "small", "medium", "large"], default="base", help="The model of whisper")
parser.add_argument("-d", "--directory", type=str, required=True, help="The directory of audio files")
parser.add_argument("-l", "--language", type=str, choices=["English", "Chinese", "Spanish", "French", "German", "auto"], default="auto", help="The language of whisper")
args = parser.parse_args()

model = whisper.load_model(args.model)
model.language = args.language

input_dir = args.directory
output_dir = args.directory

audio_files = [f for f in os.listdir(input_dir) if f.endswith(".mp3") or f.endswith(".wav")]

for audio_file in tqdm.tqdm(audio_files, desc="Processing audio files"):
    audio_path = input_dir + "/" + audio_file
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)
    result = whisper.transcribe(model, audio)
    text = result["text"]
    pinyin = " ".join(pypinyin.lazy_pinyin(text, errors='ignore'))
    output_path = output_dir + "/" + audio_file[:-4] + ".lab"
    if os.path.exists(output_path):
        os.remove(output_path)
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(pinyin)

print("\nInference completed")