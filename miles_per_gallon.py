"""Chapter 13 Practice 2 Program - Miles Per Gallon

Assignment Requirements:
Write an object-oriented GUI program that calculates a car’s gas mileage. The program’s window should have Entry
widgets that let the user enter the number of gallons of gas the car holds, and the number of miles it can be driven
on a full tank. When a Calculate MPG button is clicked, the program should display the number of miles that the car
may be driven per gallon of gas. Use the following formula to calculate miles per gallon:"""

import tkinter


class MilesPerGallon:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label_gallons_held = tkinter.Label(self.top_frame, padx=20, text='Enter how many gallons your car holds:')
        self.entry_gallons = tkinter.Entry(self.top_frame)
        self.label_miles_traveled = tkinter.Label(self.top_frame, text='How many miles have you traveled:')
        self.entry_miles = tkinter.Entry(self.top_frame)

        self.label_gallons_held.pack()
        self.entry_gallons.pack()
        self.label_miles_traveled.pack()
        self.entry_miles.pack()

        self.value_mpg = tkinter.StringVar()
        self.label_convert = tkinter.Label(self.top_frame, textvariable=self.value_mpg)
        self.label_convert.pack()

        self.btn_convert = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.btm_quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.btn_convert.pack(side='left')
        self.btm_quit.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        gallons = self.entry_gallons.get()
        miles = self.entry_miles.get()

        miles_per_gallon = int(miles) / int(gallons)

        self.value_mpg.set('Converted to miles per gallon: ' + str(format(miles_per_gallon, '.2f')))


if __name__ == '__main__':
    mpg = MilesPerGallon()
