import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from MetodosEDOs import runge_kutta_4  #Run this from the carpet above in the terminal

# Number of double pendulums to simulate
Number = 10  # Set the number of pendulums you want to simulate
dt = 0.05  # Time step
t = np.linspace(0, 30, int(30/dt))  # Defining the time array

# Define the double pendulum motion equations
def double_pend(u, m1, m2, l1, l2, g):
    """
    Motion equations of a double pendulum derived from the Lagrangian.
    Args:
        u: The vector to solve using numerical methods for ODEs.
        m1, m2: Masses of the two pendulums.
        l1, l2: Lengths of the two pendulums.
        g: Gravity acceleration on Earth.
    """
    theta1, theta2, w1, w2 = u
    alpha = (m1 + m2) * l1**2
    beta = m2 * l1 * l2 * np.cos(theta1 - theta2)
    gamma = m2 * l2**2
    delta = m2 * l1 * l2 * (w2**2) * np.sin(theta1 - theta2) + l1 * g * (m1 + m2) * np.sin(theta1)
    epsilon = -m2 * l1 * l2 * (w1**2) * np.sin(theta1 - theta2) + l2 * m2 * g * np.sin(theta2)

    return np.array([w1,
                     w2,
                     (-beta / alpha) * (((delta * beta) / alpha - epsilon) / (gamma - (beta**2) / alpha)) - delta / alpha,
                     ((beta * delta) / alpha - epsilon) / (gamma - (beta**2) / alpha)])

# Initialize the figure and axis
plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)  # Set x-limits for the plot
ax.set_ylim(-2, 2)  # Set y-limits for the plot

# Create a list to store the lines for each pendulum
lines = [ax.plot([], [], 'o-', lw=2)[0] for _ in range(Number)]  # 'o-' creates lines with markers

# Define the initial conditions for all pendulums
initial_conditions = [np.array([np.pi/2 ,
                                 np.pi/2 ,
                                   dt/4 *i,
                                     0])
                                       for i in range(Number)]

# Use the Runge-Kutta method to get the results for each pendulum
results = [runge_kutta_4(lambda u,
                            t: double_pend(u, 1, 1, 2, 1, 9.8),
                              u0,
                                t,) 
                                  for u0 in initial_conditions]

def init():
    """Initialize the background with multiple pendulums."""
    for line in lines:
        line.set_data([], [])
    return lines


def update(frame):
    """Update the pendulums' positions for each frame."""
    for i, line in enumerate(lines):
        # Extract positions for each pendulum at the current frame
        theta1 = results[i][frame, 0]  # Angle theta1 for pendulum i
        theta2 = results[i][frame, 1]  # Angle theta2 for pendulum i

        # Calculate the positions of the pendulum arms
        x1 = np.sin(theta1)
        y1 = -np.cos(theta1)
        x2 = x1 + np.sin(theta2)
        y2 = y1 - np.cos(theta2)

        # Update the pendulum positions for this frame
        line.set_data([0, x1, x2], [0, y1, y2])

    return lines

# Create the animation
ani = FuncAnimation(fig,
                     update,
                       frames=len(t),
                         init_func=init,
                           blit=True,
                           interval=dt * 1000)

# Show the plot with the animation
#ani.save("img/double_pend.gif",fps=60)

plt.show()



