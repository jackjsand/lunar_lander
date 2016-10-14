# -*- coding: utf-8 -*-
"""
Lunar Lander Game Script
By Jack Sandiford (SID: 4231908)

Use the engine to stop the lunar lander from crashing!

Created on Tue Oct  4 14:41:30 2016
@author: ppyjs8
"""

# Import required packages
import numpy              as np;
import matplotlib         as mpl;
import matplotlib.pyplot  as plt;
import matplotlib.widgets as ui;
import time;
import msvcrt;
from msvcrt import getch  as getch;


# This is the function that starts the game
def start(difficulty):
    print(difficulty)    
    """
    Initial Parameters & Data Storage
    """
    # timestep - 0.02 gives 25 changes in a second
    dt = 0.15;
    # initial position, velocity, accel. due to gravity
    x_0    = 100;
    v_0    = 0;
    a_grav = 1;
    # initial engine thrust, initial net accel.
    a_eng     = 0.0;
    a_eng_max = 3.0;
    f_net  = None;
    mass   = None;
    a_net0 = a_eng - a_grav;
    # safe landing speed limit
    v_safelim = 5.0;
    # initial amount of fuel
    fuel_amount = 100;
    # arrays for data storage
    data_a_net = np.array([a_net0]);
    data_v     = np.array([v_0]);
    data_x     = np.array([x_0]);
    data_t     = np.array([0]);
    
    
    """
    Setting up figure and GUI
    
    NOTE: Maybe use a list to apply one function to several objects
          This would simplify the code by a significant amount.
    """
    # Clearing any existing figures
    plt.close("all");
    # Removing navigation toolbar from figure windows
    mpl.rcParams['toolbar'] = 'None';
    # Create figure for the GUI
    fig_GUI = plt.figure(num=2, facecolor='#cccccc');
    # Set the window title of the GUI figure
    fig_GUI.canvas.set_window_title('Lunar Lander Interface');
    # Create axes for the bar graphs in a 16 x 6 grid, and label them
    x_barplot    = plt.subplot2grid((16,7), (0,0), rowspan=8);
    v_barplot    = plt.subplot2grid((16,7), (0,1), rowspan=8);
    # Add dotted line on velocity graph to indicate safe landing speed
    plt.hold(True);
    plt.plot(np.linspace(0,1,2), np.linspace(-v_safelim,-v_safelim,2),
             'r-', linewidth=3);
    # Create axes for the bar graphs in a 2 x 3 grid, and label them
    a_barplot    = plt.subplot2grid((16,7), (0,2), rowspan=8);
    fuel_barplot = plt.subplot2grid((16,7), (8,0), rowspan=3, colspan=3);
    eng_sliderax = plt.subplot2grid((16,7), (11,0), rowspan=3, colspan=1);
    # Adding engine thrust slider
    eng_slider = ui.Slider(eng_sliderax, 'Engine', 
                           a_eng, a_eng_max, valinit=0.0, color="#b30000");
    # Hide the slider value text and the slider label
    eng_slider.valtext.set_visible(False);
    eng_slider.label.set_visible(False);
    # Adjust padding between each subplot to improve spacing
    plt.tight_layout(pad=2.0);
    # Label each axes
    x_barplot.set_title('Height\n');
    v_barplot.set_title('Velocity\n');
    a_barplot.set_title('Acceleration\n');
    fuel_barplot.set_title('Fuel');
    eng_sliderax.set_title('Engine Control');
    # Add bar graphs
    x_barcontainer    = x_barplot.bar(0, data_x[0], width=1, color='#66ff99');
    v_barcontainer    = v_barplot.bar(0, data_v[0], width=1, color='#99ccff');
    a_barcontainer    = a_barplot.bar(0, 0, width=1, color='#ffff99');
    fuel_barcontainer = fuel_barplot.bar(0, 1, width=100, color='#cc99ff');
    # Remove unwanted axis tick lines and labels
    x_barplot.tick_params(axis='x', length=0, labelsize=0);
    v_barplot.tick_params(axis='x', length=0, labelsize=0);
    a_barplot.tick_params(axis='x', length=0, labelsize=0);
    fuel_barplot.tick_params(axis='both', length=0, labelsize=0);
    # Adjust axis tick lines and tick labels
    x_barplot.set_yticks(np.arange(0, 160+10, 20));
    v_barplot.set_yticks(np.arange(-20, 11, 5));
    a_barplot.set_yticks(np.arange(-a_grav, a_eng_max - a_grav + 0.1, 1));
    fuel_barplot.set_xticks(np.arange(0, 100+10, 25));
    # Get references for bar chart bars (rectangles)
    x_bar    = x_barcontainer[0];
    v_bar    = v_barcontainer[0];
    a_bar    = a_barcontainer[0];
    fuel_bar = fuel_barcontainer[0];
    
    
    """
    Add visual representation of lunar lander and surface
    """
    # Add axes and plot
    vr_axes = plt.subplot2grid((16,7), (0,3), rowspan=16, colspan=4);
    vr_axes.tick_params(axis='x', length=0, labelsize=0);
    vr_axes.set_yticks(np.arange(0, 100+10, 5));
    # Add lunar lander at initial position
    landerx = 0.5;
    landery = 100.0;    
    vr_plot = plt.plot(landerx, landery, 'kx');
    
    
    # Maximise the figure window
    plt.get_current_fig_manager().window.showMaximized();
    # Bring the GUI figure to the front
    plt.show();
    
    
    """
    Pause to allow packages to be imported
    """
    #plt.pause(1);
    
    
    """
    Lunar lander is released into freefall
    """
    lander_has_not_landed = True;
    data_counter = 0;
    t_0 = time.time();
    status = '';
    
    """
    while True:
        key = ord(getch())
        if key == 27: #ESC
            break
        elif key == 13: #Enter
            select()
        elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
            key = ord(getch())
            if key == 80: #Down arrow
                moveDown()
            elif key == 72: #Up arrow
                moveUp()
    """
    
    while(lander_has_not_landed):
        # Start a timer - count how long while loop iteration takes
        cycleTime_Start = time.time();
        # Check if there is any fuel left
        if(fuel_amount > 0):
            # Check slider for engine thrust value
            if(a_eng != eng_slider.val):
                # If value has changed to previous value, update engine thrust value
                a_eng = eng_slider.val;
            # If engine thrust is above 0, decrease fuel
            if((eng_slider.val > 0.0) & (fuel_amount != 0.0)):
                fuel_amount = fuel_amount - (0.5*eng_slider.val);
                fuel_bar.set_width(fuel_amount);
        else:
            a_bar.set_height(-1);
            fuel_bar.set_width(0);
            a_eng = 0;
        # Calculate the time the lander has been in falling for
        t_1 = time.time() - t_0;        
        # Calculate lander's new acceleration, velocity and position
        a_net1 = a_eng - a_grav;
        v_1 = data_v[data_counter] + (a_net1 * dt);
        x_1 = data_x[data_counter] + (v_1 * dt);
        # Update position on the plot
        a_bar.set_height(a_net1);    
        v_bar.set_height(v_1); # velocity can be negative, use absolute val
        x_bar.set_height(x_1);
        # Update visual representation
        #vr_plot.plot(landerx, landery, 'kx');
        # Increase counter 'data_entires' by 1
        data_counter += 1;
        # Save new values to data storage arrays
        data_a_net = np.append(data_a_net, [a_net1]);
        data_v     = np.append(data_v, [v_1]);
        data_x     = np.append(data_x, [x_1]);
        data_t     = np.append(data_t, [t_1]);
        # Check if lunar lander has crashed
        if(x_1 <= 0):      
            polynomial = np.array([0.5*data_a_net[data_counter-1], 
                                   data_v[data_counter-1], 
                                   data_x[data_counter-1]]);
            solutions = abs(np.roots(polynomial));
            fall_time = data_t[data_counter-1] + np.amin(solutions);
            print("Lander hit the ground after " + str(round(t_1, 4))
                + ' seconds.');
            # Check velocity
            # Use string formatting here to simplify code?
            if(abs(v_1) <= v_safelim):
                # Velocity is a safe velocity, do stuff            
                status = 'landed safely';
                print("The lunar lander landed successfully, with a speed of " 
                    + str(abs(v_1)) + 'm/s!');
            else:
                # Velocity is a bad velocity, do stuff
                status = 'crash-landed';
                print("The lunar lander crash-landed, with a speed of "  
                    + str(abs(v_1)) + 'm/s!');
            # Set lander_has_not_landed to False (don't repeat while loop)
            lander_has_not_landed = False;
        else:
            # Stop while loop iteration timer
            cycleTime_End = time.time() - cycleTime_Start;
            # Calculate the time we need to pause for to be inline with timestep
            pause_time = dt - cycleTime_End;
            plt.pause(0.05);
    
    
    """
    Produce a position vs. time graph from the results
    Add a 'Reset' button?
    """
    # Create figure and its reference
    fig_results = plt.figure(num=3, facecolor='#f2f2f2');
    # Set the window title of the results figure
    fig_results.canvas.set_window_title('Height vs. time');
    # Return a subplot axes for a 1 x 1 grid
    ax_results = plt.subplot(111)
    #Set the title of the results graph
    plt.title('Lunar lander\'s height as a function of time');
    # Set the y and x axis labels of the results graph
    plt.ylabel('Height');
    plt.xlabel('Time');
    # Plot the lander's position as a function of time on the subplot
    ax_results.plot(data_t, data_x);
    ax_results.axis([0, data_t[data_counter] + 4,
                     data_x[data_counter], data_x.max() + 10]);
    # Bring the results figure to the front
    plt.show();
    
    # Create figure and its reference
    fig_results = plt.figure(num=4, facecolor='#cccccc', figsize=[4, 1]);
    # Set the window title of the results figure
    fig_results.canvas.set_window_title('Status Message');
    # Add status message text to figure
    plt.axes(axisbg='#cccccc');
    plt.text(0.06,0.5,'Your lunar lander ' + status + '!',
             verticalalignment='center');
    plt.tick_params(axis='both', length=0, labelsize=0);
    
    """
    Confirm to parent script that this daughter script ran successfully
    """
    return True;