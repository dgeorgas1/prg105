"""Chapter 13 Practice 1 Program - Name and Address

Assignment Requirements:
This is a practice assignment that is demonstrated in the video The Name and Address ProblemLinks to an external
site.

Write a GUI program that displays your name and address when a button is clicked (you can use the address of the
school). The program’s window should resemble the sketch on the far left side of figure 13-26 when it runs. When
the user clicks the Show Info button, the program should display your name and address as shown in the sketch on the
right of the figure."""

import tkinter


class NameAndAddress:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.name_value = tkinter.StringVar()
        self.address_value = tkinter.StringVar()

        self.label_name = tkinter.Label(self.top_frame, textvariable=self.name_value)
        self.label_address = tkinter.Label(self.top_frame, padx=10, textvariable=self.address_value)

        self.label_name.pack()
        self.label_address.pack()

        self.btn_show_info = tkinter.Button(self.bottom_frame, text='Show Info', command=self.show_info)
        self.btn_quit = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.btn_show_info.pack(side='left')
        self.btn_quit.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_info(self):
        name = 'Dan Georgas'
        address = '8900 Northwest Hwy #14,\nCrystal Lake, IL 60012'

        self.name_value.set(name)
        self.address_value.set(address)


if __name__ == '__main__':
    name_address = NameAndAddress()
