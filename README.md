# Python GUI Calculator

The Python GUI Calculator is provides an easy and intutitive design to allow users to be able to perform basic calculations including addition, subtraction, multiplication, floating point division, integer division, and exponents (shortcuts to squareroot and square provided). Built using Python's Tkinter GUI library, users can press on buttons to enter data or manually enter data using their keyboard. 

<p align = "center">
  <img src="images/calculator_gui_1.png" width = 250px>
  <img src="images/calculator_gui_2.png" width = 250px>
</p>

The Entry, Equals, Clear, Delete button objects were created separately as they have unique functions. The other buttons were stored in a 2D list and created using a FOR loop. This method reduces the overall clutter that would be required by creating each button separately. Challenges arose while setting the command attribute for the button objects, as the Python interpreter was unable to read the various values of the loop but only read the last iteration and assigned that value to each button. Eventually a lambda function using the below syntax was used to prevent this issue as a local iteration number was stored to let each iteration have their unique argument. The following image provides a visual of the GUI created:

