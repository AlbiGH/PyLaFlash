# PyLaFlash
A short script to create flash slides via Python 3 and LaTeX/Beamer. 

The user inputs the slide content into the _contentSlides.txt_ files. Each Beamer frame is separated by a line consisting only of the **%** char which is how the script identifies the start and end of a frame. 

After all the content is read, the script generates a random sequence to display the slides in, and outputs a _.tex_ file that the user then compiles. Script can be edited to also do the compilation, but you can run into many issues compiling LaTeX through Python that I wasn't able to find an adequate solution for.

# Slide Formats

The script makes use of beamer's ability to split one frame into multiple frames while using the _itemize_ or _enumerate_ environment in LaTeX. Take a look at the current example slides to get an idea of how that works. However, if you want to ensure certain frames always show up in a set sequence, omit the **%** between frames in that sequence. 
