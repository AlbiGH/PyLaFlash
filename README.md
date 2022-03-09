# PyLaFlash
A short script to create flash slides via Python 3 and LaTeX/Beamer. 

The user inputs the questions and answers into the _contentSlides.txt_ files. Flash cards are set up as Beamer frames. Each Beamer frame is separated by a line consisting only of the **%** char which is how the script identifies the start and end of a frame. 

After all the content is read, the script generates a random sequence to display the slides, and outputs a _.tex_ file that the user must then compile. The script can be edited to also do the compilation, but you can run into many issues compiling LaTeX through Python and I don't yet have a foolproof way to ensure it works.

# Slide Formats

The script makes use of beamer's ability to split one frame into multiple frames while using the _itemize_ or _enumerate_ environment in LaTeX. Take a look at the current example slides text file to get an idea of how that works. If you want to ensure certain frames always show up in a set sequence or want to set up cards while not using the beamer package, you just have to ensure that **%** separates each chunk of flash cards for hte randomizer to work. 
