import whisper
import argparse
import tqdm
import os
from lang.cn import cn_output
from lang.en import en_output
from lang.jp import jp_output

parser = argparse.ArgumentParser(description="Convert audio files to .lab files with pinyin using whisper")
parser.add_argument("-m", "--model", type=str, choices=["tiny", "base", "small", "medium", "large"], default="base", help="The model of whisper")
parser.add_argument("-d", "--directory", type=str, required=True, help="The directory of audio files")
parser.add_argument("-l", "--language", type=str, choices=["English", "Chinese", "Japanese"], default="Chinese", help="The language of whisper")
args = parser.parse_args()

model = whisper.load_model(args.model)
model.language = args.language

input_dir = args.directory
output_dir = args.directory

audio_files = [f for f in os.listdir(input_dir) if f.endswith(".mp3") or f.endswith(".wav")]

for audio_file in tqdm.tqdm(audio_files, desc="Processing audio files"):
    audio_path = os.path.join(input_dir, audio_file)
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)
    result = whisper.transcribe(model, audio)
    text = result["text"]
    if args.language == "Chinese":
        output = cn_output(text)
    elif args.language == "English":
        output = en_output(text)
    elif args.language == "Japanese":
        output = jp_output(text)
    else:
        output = text
    output_path = os.path.join(output_dir, os.path.splitext(audio_file)[0] + ".lab")
    if os.path.exists(output_path):
        os.remove(output_path)
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(output)

print("\nInference completed")