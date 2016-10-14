# -*- coding: utf-8 -*-
"""
Lunar Lander Main Menu Script
By Jack Sandiford (SID: 4231908)

Use the engine to stop the lunar lander from crashing!

Created on Tue Oct  4 14:41:30 2016
@author: ppyjs8
"""

# Import required packages
import matplotlib         as mpl;
import matplotlib.pyplot  as plt;
import matplotlib.widgets as ui;

# Import functions - via other python scripts
import lunar_lander_difficulties as difficulties;

# This is the function that opens the main menu
def start():
    # Clearing any existing figures
    plt.close("all");
    # Removing navigation toolbar from figure windows
    mpl.rcParams['toolbar'] = 'None';
    # Create figure for the GUI
    fig_menu = plt.figure(num=1, facecolor='#cccccc');
    # Set the window title of the GUI figure
    fig_menu.canvas.set_window_title('Lunar Lander Main Menu');
    # Wait for a button to be pressed
    difficulty = 0;
    # Add 'Lunar Lander' text
    plt.axes(axisbg='#cccccc');
    plt.text(0,0,'Lunar Lander',
             verticalalignment='center');
    plt.tick_params(axis='both', length=0, labelsize=0);
    # Create axes for the bar graphs in a 2 x 3 grid, and label them
    ax_easy  = plt.subplot2grid((7,3), (3,1));
    ax_norm  = plt.subplot2grid((7,3), (4,1));    
    ax_hard  = plt.subplot2grid((7,3), (5,1));
    ax_earth = plt.subplot2grid((7,3), (6,1));
    # Adding engine thrust slider
    button_easy  = ui.Button(ax_easy, 'Easy', 
                           color='#999999', hovercolor='#b3b3b3');
    button_norm  = ui.Button(ax_norm, 'Normal', 
                           color='#999999', hovercolor='#b3b3b3');
    button_hard  = ui.Button(ax_hard, 'Hard', 
                           color='#999999', hovercolor='#b3b3b3');
    button_earth = ui.Button(ax_earth, 'Earth', 
                           color='#999999', hovercolor='#b3b3b3');
    # Adding callbacks to buttons
    callback = difficulties.Modes();
    difficulty = button_easy.on_clicked(callback.easy_mode);
    difficulty = button_norm.on_clicked(callback.norm_mode);
    difficulty = button_hard.on_clicked(callback.hard_mode);
    difficulty = button_earth.on_clicked(callback.earth_mode);
    # Bring the GUI figure to the front
    plt.show();
    # Wait for a response from one of the buttons
    #while(difficulty == 0):
    #    print('Looping');
    #    plt.pause(0.05);
    return difficulty;