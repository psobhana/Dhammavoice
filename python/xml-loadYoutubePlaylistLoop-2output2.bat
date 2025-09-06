xml-lines-loadYoutubePlaylistLoop-2words.py %1.xml words.txt
words-loadYoutubePlaylistLoop-2input-lines.py words.txt
REM above 2 lines create the input.txt file with the same number of lines as the input xml file.
xml-text-2words.py %1.xml
words2button.py input.txt 
REM This outputs to output.txt With words added
xml-loadYoutubePlaylistLoop-2words.py %1.xml
words2-loadYoutubePlaylistLoop-and-share.py output.txt