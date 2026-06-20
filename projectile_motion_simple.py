# hi

import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile_motion(initial_velocity, angle_degree):
    '''
    Displays a line graph of trajectory of an object in simple projectile motion. 

    Parameters:
    initial_velocity is the object's initial speed in m/s.
    angle_degree is the initial angle of Flight from the horizontal. Positive is moving counter clockwise from the horizontal. (Negative is moving clockwise)
    '''   
    # Initial parameters
    v0 = initial_velocity # Initial velocity (m/s)
    theta_deg = angle_degree # Launch angle in degrees
    g = 9.81 # acceleration due to gravity (m/s^2)

    # Convert angle to radians
    theta = np.radians(theta_deg)

    # Calculate theoretical range and time of flight
    flight_time = (2 * v0 * np.sin(theta)) / g
    total_range = (v0**2 * np.sin(2 * theta)) / g

    # Generate time array and trajectory arrays
    t = np.linspace(0, flight_time, num=100)
    x = v0 * np.cos(theta) * t
    y = (v0 * np.sin(theta) * t) - (0.5 * g * t**2)

    # Plotting the trajectory
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f'Trajectory at {theta_deg}°')
    plt.title('Projectile Motion Trajectory')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.ylim(bottom=0)
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__": # use for module
    simulate_projectile_motion(50, 45)