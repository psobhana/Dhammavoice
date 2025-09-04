xml-lines-loadYoutube2-2words.py %1.xml
words-loadYoutube2-2input-lines.py words.txt
REM above 2 lines create the input.txt file with the same number of lines as the input xml file.
xml-text-2words.py %1.xml
words2button.py input.txt
xml-loadYoutube2-2words.py %1.xml
words2-loadYoutube2-and-share.py output.txt
