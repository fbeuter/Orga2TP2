import csv
import numpy as np
from pylab import *

files = ["c.blur.lena.csv", "asm1.blur.lena.csv", "asm2.blur.lena.csv", 
"c.merge.lena.csv", "asm1.merge.lena.csv", "asm2.merge.lena.csv"]

class Data:
	n = ""
	size = ""
	min = float("inf")
	max = 0
	sum = 0

#plt.xkcd()

for f in files:
	dataN = []
	dataAvg = []
	dataMin = []
	dataMax = []
	with open("prom/" + f, "rb") as csvfile:
		reader = csv.reader(csvfile, delimiter=",")
		d = Data()
		for row in reader:
			if(row[0] != "N"):
				d = row[1].split("x")
				pixels = int(d[0]) * int(d[1])
				dataN.append(pixels)
				dataAvg.append(row[5])
				dataMin.append(row[2])
				dataMax.append(row[3])

	fig = figure(figsize=(5,5))	
	sub = fig.add_subplot(1,1,1)
	sub.plot(dataN, dataAvg, label="Promedio")
	sub.plot(dataN, dataMin, label="Min")
	sub.plot(dataN, dataMax, label="Max")
	xlabel('Pixeles')
	ylabel('Ciclos de clock')
	title(f.split(".")[0].upper())
	legend(bbox_to_anchor=(0.05, 0.95, 0, 0), loc=2, ncol=1, borderaxespad=0.)
	ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	fig.savefig("graph/"+ f.split(".")[0] + "_" + f.split(".")[1] +".pdf")

filesGroup = [["c.blur.lena.csv", "asm1.blur.lena.csv", "asm2.blur.lena.csv"],
["asm1.blur.lena.csv", "asm2.blur.lena.csv"], 
["c.merge.lena.csv", "asm1.merge.lena.csv", "asm2.merge.lena.csv"],
["asm1.merge.lena.csv", "asm2.merge.lena.csv"]]

for fg in filesGroup:
	fig = figure(figsize=(5,5))
	name = ""
	xlabel('Pixeles')
	ylabel('Ciclos de clock')
	for f in fg:
		sub = fig.add_subplot(1,1,1)

		dataN = []
		dataAvg = []
		with open("prom/" + f, "rb") as csvfile:
			reader = csv.reader(csvfile, delimiter=",")
			d = Data()
			for row in reader:
				if(row[0] != "N"):
					d = row[1].split("x")
					pixels = int(d[0]) * int(d[1])
					dataN.append(pixels)
					dataAvg.append(row[2])

		sub.plot(dataN, dataAvg, label=f.split(".")[0].upper())
		name += f.split(".")[0] + "_"
		title("Comparacion de " + f.split(".")[1].title())
		legend(bbox_to_anchor=(0.05, 0.95, 0, 0), loc=2, ncol=1, borderaxespad=0.)
	
	ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	fig.savefig("graph/"+ name + f.split(".")[1] + "_comp" + ".pdf")

filesGroup = [["c.blur.lena.csv", "c.blur.colores.csv", "c.blur.rojo.csv", "c.blur.verde.csv", "c.blur.azul.csv"], 
["asm1.blur.lena.csv", "asm1.blur.colores.csv", "asm1.blur.rojo.csv", "asm1.blur.verde.csv", "asm1.blur.azul.csv"], 
["asm2.blur.lena.csv", "asm2.blur.colores.csv", "asm2.blur.rojo.csv", "asm2.blur.verde.csv", "asm2.blur.azul.csv"]]

for fg in filesGroup:
	fig = figure(figsize=(5,5))
	xlabel('Pixeles')
	ylabel('Ciclos de clock')
	for f in fg:
		sub = fig.add_subplot(1,1,1)

		dataN = []
		dataAvg = []
		with open("prom/" + f, "rb") as csvfile:
			reader = csv.reader(csvfile, delimiter=",")
			d = Data()
			for row in reader:
				if(row[0] != "N"):
					d = row[1].split("x")
					pixels = int(d[0]) * int(d[1])
					dataN.append(pixels)
					dataAvg.append(row[5])
		sub.plot(dataN, dataAvg, label=f.split(".")[2].title())
		title(f.split(".")[0].upper())
		legend(bbox_to_anchor=(0.05, 0.95, 0, 0), loc=2, ncol=1, borderaxespad=0.)
	
	ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	fig.savefig("graph/" + f.split(".")[0] + "_" + f.split(".")[1] + "_lena_colors" +".pdf")