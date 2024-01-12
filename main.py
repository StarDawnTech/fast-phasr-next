from faster_whisper import WhisperModel
import argparse
import tqdm
import os
from lang.ZhG2p import ZhG2p
from lang import JpG2p
import sys

zhg2p = ZhG2p('mandarin')
jpg2p = JpG2p

parser = argparse.ArgumentParser(description="Convert audio files to .lab files with pinyin using faster-whisper")
parser.add_argument("-m", "--model", type=str, choices=["tiny", "base", "small", "medium", "large"], default="large", help="The model of whisper")
parser.add_argument("-d", "--directory", type=str, required=True, help="The directory of audio files")
parser.add_argument("-l", "--language", type=str, choices=["Chinese", "Japanese"], default="Chinese", help="The language of whisper")
parser.add_argument("--device", type=str, choices=["cpu", "cuda"], default="cuda", help="The device to run the model")
parser.add_argument("--compute_type", type=str, choices=["float32", "float16", "int8_float16", "int8"], default="float16", help="The compute type for the model")
args = parser.parse_args()

model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type)
model.language = args.language

input_dir = args.directory
output_dir = args.directory

audio_files = [f for f in os.listdir(input_dir) if f.endswith(".mp3") or f.endswith(".wav")]

for audio_file in tqdm.tqdm(audio_files, desc="Processing audio files"):
    audio_path = os.path.join(input_dir, audio_file)
    segments, info = model.transcribe(audio_path, beam_size=5)
    text = ""
    for segment in segments:
        text += segment.text + " "
    if args.language == "Chinese":
        output = zhg2p.convert(text)
    elif args.language == "Japanese":
        output = jpg2p.convert(text)
    else:
        print("Unsupported language")
        sys.exit()
    output_path = os.path.join(output_dir, os.path.splitext(audio_file)[0] + ".lab")
    if os.path.exists(output_path):
        os.remove(output_path)
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(output)

print("\nInference completed")
