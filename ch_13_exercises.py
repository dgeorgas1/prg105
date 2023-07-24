"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text='Dan Georgas')
        self.label.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    my_gui2 = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label_name = tkinter.Label(self.top_frame, text='Dan Georgas')
        self.label_major = tkinter.Label(self.top_frame, text='AAS In Mobile Design and Development')

        self.label_name.pack()
        self.label_major.pack()

        self.label_graphic = tkinter.Label(self.bottom_frame, text='Graphic Design')
        self.label_programming = tkinter.Label(self.bottom_frame, text='Programming Logic')
        self.label_web = tkinter.Label(self.bottom_frame, text='Web Fundamentals')

        self.label_graphic.pack()
        self.label_programming.pack()
        self.label_web.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label_joke = tkinter.Label(self.main_window, text='What kind of music do bunnies like best?')

        self.btn = tkinter.Button(self.main_window, text='Click Here', command=self.display_punch_line)

        self.label_joke.pack()
        self.btn.pack()

        tkinter.mainloop()

    def display_punch_line(self):
        tkinter.messagebox.showinfo('Punch Line', 'Hip Hop')


if __name__ == '__main__':
    my_gui = GUI()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class Convert:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label_directions = tkinter.Label(self.top_frame, text='Enter a distance in inches: ')
        self.entry_inches = tkinter.Entry(self.top_frame)

        self.label_directions.pack(side='left')
        self.entry_inches.pack(side='left')

        self.btn_convert = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.btn_quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.btn_convert.pack(side='left')
        self.btn_quit.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inches = float(self.entry_inches.get())

        centimeters = inches * 2.54

        tkinter.messagebox.showinfo('Results', str(inches) + ' inches is equal to ' + str(centimeters) + ' centimeters.')


if __name__ == '__main__':
    convert = Convert()