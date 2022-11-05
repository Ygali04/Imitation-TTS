#Run to import packages
import numpy as np
import torch
from scipy.io.wavfile import write
from IPython.display import Audio

text = "hello world, what a beautiful day"

# preprocessing
utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tts_utils')
sequences, lengths = utils.prepare_input_sequence([text])

# run the models
with torch.no_grad():
    mel, _, _ = tacotron2.infer(sequences, lengths)
    audio = waveglow.infer(mel)
audio_numpy = audio[0].data.cpu().numpy()
rate = 22050

Audio(audio_numpy, rate=rate)
