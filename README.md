# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

My pseudo code is:


COUNT_LETTER_IN_STRING gets two parameters: (STRING & LETTER):

  IF type of STRING not string:
    RETURN 0 value
  COUNT variable has 0 value

  FOR every CURRENT_LETTER in STRING:
    IF CURRENT_LETTER equal to LETTER (input parameter):
      increase COUNT with 1

  RETURN the value of COUNT to COUNT_LETTER_IN_STRING


### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

We have to import the 'tkinter' toolkit with all of it tools to our file first. After we create our main window with its 'Tk()' method, after the 'mainloop()' on the end of the file. For the last time we create or 'Canvas()' with at least three parameters, the 'width' and 'height' and where should it start. Before it close we should make a 'pack()' method for the canvas.

We should use the 'create_rectangle' order to draw it to our canvas. We have to give 2 paramaters, with 4 coordinate values.
The 'x' and 'y' coordinate of the top-left corner and the 'x' and 'y' coordinate of the bottom-right corner.

The number counts from the top left corner so 10px on the 'x' means the point 10px away from the left side. 10px on the 'y' means the point is 10 px away from the top.


--> example:

from tkinter import *

root = Tk()
canvas = Canvas(top, height=100px, width=100px)

canvas.create_rectangle(10px, 10px, 20px, 20px)

canvas.pack()
root.mainloop()



### What does V stand for in MVC? [2p]
#### Your answer:
