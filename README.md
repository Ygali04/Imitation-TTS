# Imitation-TTS

Inspired by PI-READER science fair project. Accurate text to speech converters are particularly vital for the visually impaired or legaly blind. 


# Challenges in implementing accurate text-to-speech converters include:

1) Text composed of ambiguous abbreviations. Ex: "in" can be the word "in" or an abbreviation for "inches."

2) Numeral pronounciation variation. Example: "123" can be read as "one two three" or "one hundred twenty three."

3) Heteronyms (words that are spelled identically but have different pronunciations and meanings). Example: "read" can be past or present tense version of the verb.

4) Variations in pronounciation and dialect (depending on context or just in general). Example: either has two pronunciations: [EE-ther] or [AHY-ther].

# Linguistics Intro

Phone: smallest discrete segment of sound

Phoneme: smallest unit of sound that distinguishes one word from another
Ex: "hope” is a three phoneme word, composed of the “h” sound, the long “oo” sound, and the “p” sound.
The English language has 44 phonemes.

Grapheme: symbolic identifier for a phoneme
Ex: "team" is composed of the graphemes: <t>, <ee>, <m>

Oddly, some phonemes (sounds) can be spelled with different graphemes (letters). Thus, there are more than 44 graphemes in English.

In addition, identically spelled graphemes can correspond to different phonemes. 
Ex: the "oo" grapheme can be either for the sound in the word "boot" or "book."
  
Prosody: elements of speech like intonation, tone, stress, duration, and rhythm.
Reflects emotional state and tone (questioning, commanding, accusatory, sarcastic, ironic, etc.)
Ex: "I never said she stole my money" can have 7 different meanings & interpretations depending on intonation and which word is stressed by the speaker.

# Pipeline

1) Text to Words:
Begin speech synthesis with pre-processing/normalization to reduce ambiguity (Challenge 1) using statistical probability techniques (Ex: Hidden Markov Models (HMM)) or NNs.

    Ex: if the word "year" occurs in the same sentence as "1843," the model would assign higher probability that the number is pronouned "eighteen forty three."

2) Words to Phonemes:
    
    Option 1 - Dictionary Mapping to Phonemes
  
      Issues - 
        
        i. a lot of memory is required to store this
        ii. one word can have different phonemes depending on its context if the pronunciation differs.

  Option 2 - Simplification via Graphemes
    
     Cons - irregular words in English that are pronounced very differently from writting.

3) Phonemes to Sound
  
    3 approaches:
  
        i. use human recordings
        ii. computer-generated phonemes (frequencies) 
        iii. mimic human voice mechanisms
  
# Types of text to speech models
  
  I. Concatenation synthesis
    
    Concatenate (string together) segments of recorded speech.
    
    Unit Selection Synthesis:

    Recorded utterances are broken down into phones, syllables, word, phrases, etc. using a speech recognition system.

    Segments are then sorted into a database according to pitch, duration, neighboring phones, etc.

    Desired utterances are produced by speech synthesizer by chaining best candidate segments via a decision tree from database at runtime.

    Pro: Sounds natural and least robotic

    Con: requires large database, time-consuming

  II. Formant synthesis

    Doesn't use human-recorded speech samples at runtime.

    Generates a perceived sound quality from adding sine waves together and uses an acoustic model.

    Parameters like frequency and noise are varied to create waveforms of artificial speech.

    Pro: works at high speeds, doesn't require database or pre-recorded samples

    Con: sounds robotic

  III. Articulatory synthesis

    Models the human vocal tract and articulation processes.

    Con: Obsolete in commercial speech synthesis systems
  
# End to End Synthesis

Synthesizes natural sounding speech from raw transcripts without any additional prosody information via a Tacotron2 and WaveGlow model.

Tacotron2 model produces mel spectrograms from input text using encoder-decoder architecture. WaveGlow uses produced mel spectrograms to generate speech.

Implementation of Tacotron2 uses Dropout instead of Zoneout to regularize the LSTM layers.
