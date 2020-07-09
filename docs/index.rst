.. vnet documentation master file, created by
   sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==============================================
Welcome to Voicenet documentation!
==============================================

Comprehensive Python library for speech and voice.

Current Version is [release](https://github.com/Robofied/Voicenet/releases)

.. _GitHub: https://github.com/Robofied/Voicenet

Key Features
============

- Performs gender detection from voice.
- Custom model training is easily performable

.. _aiohttp-installation:

Library Installation
====================

.. code-block:: bash

   $ pip install voicenet

Getting started
====================

Download Pretrained model and dataset(if required)
--------------------------------------------------

.. code-block:: python

   from voicenet.utils.download import download_staeds_extract_data

   directory = 'path-to-directory'

   download_staeds_extract_data(direc=directory)

Making prediction from pretrained models
----------------------------------------

.. code-block:: python

   from voicenet.pipeline import VoicePipeline

   ## VoicePipeline is initialize with "gmm" model as it will use by default gmm models
   ## VoicePipeline(model="gmm") //by deafult, other options are not available for now. 
   voicenet = VoicePipeline()      
   winner = voicenet.predict('wav-file-path.wav')

print(winner)


Source Code 
====================

The project is hosted on GitHub_

Please feel free to file an issue on the `bug tracker
<https://github.com/Robofied/Voicenet/issues>`_ if you have found a bug
or have some suggestion in order to improve the library.

Dependencies
====================

- joblib
- matplotlib
- numpy
- pandas
- python-speech-features==0.6
- requests
- scipy
- sklearn
- urllib3
- wget


Table of Contents
====================

.. toctree::
   :name: mastertoc
   :maxdepth: 2

   voicenet




