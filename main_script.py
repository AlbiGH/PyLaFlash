import os
import numpy as np
import subprocess
body = []
pwd = os.getcwd()
print(pwd)
preAmb = open("preamble.txt","r")

for line in preAmb:
    body.append(line)

preAmb.close()
body.append("\\begin{document}")
body.append("\\maketitle")

content = open(".\\contentSlides.txt","r")

slides = []
cont = []
for line in content:
    if line == "%\n":
        slides.append(cont)
        cont = []
    cont.append(line)

content.close()
for x in np.random.permutation(len(slides)):
    body.extend(slides[x])

body.append("\\end{document}")

final = open(".\\finalSlides.tex","w")


for line in body:
    final.write(line)
final.close()
#
#subprocess.check_call(['pdflatex','-interaction nonstopmode', 'finalSlides.tex']) # if you can't compile right out of python, comment this line out and compile manually
