from gpiozero import TonalBuzzer
from time import sleep


tones = ["G", "G", "A", "G", "C", "B", "G", "G", "G", "E", "C", "B", "A", "F", "F", "E", "C", "D", "C"]
octave = 4
between_notes = 0.7

tbz = TonalBuzzer(17)


def play_tones(tones: list):
    for tone in tones:
        tbz.play(tone + str(octave))
        sleep(between_notes)
        tbz.stop()

# Play the song

play_tones(tones[:6])
sleep(1)
play_tones(tones[:6])
sleep(1)
play_tones(tones[6:12])
sleep(1)
play_tones(tones[12:])
