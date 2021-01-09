'''wavenum = input("how many voices? ")
lenght = input("how long for cycle:seconds ")
slowest = input("voice with least ammount of cycles? # of cycles " )
fastest = input("voice with most ammount of cycles? # of cycles " )
'''
import tkinter as tk
import pdfileformat as pdff
wavenum = 20
length = 20
slowest = 2
fastest = 100


file = open("pendulum.txt","w+")


d={}

root=tk.Tk()
root.title('PENDULUM CALCULATOR')
root.geometry("400x400")
root.configure(bg="brown")
output = tk.StringVar()
output.set("Generate list of voices in ms\n\n\n\n\n\n\n\n\n\n")

mytext = tk.StringVar(value='test ' * 30)
myentry = tk.Entry(root, textvariable=output, state='readonly')
myscroll = tk.Scrollbar(root, orient='horizontal', command=myentry.xview)
myentry.config(xscrollcommand=myscroll.set)



#######GUI#############################

# LABELS

lvoices = tk.Label(root, text="Number of voices")
llength = tk.Label(root, text="Length of cycle (seconds)")
lslowest = tk.Label(root, text="Slowest voice (# of cycles) ")
lfastest = tk.Label(root, text="Fastest voice (# of cycles) ")
loutput = tk.Label(root, textvariable= output)

# ENTRY

evoices = tk.Entry(root, text="Number of voices")
elength = tk.Entry(root, text="Length of cycle")
eslowest = tk.Entry(root, text="Slowest voices")
efastest = tk.Entry(root, text="Fastest voices")

#PACKING
lvoices.pack()
evoices.pack()
llength.pack()
elength.pack()
lslowest.pack()
eslowest.pack()
lfastest.pack()
efastest.pack()
loutput.pack()
myscroll.pack


###FUNCTIONS##################

#gets values from entry widgets
def getvalues(event):
	global length
	wavenum = int(evoices.get())
	length = int(elength.get())
	slowest = int(eslowest.get())
	fastest = int(efastest.get())
	incrementcalc(wavenum,length,slowest,fastest)

root.bind("<Return>", getvalues)

# calculates how each voice should increment in (?)
def incrementcalc(wavenum,length,slowest,fastest):
	increment= (int(fastest)-int(slowest)) / (int(wavenum)-1)
	changeifstatements(wavenum,length,slowest,fastest,increment)
	print(increment)

# tbh idr
def changeifstatements(wavenum,length,slowest,fastest,increment):
	if (increment*wavenum)>fastest:
		change=-1
	elif (increment*wavenum)<fastest: 
		change=1
	else:
		change = 0
	wavenumdesignation(wavenum,length,slowest,fastest,increment)

# calculates n writes voice BPM
def wavenumdesignation(wavenum,length,slowest,fastest,increment):
	d={}
	bpmlist = ""
	d['1'] = slowest
	for x in range(1,wavenum):
		d[x+1]=((x*increment)+slowest)
	for x in d:
		y = (d[x])
		seconds = length/y
		seconds = seconds*1000
		bpm = 60/seconds
		# bpmlist not actually bpm, making list with seconds for metro
		bpmlist+=str(seconds)+"\n"
	output.set(bpmlist)
	file = open("pendulum.txt","w")
	file.write(bpmlist)
	file.close()
	pdff.format()




root.mainloop()