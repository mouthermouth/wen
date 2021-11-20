# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = '''The term biotechnology refers to any technology, process or practice that modifies or harnesses any living organism or system to be useful to any human purpose. The word defines itself: bio means life and technology is defined as the application, or harnessing of science for a specific purpose. When you hear the word biotechnology today, you probably think about scientists working at the cutting edge with viruses and genomes in a state-of-the-art laboratory, but when you consider how many different types of life there are, and how many different types of technologies there are, you begin to realize that biotechnology is a broad category that has been around for ages! It is not known precisely when people began using the word biotechnology to refer to technologies based on living things. Many believe the phrase was first coined in the early 1900s by a Hungarian engineer named Károly Ereky, but the practice of biotechnology began long before that and dates back almost to the beginning of human existence. But we have basically kept it in practice when we needed it in cases of: - Agriculture
-Vaccination
-Understanding Human DNA
-Mutation
-Understanding of Environement. But still its a question that before the development of such advanced technology nature was controlling all the phenomenon then what made us feel to develop so? The answer is simple, it was our curiosity, it was our imagination and thinking power which made us aware of the need that we humans should develop such technology that can make our life easy and help us to understand more about nature and its fruit.'''
# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

