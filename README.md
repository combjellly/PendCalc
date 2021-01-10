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

The model of a pendulum wave machine is represented by multi temporal nodes that oscillate at different frequencies, sync’ing up at pre-determined points (common multiple of oscillations). This interaction between nodes causes complex rhythmic patterns to arrise out of nodes drifting in and out of phase from one another.  Using Pure Data, one can sonnify this phenomenon. The tedium of coding this can be circumvented by automating the process using Python, thus allowing for simple model building for large multi-phonic voice arrangements. 

# Pendulum WaveMachine

The pendulum wave machine used as a basis for this project was demonstrated and published online via Harvard University and made by Nils Sorensen. Sorensens’ design was derived from a design published by Richard Berg of the University of Maryland. Berg’s design was adapted from an earlier design published around 1867 by Ernst Mach when he was a professor of experimental physics at Charles University in Prague (originally called Charles-Ferninand University). 

The Harvard model showcases a system of 15 pendulums tied to strings of various lengths. The oscillations of the pendulums synchronize together after 60 seconds. The visual effect produced by the pendulums has been described as “hypnotic”. Each pendulum oscillates at different intervals, giving rise to complex structures of synchronicity between the different oscillating balls. Gestalt grouping allows for order to be perceived in the mass of chaos, however these glimpses of stability are fleeting as the balls quickly fall out of sync with one another. 

When this model is sonified, this visual effect carries over to the rhythmic domain. As balls go in and out of phase with one another, complex rhythmic patterns will arise and dissipate - evolving seamlessly between bits of metered and a-metered rhythmic structures. 

# Conversion to Aural Domain

When sonifying this model, it is important to take into account the spatialization of sounds. Because the interface is working in a 2 channel array, all code will be focused on generating sounds in a stereo space (by default, it will all sounds will be summed into a single mono channel). The code is easy to adapt for a multichannel setup if the end-user wishes to use this for performance/fixed media installation in a surround setup. 

The sonnifcation will focus on attributing a single sound trigger to each pendulum. So in the case of mimicking the Harvard model, there will be 15 different sounds, each drifting in and out of rhythmic phase with one another. These sounds will be sample based and not synthesized, however, slight modifications to the code could enable someone to synthesize sounds using PD’s built in DSP. (an example of the harvard model will be included in the main git release (pdaudio.pd).

Each pendulum will be controlled by a timing module, allowing for greater precision of control than the original design’s string contraption. Due to the simplicity of the playback code, it will be simple to create timing and playback control for 100+ sound samples. 



# Determinante tempo algorithms [Variables needed to generate output data]

Using python, a simple algorithm takes 4 input variables and spits out a list of clock speeds needed for Pure Data to create pendulum wave rhythms at a a fixed time cycle. These 4 variables are:

**Number of voices** 

This variable tells the algorithm how many clock speeds to generate. This (if visualized) would be the amount of pendulums the machine would have. This variable controls how many samples will be played independently from another. 

**Length of Cycle** 

How long it will take before all the voices line up in time (fall into phase with one another). This is measured in seconds. Theoretically this component would allow you to create a composition that lasts for days, even weeks or years without ever repeating. 

**Slowest Voice (number of triggers per cycle)** 

The slowest voice in the composition. Dictated by the amount of oscillations it’ll have in the entire cycle. 


**Fastest Voice (number of triggers per cycle)** 

The slowest voice in the composition. Dictated by the amount of oscillations it’ll have in the entire cycle. 

### How it Works

Using all 4 user defined variables. the algorithm first calculates the interpolation increment (increment difference from one voice to the next). This increment is then used to calculate how many times each voice should be triggered in the sequence. This is not yet time dependent as the number of triggers can be converted to any time variable. It is important to remember that each pendulum’s oscillation must increase by the same number in order for the model to properly represent the Harvard Model’s patterns. 

	Number of voices = 15
	Length = 60 (s)
	Slowest = 51
 	Fastest = 65

	  increment= (int(Fastest)-int(Slowest)) / (int(# of voices)-1)
	  increment =  1 

With these numbers, it is simple to convert each voice to a clock variable using the total length of the cycle:

 	 clock variable = (length/voice) * 1000
  
# Automated Integration in Pure Data

To simplify the implementation of clock variables into Pure Data, python can automate Pure Data patch creation. Using an array of clock variables, it is possible for python to generate any number of sample engines, each with an appropriate clock speed for their corresponding voice. 

This is implemented using the format function in the included pdfileformat library. After python calculates the appropriate clock variables, it saves the array into a txt file that pdfileformat then accesses to generate a “pdaudio.pd” file. 

This automation saves time and allows the end user to make complex pure data patches that can have hundreds of voices. The generated pd file refers to local .wav files that are named via the numbering of voices - counting from 0 onwards. 

This is the section that would need to be altered to enable surround sound or more complex stereo specialization as the default routes all samples into the left and right channels of the default audio device that Pure Data uses. 

