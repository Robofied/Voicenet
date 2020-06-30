## Voicenet
Comprehensive Python library for speech and voice.<br><br>
![testimage](https://github.com/Robofied/Voicenet/blob/master/Voicenet.png)

### Getting Started
Voicenet is a comprehensive library for performing speech/voice based functions. It is capable of doing:

* Gender detection based on the voice.
* Feature extraction from voice

<!-- * Pronunciation posterior score
* Articulation-rate
* Speech rate
* Filler words
* Age detection from voice.
* Speech Enhancement and Noise Reduction
* Emotion detection from voice.
* Speaker Identification and segmentation 
* Speech Tagging (Silence, Speech, Noise, Laughter, Song) -->

## Build Status

In development, released [first model](https://github.com/Robofied/Voicenet/releases/tag/v1.0).

## Installation

### With pip


### From Source

```python
git clone https://github.com/Robofied/Voicenet
cd Voicenet
pip install -e .
```

### Hardware Requirements

## Getting Started

### Downloading pre-trained models and data

You can download the models and data manually from the GitHub releases or use our download functions:

```python
from voicenet.utils.download import download_staeds_extract_data

directory = 'path-to-directory'

download_staeds_extract_data(direc=directory)

```

### Training Models

```python
from voicenet.training import GMMModelTraining

gmm_model = GMMModelTraining()

data_dir = 'path-to-load-data-from'
model_save_dir = 'path-to-save-trained-model'

gmm_model.train_model(data_dir = data_dir, model_dir = model_save_dir)
```


## Contributing to Voicenet

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

A detailed overview on how to contribute can be found in the contributing guide. There is also an overview on GitHub.

If you are simply looking to start working with the voicenet codebase, navigate to the GitHub "issues" tab and start looking through interesting issues. There are a number of issues listed under Docs and good first issue where you could start out.

You can also triage issues which may include reproducing bug reports, or asking for vital information such as version numbers or reproduction instructions.

Or maybe through using you have an idea of your own or are looking for something in the documentation and thinking ‘this can be improved’. You can do something about it!

Feel free to ask questions on the mailing list or on [Slack](https://robofied.slack.com).

# License
[BSD-3](https://github.com/Robofied/Voicenet/blob/master/LICENSE)


