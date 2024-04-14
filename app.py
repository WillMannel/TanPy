import matplotlib.pyplot as plt
import numpy as np

def plot_graph():
    # Define the function you want to plot (e.g., f(x) = x^2)
    f = lambda x: x**2
    
    # Generate x values
    x = np.linspace(-10, 10, 400)
    y = f(x)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label="f(x) = x^2")
    
    # Event handler to detect clicks
    def onclick(event):
        if event.xdata is not None and event.ydata is not None:
            ax.cla()  # Clear the previous plot
            ax.plot(x, y, label="f(x) = x^2")  # Redraw the function
            draw_tangent_line(f, event.xdata, ax)  # Draw tangent line at the clicked x
            
            plt.draw()
    
    # Connect the click event to the handler
    fig.canvas.mpl_connect('button_press_event', onclick)
    
    # Show the plot with grid
    ax.grid(True)
    plt.legend()
    plt.show()

def draw_tangent_line(f, x_point, ax):
    # Calculate the derivative using a numerical method
    h = 0.0001
    derivative = (f(x_point + h) - f(x_point - h)) / (2 * h)
    
    # Calculate y for the tangent line: y = m(x - x_point) + y_point
    y_point = f(x_point)
    tangent_line = lambda x: derivative * (x - x_point) + y_point
    
    # Plot tangent line
    x_values = np.linspace(x_point - 3, x_point + 3, 10)
    ax.plot(x_values, tangent_line(x_values), label=f"Tangent at x = {x_point:.2f}", color="red")
    ax.plot(x_point, y_point, 'ro')  # Mark the point of tangency
    
    # Add a legend
    ax.legend()

# Run the program
plot_graph()
