xml-lines-loadYoutubeStartStop-2words.py %1.xml
words-loadYoutubeStartStop-2input-lines.py words.txt
REM above 2 lines create the input.txt file with the same number of lines as the input xml file.
xml-text-2words.py %1.xml
words2button.py input.txt 
REM This outputs to output.txt With words added
xml-loadYoutubeStartStop-2words.py %1.xml
words2-loadYoutubeStartStop-and-share.py output.txt