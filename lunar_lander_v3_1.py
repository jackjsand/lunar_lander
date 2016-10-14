# -*- coding: utf-8 -*-
"""
Lunar Lander Parent Script
By Jack Sandiford (SID: 4231908)

Use the engine to stop the lunar lander from crashing!

Created on Tue Oct  4 14:41:30 2016
@author: ppyjs8
"""


"""
Clearing any previous variables and clearing the console
"""
### Remove all variables
# %reset
### Clear the terminal
# clear


"""
Import functions - via other python scripts
"""
import lunar_lander_main_menu as main_menu;
import lunar_lander_game      as game;


"""
Menu Screen:
Select difficulty and read instructions
"""
difficulty = main_menu.start();



"""
Run the lunar lander game
"""
game.start(difficulty);



"""
Features that could be added in the future:
- Menu screen
- Add instructions
- Several difficulty modes
- Bar colours change depending on bar height
- Get lunar lander visual representation working
- Tidy up code by adding all bars to a list
- Add a status message that predicts the outcome
- Add horizontal motion
- Add key bindings / listeners
- Add a quit button
- Add a pause button
- Add a reset button
- Save final score to a file
- Read score to check high score
- Add sound effects
- Add music
- Add lunar lander sprite (visual representation)
- Add engine effects (visual representation)
- Add arrow keys that highlight when an arrow key press is detected
- Add planet's ground (visual representation)
- Planet's colour and features depend on difficulty (visual representation)
- 
"""



"""
OTHER COMMENTS:

Couldn't manage to get the several difficulty buttons to work!
Will work on this in my own time.
"""
















