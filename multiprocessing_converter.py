import os
from pydub import AudioSegment
import multiprocessing
import json
import vosk
import wave
from tqdm import tqdm
import csv


mp3_files_path = '/home/sergey/Python projects/RU_NER/CommonVoice_ru/ru/working_copy'
output_file = '/home/sergey/Python projects/RU_NER/converted_with_multiprocessing.csv'
save_interval = 500

model = vosk.Model('/home/sergey/Python projects/RU_NER/vosk-model-ru-0.42')
rec = vosk.KaldiRecognizer(model, 48000)


def convert_and_transcribe(mp3_file):
    index = os.path.basename(mp3_file).split('_')[3][:-4]
    wav = mp3_file.split('.')[0]+'.wav'
    audio = AudioSegment.from_mp3(mp3_file)
    audio = audio.set_channels(1)
    audio.export(wav, format='wav')
    with wave.open(wav, 'rb') as wf:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                os.remove(wav)
                break
            rec.AcceptWaveform(data)
    return index, json.loads(rec.FinalResult())['text']


def save_results(data, output_file):
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(data)


def process(mp3_files, save_interval, output_file):
    pool = multiprocessing.Pool()
    progress_bar = tqdm(total=len(mp3_files))

    def update_progress(*_):
        progress_bar.update()

    transcription = []
    for i, file in enumerate(mp3_files):
        transcription.append(pool.apply_async(convert_and_transcribe, args=(file,), callback=update_progress))
        if i % save_interval == 0:
            transcription = [t.get() for t in transcription]
            save_results(transcription, output_file)
            transcription = []

    pool.close()
    pool.join()

    transcription = [t.get() for t in transcription]
    progress_bar.close()
    return transcription


if __name__ == "__main__":
    mp3_files = [os.path.join(mp3_files_path, file) for file in os.listdir(mp3_files_path) if file.endswith(".mp3")]
    data = process(mp3_files, save_interval, output_file)
    save_results(data, output_file)
