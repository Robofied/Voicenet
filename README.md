## Voicenet
Comprehensive Python library for speech :speech_balloon: and voice :sound:.<br><br>
![testimage](https://github.com/Robofied/Voicenet/blob/master/resources/Voicenet.png)

## Getting Started
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

Models are trained and run on these machines -:

CPU(Octa-Core) 16GB RAM - Ubuntu 19.04 

## Getting Started

### Downloading pre-trained models and data

You can download the models and data manually from the GitHub [releases](https://github.com/Robofied/Voicenet/releases) or use our download functions:

```python
from voicenet.utils.download import download_staeds_extract_data

directory = 'path-to-directory'

download_staeds_extract_data(direc=directory)

```
If you are looking to work on ST-AEDS dataset with model training(we arlready have trained model but incase you want to train model again.) then you can skip this step as [training module](#Training-Models) already perform this step.


### Making Predictions

Trained models are saved in 'models/' directory

```python
from voicenet.pipeline import VoicePipeline

## VoicePipeline is initialize with "gmm" model as it will use by default gmm models
## VoicePipeline(model="gmm") //by deafult, other options are not available for now. 
voicenet = VoicePipeline()      
winner = voicenet.predict('wav-file-path.wav')

print(winner)

```

### Preparing Your Data

If you are planning to use [training modules](#Training-Models) of Voicenet then you can skip this step totally for ST-AEDS dataset and for any other dataset you have to download data in a [specific format](#2.-Any-other-dataset) and then skip it if want to use training modules

#### 1. ST-AEDS Dataset

<!-- If you are planning to work on ST-AEDS Dataset then you can do it either manually or with converters -->

<b>a. Manual</b>

You have to download ST-AEDS Dataset from [here]() and then extract it and split it into training and testing sets for females and males both separately as shown below(directory structure) 

![directory-structure](https://github.com/Robofied/Voicenet/blob/master/resources/ST-AEDS-directory.png)

<b>b. With converters</b>

```python
from voicenet.utils.download import download_staeds_extract_data
from voicenet.data_preparation import SplitData

directory = 'path-to-directory'

download_staeds_extract_data(direc=directory)
SplitData.staeds_data_preparation(os.path.join(data_dir, STAEDS))

```

#### 2. Any other dataset(Custom dataset)

<b>a. Manual</b>

You have to download/save your data into a directory which also contains subfolders female, male with thier respective females and males voice file.

Moving forward you need to prepare data i.e, training/testing data splitting and follow this [directory structure](#ST--AEDS-Dataset)

<b>b. With converters</b>

You have to dowload/save your data into a directory which should contains subfolders female, male with thier respective females and males voice file.

But in order to split dataset you can use -:

```python

from voicenet.data_preparation import SplitData

data_dir = 'path-to-load-data-from-containing-females-males-folder'

data_dir_females = 'path-to-load-data-from-containing-females-males-folder-and-load-only-females'

data_dir_males = 'path-to-load-data-from-containing-females-males-folder-and-load-only-males'

SplitData.universal_data_preparation(data_dir, data_dir_females, data_dir_males)

```



### Training Models



#### 1. ST-AEDS Dataset

```python

from voicenet.training import GMMModelTraining

gmm_model = GMMModelTraining()

data_dir = 'path-to-load-data-from'
model_save_dir = 'path-to-save-trained-model'

gmm_model.train_model(data_dir = data_dir, model_dir = model_save_dir)
```

#### 2. Any other dataset

```python

from voicenet.training import GMMModelTraining

gmm_model = GMMModelTraining(staeds_flag=False)

data_dir = 'path-to-load-data-from-containing-females-males-folder'

data_dir_females = 'path-to-load-data-from-containing-females-males-folder-and-load-only-females'

data_dir_males = 'path-to-load-data-from-containing-females-males-folder-and-load-only-males'

model_save_dir = 'path-to-save-trained-model'

## Examples to load females/males data
gmm_model.train_model(data_dir='data/raw/test', data_dir_females='data/raw/test/females', data_dir_males='data/raw/test/males', model_dir='models/')

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


