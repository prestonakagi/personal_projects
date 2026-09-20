# hi2

# A numerical model for projectile motion with quadratic drag is provided below. 
# This model uses the standard Euler-Cromer numerical method to solve the coupled differential equations over discrete time steps.

import numpy as np
import matplotlib.pyplot as plt
from math import isclose

"""
def simulate_projectile_motion_with_drag_and_changing_weight(radius, mass, initial_velocity, angle_degree, time_to_change_weight, speed_change):
    # Parameter speed_change: when Twinborn's weight increases at time_of_weight_change, a negative float will be added to and redefine (+=) vx[i].
    #                         When Twinborn's weight decreases at time_of_weight_change, a positive float will be added to and redefine (+=) vx[i].

    # 1. Physical Constants & Parameters
    g = 9.81 # acceleration due to gravity (m/s^2)
    rho = 1.225 # Air density at sea level (kg/m^3)
    C_d = 0.47 # Drag coefficient (sphere)
    r = radius # r = 0.037 # Radius of the object (meters)
    m = mass # m = 0.145 # Mass of the object (kg, e.g., baseball)
    # Calculate cross-sectional area
    A = np.pi * r**2 # Group constant drag terms for efficiency: F_d = k * v^2
    k = 0.5 * C_d * rho * A 

    # 2. Initial Conditions
    v0 = initial_velocity # 45.0 # Initial velocity (m/s)
    angle = angle_degree # 35.0 # Launch angle (degrees)
    x0, y0 = 0.0, 0.0 # Initial position
    # Convert angle to radians and split velocity components
    theta = np.radians(angle)
    vx0 = v0 * np.cos(theta) 
    vy0 = v0 * np.sin(theta)

    # 3. Time Stepping Setup
    dt = 0.001 # Time step size (seconds)
    t = [0.0] # Time array
    x = [x0] # X-position array
    y = [y0] # Y-position array
    vx = [vx0] # X-velocity array #NOTE: only Ferro iron will change the vx at certain time
    vy = [vy0] # Y-velocity array

    # 4. Numerical Integration Loop (Euler-Cromer Method)
    i = 0
    while y[i] >= 0.0:
        if any(isclose(time, time_to_change_weight, abs_tol=1e-3) for time in t):
            # change only vx[i]
            vx[i] += speed_change

            # Current total velocity magnitude
            v = np.sqrt(vx[i]**2 + vy[i]**2) #NOTE: only Ferro iron will change the vx at certain time
    
            # Calculate accelerations (F/m = a)
            # Drag force opposes the direction of each velocity component
            ax = - (k / m) * v * vx[i] #NOTE: only Ferro iron will change the vx at certain time
            ay = - g - (k / m) * v * vy[i]
    
            # Update velocities for the next step
            vx.append(vx[i] + ax * dt)
            vy.append(vy[i] + ay * dt)
    
            # Update positions using the newly calculated velocities
            x.append(x[i] + vx[i+1] * dt)
            y.append(y[i] + vy[i+1] * dt)
    
            # Advance time track
            t.append(t[i] + dt)
            i += 1
        else:
            # Current total velocity magnitude
            v = np.sqrt(vx[i]**2 + vy[i]**2)

            # Calculate accelerations (F/m = a)
            # Drag force opposes the direction of each velocity component
            ax = - (k / m) * v * vx[i]
            ay = - g - (k / m) * v * vy[i]

            # Update velocities for the next step
            vx.append(vx[i] + ax * dt)
            vy.append(vy[i] + ay * dt)

            # Update positions using the newly calculated velocities
            x.append(x[i] + vx[i+1] * dt)
            y.append(y[i] + vy[i+1] * dt)

            # Advance time track
            t.append(t[i] + dt)
            i += 1

    # 5. Plotting the Trajectory
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f'With Drag (Angle: {angle}°)', color='crimson', lw=2)
    plt.title("Projectile Motion Simulation with Quadratic Drag", fontsize=14)
    plt.xlabel("Horizontal Distance (meters)", fontsize=12)
    plt.ylabel("Vertical Height (meters)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', lw=1)
    plt.legend()
    plt.show()

    # Print critical metrics
    print(f"Max Height: {max(y):.2f} meters")
    print(f"Total Distance (Range): {x[-1]:.2f} meters")
    print(f"Total Flight Time: {t[-1]:.2f} seconds")
"""

def time_projectile_motion_with_drag_and_changing_weight(radius, mass, initial_velocity, angle_degree, time_to_change_weight, speed_change):
    # Parameter speed_change: when Twinborn's weight increases at time_of_weight_change, a negative float will be added to and redefine (+=) vx[i].
    #                         When Twinborn's weight decreases at time_of_weight_change, a positive float will be added to and redefine (+=) vx[i].
    # This is only for one time changing weight.
    # Return list of time_total_flight, max_height, total_distance

    # 1. Physics Parameters
    g = 9.81              # Gravity (m/s^2)
    m = mass # m = 0.145 # Mass of the object (kg, e.g., baseball)
    rho = 1.225           # Air density (kg/m^3)
    Cd = 0.47             # Drag coefficient (sphere)
    r = radius # r = 0.037 # Radius of the object (meters)
    A = np.pi * r**2      # Cross-sectional area

    # 2. Initial Conditions
    x, y = 0.0, 0.0       # Starting position
    v0 = initial_velocity # Initial velocity (m/s)
    angle = angle_degree  # Launch angle (degrees)
    rad_angle = np.radians(angle)

    vx = v0 * np.cos(rad_angle)
    vy = v0 * np.sin(rad_angle)

    # 3. Simulation Parameters
    dt = 0.001            # Time step (s)
    t = 0.0               # Initial time
    change_time = time_to_change_weight     # Time at which Vx changes (s)
    new_vx_to_add = speed_change         # The new Vx value after change_time (m/s)
    has_changed = False   # Flag to ensure it only fires once

    # Lists for plotting
    t_list, x_list, y_list = [], [], []

    # 4. Simulation Loop (Stops when it hits the ground)
    while y >= 0:
        # Record current state
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)

        # Calculate speed and drag force magnitude
        v = np.sqrt(vx**2 + vy**2)
        f_drag = 0.5 * rho * Cd * A * v**2

        # Decompose forces into components
        # Drag direction is always opposite to the current velocity direction
        f_drag_x = -f_drag * (vx / v)
        f_drag_y = -f_drag * (vy / v)

        # Accelerations (F = ma -> a = F/m)
        ax = f_drag_x / m
        ay = -g + (f_drag_y / m)

        # Update velocities and positions using Euler method
        x += vx * dt
        y += vy * dt
        vx += ax * dt
        vy += ay * dt

        # Check if we should alter Vx
        if t >= change_time and not has_changed:
            vx += new_vx_to_add         # Manually force the velocity change
            has_changed = True  # Mark as done

        t += dt
        
    # Save critical metrics
    max_height = max(y_list)
    total_distance = x_list[-1]
    time_total_flight = t_list[-1]
    #print(f"Args: {radius=}, {mass=}, {initial_velocity=}, {angle_degree=}, {time_to_change_weight=}, {speed_change=}")
    
    return [time_total_flight, max_height, total_distance]


def simulate_projectile_motion_with_drag_and_multiple_changing_weight(radius, mass, initial_velocity, angle_degree, times_to_change_weight, speed_changes):
    # Parameter speed_change: when Twinborn's weight increases at time_of_weight_change, a negative float will be added to and redefine (+=) vx[i].
    #                         When Twinborn's weight decreases at time_of_weight_change, a positive float will be added to and redefine (+=) vx[i].
    # This is for multiple times changing weight in one jump.

    # 1. Physics Parameters
    g = 9.81              # Gravity (m/s^2)
    m = mass # m = 0.145 # Mass of the object (kg, e.g., baseball)
    rho = 1.225           # Air density (kg/m^3)
    Cd = 0.47             # Drag coefficient (sphere)
    r = radius # r = 0.037 # Radius of the object (meters)
    A = np.pi * r**2      # Cross-sectional area

    # 2. Initial Conditions
    x, y = 0.0, 0.0       # Starting position
    v0 = initial_velocity # Initial velocity (m/s)
    angle = angle_degree  # Launch angle (degrees)
    rad_angle = np.radians(angle)

    vx = v0 * np.cos(rad_angle)
    vy = v0 * np.sin(rad_angle)

    # 3. Simulation Parameters
    dt = 0.001            # Time step (s)
    t = 0.0               # Initial time
    i = 0   # counter for user input lists.
    change_time = times_to_change_weight[i]     # Time at which Vx changes (s)
    new_vx_to_add = speed_changes[i]         # The new Vx value after change_time (m/s)
    has_changed = False   # Flag to ensure it only fires once for current time to change.

    # Lists for plotting
    t_list, x_list, y_list = [], [], []

    # 4. Simulation Loop (Stops when it hits the ground)
    while y >= 0:
        has_changed = False
        # Record current state
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)

        # Calculate speed and drag force magnitude
        v = np.sqrt(vx**2 + vy**2)
        f_drag = 0.5 * rho * Cd * A * v**2

        # Decompose forces into components
        # Drag direction is always opposite to the current velocity direction
        f_drag_x = -f_drag * (vx / v)
        f_drag_y = -f_drag * (vy / v)

        # Accelerations (F = ma -> a = F/m)
        ax = f_drag_x / m
        ay = -g + (f_drag_y / m)

        # Update velocities and positions using Euler method
        x += vx * dt
        y += vy * dt
        vx += ax * dt
        vy += ay * dt

        # Check if we should alter Vx
        if t >= change_time and not has_changed:
            vx += new_vx_to_add         # Manually force the velocity change
            i += 1 # advance user input lists.
            has_changed = True  # Mark as done

        t += dt
    
    # 5. Plotting the Trajectory
    plt.figure(figsize=(8, 5))
    plt.plot(x_list, y_list, label="Projectile Trajectory", color="blue")
    '''
    # Define your list of multiple change times
    change_times = [1.5, 3.0, 4.5]

    # Loop through each time to draw a vertical line
    for i, change_time in enumerate(change_times):
        # Find the matching x coordinate
        target_t = next(filter(lambda x: x >= change_time, t_list))
        x_val = x_list[t_list.index(target_t)]

        # Set the label only for the first line to avoid duplicate legend entries
        line_label = "Vx Change Point" if i == 0 else ""

        plt.axvline(x=x_val, color="red", linestyle="--", label=line_label)

        Key Parameter Adjustments
        enumerate(change_times): Tracks the current loop index (i). 
        This prevents your plot legend from generating duplicate labels for every single line drawn.
        line_label Conditional: Passes the descriptive label to plt.axvline only on the very first pass (i == 0). 
        Subsequent lines use an empty string so your legend remains clean.

        I can show you how to swap out the filter() function for a high-performance NumPy binary search (np.searchsorted).
    
        Since your t_list is monotonically increasing, you can completely eliminate the slow filter() loop and .index() lookups 
        by using binary search. If you are already using NumPy for your plotting data, np.searchsorted() finds the exact index 
        where a value should be inserted to maintain order, which is the fastest way to find your change points. 
        If you prefer to stick to standard Python without external libraries, 
        the built-in bisect.bisect_left() module achieves the exact same optimization.
        
        Option 1: The Fast NumPy Way (Recommended)
        This approach scales incredibly well for large datasets because it runs optimized C-code under the hood.

        import numpy as np

        # Convert lists to NumPy arrays if they aren't already
        t_arr = np.array(t_list)
        x_arr = np.array(x_list)

        change_times = [1.5, 3.0, 4.5]

        for i, change_time in enumerate(change_times):
            # Instantly finds the index where t >= change_time using binary search
            idx = np.searchsorted(t_arr, change_time)

            # Optional boundary check to prevent IndexError if change_time exceeds max time
            if idx < len(x_arr):
                x_val = x_arr[idx]
                line_label = "Vx Change Point" if i == 0 else ""
                plt.axvline(x=x_val, color="red", linestyle="--", label=line_label)

                
        import bisect

        change_times = [1.5, 3.0, 4.5]

        for i, change_time in enumerate(change_times):
            # Instantly finds the index where t >= change_time
            idx = bisect.bisect_left(t_list, change_time)

            if idx < len(x_list):
                x_val = x_list[idx]
                line_label = "Vx Change Point" if i == 0 else ""
                plt.axvline(x=x_val, color="red", linestyle="--", label=line_label)

        Performance Comparison
        Instead of reading through t_list element-by-element from the beginning 
        every single time (which takes longer as your list grows), 
        binary search continually cuts your list in half to find the target index 
        in just a few operations.
    '''
    # Convert lists to NumPy arrays if they aren't already
    t_arr = np.array(t_list)
    x_arr = np.array(x_list)

    # change_times = [1.5, 3.0, 4.5]

    for i, change_time in enumerate(times_to_change_weight):
        # Instantly finds the index where t >= change_time using binary search
        idx = np.searchsorted(t_arr, change_time)

        # Optional boundary check to prevent IndexError if change_time exceeds max time
        if idx < len(x_arr):
            x_val = x_arr[idx]
            line_label = "Vx Change Point" if i == 0 else ""
            plt.axvline(x=x_val, color="red", linestyle="--", label=line_label)
    # plt.axvline(x=x_list[t_list.index(next(filter(lambda x: x >= change_time, t_list)))], 
                # color="red", linestyle="--", label="Vx Change Point")
    plt.title("Projectile Motion with Drag and Variable Vx")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Print critical metrics
    print(f"Args for initial conditions: {radius=}, {mass=}, {initial_velocity=}, {angle_degree=}, {times_to_change_weight[0]=}, {speed_changes[0]=}\n{times_to_change_weight=}  {speed_changes=}")
    print(f"Max Height: {max(y_list):.2f} meters")
    print(f"Total Distance (Range): {x_list[-1]:.2f} meters")
    print(f"Total Flight Time: {t_list[-1]:.2f} seconds\n")


if __name__ == "__main__": # use for module
    time_projectile_motion_with_drag_and_changing_weight((1.65/2), 62, 50, 45, 0.050, 1)
    simulate_projectile_motion_with_drag_and_multiple_changing_weight((1.65/2), 62, 50, 45, 0.050, 1)