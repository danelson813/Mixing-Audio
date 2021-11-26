from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')
sax = AudioSegment.from_wav('sax.wav')

beat2 = beat*2
# beat2.export('beat2,wav')

mixed = beat2.overlay(sax)
# mixed.export('mixed.wav')

final = beat2 + mixed * 2 + sax + beat2 + sax
# final.export("final.wav")