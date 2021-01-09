### The Sonnification of Pendulum Waves using Pure Data and automative mathematical implementation of it through Python

## Installation

  - Python3 and Pure Data 0.48 or more required
  
  _How to Run_

As of right now, no extra libraries are needed to run any of the code included in the github. This should be able to run on vanilla Python3 and Pure Data. You must have access to both runtimes to run the code.

Run main.py using your preferred IDE or via the command prompt. A GUI should pop up with 4 input sections should pop up. Fill in the required fields then hit Return on your keyboard. If all runs well, the clock variables (ms) should populate in the GUI and 2 new files will be written in the same folder you executed the code from - pendulum.txt & pdaudio.pd. 

pendulum.txt contains the list of clock variables generated from python
pdaudio.pd is the pure data code that will playback samples with the appropriate clock variables contained in pendulum.txt

Make sure you run the pdaudio file in the same folder as the samples you want to use. They must be .wav format and named 0.wav, 1.wav, 2.wav etc…. 



# Abstract

The model of a pendulum waves is represented by multi temporal nodes that oscillate at different frequencies, sync’ing up at pre determined points (common multiple of oscillations). Using Pure Data, one can sonnify this phenomenon. The tedium of coding this can be circumvented by automating the process using Python, thus allowing for simple model building for large multi-phonic voice arrangements. 

# Pendulum WaveMachine

The pendulum wave machine used as a basis for this project was demonstrated and published online via Harvard University and made by Nils Sorensen. Sorensens’ design was derived from a design published by Richard Berg of the University of Maryland. Berg’s design was adapted from an earlier design published around 1867 by Ernst Mach when he was a professor of experimental physics at Charles University in Prague (originally called Charles-Ferninand University). 

The Harvard model showcases a system of 15 pendulums tied to strings of various lengths. The oscillations of the pendulums synchronize together after 60 seconds. The visual effect produced by the pendulums has been described as “hypnotic”. Each pendulum oscillates at different intervals therefore giving rise to complex structures of synchronicity between the different oscillating balls. Gestalt grouping allows for order to be perceived in the mass of chaos however, these glimpses of stability are fleeting as the balls quickly fall out of sync with one another. 

It is expected that when this model is sonified, this visual effect will carry over to the rhythmic domain. As balls go in and out of phase with one another, complex rhythmic patterns will arise and dissipate - evolving seamlessly between bits of metered and a-metered rhythmic structures. 

# Conversion to Aural Domain

When designing this model, it is important to take into account spatialization of sounds. Because the interface is working in a 2 channel array, all code will be focused on generating sounds in a stereo space (by default, it will be mono). The code will be easy to change for a multichannel setup if the end-user wishes to use this for performance/fixed media installation in a surround setup. 

The sonnifcation will focus on attributing a single sound trigger to each pendulum. So in the case of mimicking the Harvard model, there will be 15 different sounds, each drifting in and out of rhythmic phase with one another. These sounds will be sample based and not synthesized, however, slight modifications to the could enable someone to use synthesize sounds using PD’s built in DSP.

Each pendulum will be controlled by a timing module, allowing for greater precision of control than the original design’s string contraption. Due to the simplicity of the playback code, it will be simple to create timing and playback control for 100+ sound samples. 







