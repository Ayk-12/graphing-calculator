# Graphing Calculator

This program visualizes mathematical functions in Python.

![graphing-calculator](https://github.com/Ayk-12/graphing-calculator/blob/main/Screenshots/graphing-calculator.png)

Running the main file (*graphing_calculator.py*) should open a window like the one above without any functions.
If the "pygame" package is not installed, the program will not run. Download it using `pip install pygame`.

## Usage
The program supports adding, removing, and saving funtions, in addition to creating custom functions and calculating specific values.

### Adding a function
To add a function, left click the **New Function** button on the panel to the left. Now, you will be able to write a function by typing on your keyboard. The syntax to write a function is as follows:

{name} {expression in x} {from x} {to x} {precision} {color RED} {color GREEN} {color BLUE}

Separate the fields by singular spaces.
After Enter is pressed, the function should appear on the graph (it may take up to a second, depending mainly on the *precision* and *from-to* interval of the function).
If the function did not appear, then something went wrong and the program could not draw the function. Re-enter the function, and check the syntax and notes below.

#### Example
![adding-new-function-a](https://github.com/Ayk-12/graphing-calculator/blob/main/Screenshots/adding-new-function-a.png)
![adding-new-function-b](https://github.com/Ayk-12/graphing-calculator/blob/main/Screenshots/adding-new-function-b.png)

#### Notes for adding functions
- *name* refers to the name of the function (usually f or g...)
- the expression must NOT include any spaces whatsoever
- use parentheses in the expression; x**2 and (x)**2 are different functions for negative numbers (the correct one is (x)**2)
- use * for multiplcation (and ** for exponentiation); "two times x" must be written as 2*x, and not 2x
- if there is a possibility of division by 0 in a function, it is best to offset the *from* and *to* by a small amount (eg., -10.1 10.1 instead of -10 10); alternatively, a custom function can be written to handle undefined cases (covered below)
- *precision* refers to the number of points the program draws; usually a *precision* between 100 and 200 is enough, but larger functions or bigger *from-to* intervals require a higher precision; a low precision means harsh and jagged lines, while a high precision means smoother lines, but it is more resource-intensive
- including {color R/G/B} is optional to customize the color of the function on the graph (color R/G/B must be integers between 0 and 255); not including a color will assign a randomly generated color to the function
- typing may feel slow or broken; the program can read only one key press at a time (except for Shift + {another key})

### Removing a function
To remove a function, simply left click on the function information on panel to the left. This will remove the function from the graph and from the saved functions in the json file.

### Saving a function
Added functions are automatically saved to *All_Functions_Saved.json*. To ensure they are properly saved, press Escape to exit the program.
If something goes wrong and the program crashes when adding a function (due to undefined function values), trying to reopen the program still causes it to crash (due to reloading the function with undefined behavior). To fix this, remove the function that is causing the crash from *All_Functions_Saved.json* (usually, the last added function).

### Calculating a specific function value
To find the value of a function at a specific point, left click the **f(a) = b** button on the panel to the left. The syntax is as follows:
{name}({value})
The result will appear on the bottom right corner of the screen, and a black dot on the graph will appear if the coordinate (value, function(value)) is visible on the screen.
If the coordinate is not visible, use the scroll wheel of the mouse to zoom in/out, or move around the graph using the arrow keys or by left click dragging.  

#### Example
![calculating-specific-value-a](https://github.com/Ayk-12/graphing-calculator/blob/main/Screenshots/calculating-specific-value-a.png)
![calculating-specific-value-b](https://github.com/Ayk-12/graphing-calculator/blob/main/Screenshots/calculating-specific-value-b.png)

### Writing a custom function
The program supports custom user-written functions. To add one, write any number returning Python function in *SomeFunctions.py*. The custom function can have any number of input parameters, as long as it returns a single number. To add a custom function to graph, abide by the syntax rules above, only replace the expression by "sf.{function name}".

#### Example
![adding-custom-function-a](https://github.com/Ayk-12/graphing-calculator/blob/main/Screenshots/adding-custom-function-a.png)
![adding-custom-function-b](https://github.com/Ayk-12/graphing-calculator/blob/main/Screenshots/adding-custom-function-b.png)
