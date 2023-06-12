# Transcribed Speech Dataset Simulation

The goal of this project is to create a dataset for Named Entity Recognition (NER) tasks, simulating text obtained from a speech recognition system in the Russian language. The dataset will be generated from various sources, including the CommonVoice dataset in Russian from Mozilla, and pre-made datasets such as WikiANN and MultiNERD and Wikineural augmeted in a way to simulate errors after transcription.

## Table of Contents

- [Files](#files)
  - [multiprocessing_converter.py](#multiprocessing_converterpy)
- [Data](#data)
   - [Wikineural](#wikineural)
   - [Common_Voice](#common_voice)
   - [MultiNERD](#multinerd)
   - [Wikiann](#wikiann)


## Files

- `multiprocessing_converter.py`: the converter script used to transcribe the entire Russian CommonVoice dataset. It utilizes the Vosk library for speech recognition and conversion. This script employs multiprocessing techniques to enhance efficiency in processing a large number of audio files.

## Data

### Wikineural
[Source](https://huggingface.co/datasets/Babelscape/wikineural)

- `Wikineural_augmentation.ipynb`: Code used to augment the data.
- `Wikineural_augmented.csv`: Augmented data

### Common_Voice
[Source](https://commonvoice.mozilla.org/en/datasets)

- `Editing_NER_anotations_Common_Voice.ipynb`: Code used to get NER markup of the corpus.
- `NER_Common_Voice_ru.csv`: Transcribed and marked data, fine tuned BERT model was used to produce the NER markup.

### MultiNERD
[Source](https://github.com/babelscape/multinerd)

- `MultiNERD_augmentation.ipynb`: Code used to augment the data.
- `MultiNERD_augmented.csv`: Augmented data

### Wikiann
[Source](https://huggingface.co/datasets/wikiann)

- `Wikiann_augmentation.ipynb`: Code used to augment the data.
- `Wikiann_augmented.csv`: Augmented data



Please note that as this project is a work in progress, additional files and details will be added as the dataset simulation progresses.
