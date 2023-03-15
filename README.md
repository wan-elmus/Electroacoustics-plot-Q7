## plot

This program defines a pressure pulse propagating in a medium with certain parameters, and plots the pressure at different positions and times.

First, the code sets the parameters P_max, tau, and c, which correspond to the maximum pressure, the time constant, and the speed of sound in the medium, respectively.

Then, a grid of x and t values is created using the np.linspace function. The x values are centered around 0 using the line x = x - x[int(len(x)/2)]. The t values are defined as an array with three elements.

*Note*
x represents the spatial coordinate in meters (m). np.linspace(-10, 10, 1000) generates an array of 1000 equally spaced values between -10 and 10, which is then centered around 0 by subtracting the value at the middle index of the array from all the values in the array. The resulting array x represents the spatial coordinates ranging from -10 m to 10 m, with the origin at the center. This x array is then used to create a meshgrid with t array to compute the pressure pulse P at each point on the grid.

Next, a meshgrid of x and t values is created using the np.meshgrid function.

The pressure pulse is calculated using the formula P_max * np.exp(-(t_grid/tau)**2) * np.exp(-(x_grid/(2*c*t_grid))**2), which represents a Gaussian function of time and space. The result is a 2D array of pressure values corresponding to each x and t value.

Invalid values where t_grid is zero are masked using np.ma.masked_invalid, since the exponential function in the formula would otherwise produce NaN values.

Finally, the pressure pulse is plotted for different times using the plt.plot function, and the resulting figure is displayed using plt.show(). The figure contains three subplots: the first shows the pressure pulse at all three times, while the other two show the pressure pulse at specific times. The x-axis represents the position x and the y-axis represents the pressure P. The pressure is limited to a maximum value of 1100 Pa using plt.ylim([0, 1100]), and each subplot is given a title and axis labels.

### Error before plotting

The errors "divide by zero encountered in divide" and "invalid value encountered in divide" occur because in the calculation of pressure pulse P, the denominator 2*c*t_grid could become zero for some elements of t_grid. When this happens, the exp function evaluates to infinity, which then causes the P array to contain invalid values (NaNs).

To fix this issue, the code is masking these invalid values using np.ma.masked_invalid function.

### Plotted graph

The plotted graph shows different colors for each t=0.1 and t=0.2 because the data is being plotted as a "line plot" and the different colors are used to distinguish between the data corresponding to different values of t. Specifically, the plt.plot() function is being used to plot the pressure pulse as a function of x at different times t, using different colors for each value of t.

In the code, the pressure pulse P is a 2D array with dimensions (1000,3), where the first index corresponds to the x values, and the second index corresponds to the t values. To plot the data as a line plot, the plt.plot() function is called three times, once for each value of t. The x_grid array is used as the x values for the plot, and the corresponding pressure values are taken from the P array.

Since each plt.plot() call corresponds to a different value of t, the label argument is used to specify a label for each line. The legend() function is then called to display the legend with the corresponding labels for each line.
