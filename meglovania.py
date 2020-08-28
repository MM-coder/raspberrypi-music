from gpiozero import TonalBuzzer
from time import sleep


tones = [['D', 'D', 'D', 'A', 'G#', 'G', 'F', 'D', 'F', 'G'], ['C', 'C', 'D', 'A', 'G#', 'G', 'F', 'D', 'F', 'G'], ['B', 'B', 'D', 'A', 'G#', 'G', 'F', 'D', 'F', 'G'], ['A#', 'A#', 'D', 'A', 'G#', 'G', 'F', 'D', 'F', 'G']]
octave = 4
between_notes = 0.3

tbz = TonalBuzzer(17)


def play_tones(tones: list):

    # For each tone (string) in the list

    for tone in tones:

        # Tell the buzzer to play the tones
        # Concat the octave

        tbz.play(tone + str(octave))

        # Wait for the time between notes

        sleep(between_notes)

        # Stop the buzzer

        tbz.stop()

# Play the song

for tone_set in tones:

    # For each list, play the tones

    play_tones(tone_set)