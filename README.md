## plot

This program defines a pressure pulse propagating in a medium with certain parameters, and plots the pressure at different positions and times.

First, the code sets the parameters P_max, tau, and c, which correspond to the maximum pressure, the time constant, and the speed of sound in the medium, respectively.

Then, a grid of x and t values is created using the np.linspace function. The x values are centered around 0 using the line x = x - x[int(len(x)/2)]. The t values are defined as an array with three elements.

Next, a meshgrid of x and t values is created using the np.meshgrid function.

The pressure pulse is calculated using the formula P_max * np.exp(-(t_grid/tau)**2) * np.exp(-(x_grid/(2*c*t_grid))**2), which represents a Gaussian function of time and space. The result is a 2D array of pressure values corresponding to each x and t value.

Invalid values where t_grid is zero are masked using np.ma.masked_invalid, since the exponential function in the formula would otherwise produce NaN values.

Finally, the pressure pulse is plotted for different times using the plt.plot function, and the resulting figure is displayed using plt.show(). The figure contains three subplots: the first shows the pressure pulse at all three times, while the other two show the pressure pulse at specific times. The x-axis represents the position x and the y-axis represents the pressure P. The pressure is limited to a maximum value of 1100 Pa using plt.ylim([0, 1100]), and each subplot is given a title and axis labels.
