def format():
	file = open("pdaudio.pd","w+")
	bpmlist = open("pendulum.txt","r+").read().splitlines()
	counter = 0
	x = 150
	y = 160
	togglecounter = 2
	metrocounter= 3
	readincounter = 4
	readoutcounter = 5

	file.write("#N canvas 0 22 794 702 12;\n")
	file.write("#X obj 18 12 tgl 100 0 empty empty empty 17 7 0 10 -261234 -1 -1 01;\n")
	file.write("#X obj 37 660 dac~;\n")

	for bpm in bpmlist:
		file.write("#X obj " + str(x) + " " + str(y) + " metro " + bpm + ";\n")
		file.write("#X msg " + str(x) +" 200 open "+ str(counter) + ".wav \, 1;\n")
		file.write("#X obj " + str(x) +" 240 readsf~;\n")
		file.write("#X obj " + str(x) +" 400 *~ 0.3;\n")
		file.write("#X connect 0 0 " + str(togglecounter) +" 0;\n")
		file.write("#X connect " + str(togglecounter) +" 0 " + str(metrocounter) +" 0;\n")
		file.write("#X connect " + str(readincounter) +" 0 " + str(readoutcounter) +" 0;\n")
		file.write("#X connect " + str(metrocounter) +" 0 " + str(readincounter) +" 0;")
		file.write("#X connect " + str(readoutcounter) +" 0 1 0;")
		file.write("#X connect " + str(readoutcounter) +" 0 1 1;")
		readincounter += 4
		readoutcounter += 4
		metrocounter += 4
		togglecounter += 4
		x += 100
		counter += 1
