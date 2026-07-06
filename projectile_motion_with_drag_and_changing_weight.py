# hi2

# A numerical model for projectile motion with quadratic drag is provided below. 
# This model uses the standard Euler-Cromer numerical method to solve the coupled differential equations over discrete time steps.

import numpy as np
import matplotlib.pyplot as plt
from math import isclose

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


if __name__ == "__main__": # use for module
    simulate_projectile_motion_with_drag_and_changing_weight((1.65/2), 62, 50, 45, 0.050, 1)