from microbit import *
import music

STATE_INTRO = 1
STATE_MAIN = 2
ONE_SECOND_MS = 1000

gameState = STATE_INTRO;
introMusicPlayed = False;

# Palette town intro music
palletTownNotes =  ["D4:2", "C", "B3", "A", "G4", "E", "F#", "E",
                    "D:6", "B3:2", "G", "G", "A", "B",
                    "C4:6", "F#3:2", "G", "A", "B:6",
                    "C4:1", "B3", "A:5"]

# Animated spinning pokeball
pokeballFrame1 = Image("06660:"
             "64446:"
             "66966:"
             "60006:"
             "06660")
pokeballFrame2 = Image("06660:"
             "60646:"
             "60946:"
             "60646:"
             "06660")

pokeballFrames = [pokeballFrame1, pokeballFrame2]

# Animate pokeball on startup
for i in range(2):
    display.show(pokeballFrames, delay=ONE_SECOND_MS)

while True:
    display.clear()
    
    if (gameState == STATE_INTRO):
        if (introMusicPlayed == False):
            introMusicPlayed = True
            music.play(palletTownNotes, wait=False)

        if (button_a.is_pressed()):
            music.stop()
            gameState = STATE_MAIN
        else:
            display.show('A')
            sleep(ONE_SECOND_MS / 2)

            display.show(Image.ARROW_W)
            sleep(ONE_SECOND_MS / 2)
    elif (gameState == STATE_MAIN):
        display.scroll('Todo! :)')
