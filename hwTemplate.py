import string

lst = string.ascii_lowercase

print("\n\n\nWelcome!\n")

name = input("What is your name?\n")

hw = input("What HW number is this?\n")

output = open("CS70__HW" + str(hw) + ".tex", "w")

hw = "HW" + hw

date = input("When is it due?\n")

partners = []
num = int(input("How many people did you work with?\n"))

for i in range(num):
	nombre = input("What is the name of partner " + str(i + 1) + "?\n")
	correo = input("What is their email?\n")
	partners.append((nombre, correo))

num = int(input("How many sections are there?\n"))

sections = []

for i in range(num):
	title = input("What is the title of section " + str(i + 1) + "?\n")
	print("What letter does it go up to?")
	end = input("If there is only one subsection, hit enter to skip this.\n").lower()
	sections.append((title, end.strip("\n")))

def opener():
	output.write("\\documentclass{article}\n")
	output.write("\\usepackage[utf8]{inputenc}\n")
	output.write("\\usepackage{amsmath}\n")
	output.write("\\usepackage{enumerate}\n")
	output.write("\n")
	output.write("\\title{CS70: " + hw + "}\n")
	output.write("\\author{" + name + "}\n")
	output.write("\\date{" + date + "}\n")
	output.write("\n")
	output.write("\n")
	output.write("\\begin{document}\n")
	output.write("\n")
	output.write("\\maketitle\n")
	if len(partners) > 0:
		output.write("I worked with:\n")
		output.write("\\begin{itemize}\n")
		output.write("\n")
		for tup in partners:
			output.write("	\\item " + tup[0] + " - " + tup[1] + "\n")
		output.write("\n")
		output.write("\\end{itemize}\n\n")
	output.write("I certify that all solutions are entirely in my words and that I have not looked at another student’s solutions. I have credited all external sources in this write up.\n")
	output.write("\\\\-" + name)
	output.write("\n\n")

def body():
	for tup in sections:
		output.write("\\section{" + tup[0] + "}\n\n")
		if len(tup[1]) > 0:
			end = lst.index(tup[1]) + 1
			x = 0
			output.write("\\begin{description}\n")
			output.write("\n")
			while x < end:
				output.write("	\\item[(" + lst[x] + ")] \n")
				output.write("\n")
				output.write("\n")
				x += 1
			output.write("\\end{description}\n")
			output.write("\n")

opener()

body()
	
output.write("\\end{document}\n")
