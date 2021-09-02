# Python GUI Calculator

The Python GUI Calculator is provides an easy and intutitive design to allow users to be able to perform basic calculations including addition, subtraction, multiplication, floating point division, integer division, and exponents (shortcuts to squareroot and square provided). Built using Python's Tkinter GUI library, users can press on buttons to enter data or manually enter data using their keyboard. To work with exponents, users can input base**exponent to have it evalulate as base^exponent.

<p align = "center">
  <img src="images/calculator_gui_1.png" width = 250px>
  <img src="images/calculator_gui_2.png" width = 250px>
</p>

The Entry, Equals, Clear, Delete button objects were created separately as they have unique functions. The other buttons were stored in a 2D list and created using a FOR loop. This method reduces the overall clutter that would be required by creating each button separately. Challenges arose while setting the command attribute for the button objects, as the Python interpreter was unable to read the various values of the loop but only read the last iteration and assigned that value to each button. Eventually a lambda function using the below syntax was used to prevent this issue as a local iteration number was stored to let each iteration have their unique argument.

<p align= "center">Feel free to connect with me on any of the following platforms to talk about question, possible collaborations, opportunities, events, tech, or for fun!! Can't wait to meet you!</p>
<p align = "center">
  <a href="https://www.linkedin.com/in/divyank-shah/" target = "_blank">
    <img src="https://evergreenengineering.com/wp-content/uploads/2019/06/LinkedIn_logo_initials.png" width = 60px>
  </a>

  <a href="https://instagram.com/divyank.shah" target = "_blank">
    <img src="https://i.dlpng.com/static/png/6382269_preview.png" width = 90px>
  </a>

  <a href="https://github.com/shahdivyank" target = "_blank">
    <img src="https://www.tethysplatform.org/images/github-icon.png" width = 65px>
  </a>

  <a href="mailto:divyank.shah.2016@gmail.com" target = "_blank">
    <img src="https://logos-world.net/wp-content/uploads/2020/11/Gmail-Logo.png" width = 100px>
  </a>
</p>
