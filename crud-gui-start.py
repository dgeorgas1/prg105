"""Chapter 13 Assessment Program - CRUD GUI

Assignment Requirements:
You will create a CRUD (Create-Read-Update-Delete) program with a GUI interface for input and output. The logic of the
program will be similar to the CRUD Name and Address program you created in module 12, however you will use Tkinter
widgets to get data from the user and to display results.

The start file (below) provides the functionality of the main function, menu function, and read function in your
previous program. Using the example code provided in the start file and in your CRUD Name and Address program, complete
the TODO steps indicated to complete the program.

Use the CRUD GUI start file in your Exercises folder, or download it here Download download it here."""

# This program implements a simple CRUD (Create, Read, Update, Delete) GUI program
# Code is included to change font size for accessibility
import tkinter
import tkinter.messagebox
import tkinter.font as tkfont
import pickle


# main (root) GUI menu
class CrudGUI:
	def __init__(self, master):
		# the primary window (master) was initialized in the main() program
		#  -- save the master parameter in an instance variable to make it available throughout the class
		self.master = master
		self.master.title('Welcome Menu')

		# these statements tell Tkinter what font size to use for the default font
		default_font = tkfont.nametofont("TkDefaultFont")
		# TODO: change the size to use a larger value for better visibility
		default_font.configure(size=20)

		# create two frames -- one for the menu, one for the buttons
		self.top_frame = tkinter.Frame(self.master)
		self.bottom_frame = tkinter.Frame(self.master)

		# the menu uses Radio buttons so that only one option is selected at any time -- start by selecting option 1
		self.radio_var = tkinter.IntVar()
		self.radio_var.set(1)

		# create the radio buttons
		self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer', variable=self.radio_var, value=1)
		self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer', variable=self.radio_var, value=2)
		self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email', variable=self.radio_var, value=3)
		self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer', variable=self.radio_var, value=4)

		# for visibility at a larger scale, you can turn off the radiobutton indicator (icon)
		#  -- resulting in a push-button look (set indicatoron to False)
		#  -- (Tkinter also provides an option to provide custom images for the icons)
		self.look.configure(indicatoron=True)
		self.add.configure(indicatoron=True)
		self.change.configure(indicatoron=True)
		self.delete.configure(indicatoron=True)

		# pack the radio buttons
		self.look.pack(anchor='w', padx=20)
		self.add.pack(anchor='w', padx=20)
		self.change.pack(anchor='w', padx=20)
		self.delete.pack(anchor='w', padx=20)

		# create ok and quit buttons
		self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu, width=10)
		self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy, width=10)

		# pack the buttons
		self.ok_button.pack(side='left')
		self.quit_button.pack(side='left')

		# pack the frames
		self.top_frame.pack()
		self.bottom_frame.pack()

	# this method is called to process the menu choice when the OK button is pressed
	# TODO: you will need to modify this method to add more menu options based on the radio button selection
	#  -- each menu item should be instantiated as an appropriate class similar to the example provided
	#  -- you will add classes to Add/Create, Update, and Delete entries (the Read/Look class is provided)
	def open_menu(self):
		if self.radio_var.get() == 1:
			_ = LookGUI(self.master)
		elif self.radio_var.get() == 2:
			_ = AddGUI(self.master)
		elif self.radio_var.get() == 3:
			_ = ChangeGUI(self.master)
		elif self.radio_var.get() == 4:
			_ = DeleteGUI(self.master)
		else:
			tkinter.messagebox.showinfo('Function', 'still under construction')


# This example class processes the first user choice -- to look for a name (the Read option)
class LookGUI:
	def __init__(self, master):

		# open the file, load to customers, close file. Do this in each class
		try:
			input_file = open("customer_file.dat", 'rb')
			self.customers = pickle.load(input_file)
			input_file.close()
		except (FileNotFoundError, IOError):
			self.customers = {}

		# tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
		# when the Toplevel window is closed, it returns focus to the master window
		self.look = tkinter.Toplevel(master)
		self.look.title('Search for customer')

		# create Frames for this Toplevel window
		self.top_frame = tkinter.Frame(self.look)
		self.middle_frame = tkinter.Frame(self.look)
		self.bottom_frame = tkinter.Frame(self.look)

		# widgets for top frame - label and entry box for name
		self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
		# Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
		self.search_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

		# pack top frame
		self.search_label.pack(side='left')
		self.search_entry.pack(side='left')

		# middle frame - label for results
		self.info_string = tkinter.StringVar()
		self.info = tkinter.Label(self.middle_frame, text='Results: ')
		self.result_label = tkinter.Label(self.middle_frame, textvariable=self.info_string)

		# pack Middle frame
		self.info.pack(side='left')
		self.result_label.pack(side='left')

		# buttons for bottom frame
		self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search, width=10)
		self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

		# pack bottom frame
		self.search_button.pack(side='left')
		self.back_button.pack(side='left')

		# pack frames into the Toplevel window
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

	# this method is called by the Search button
	def search(self):
		# get the data from the entry box
		name = self.search_entry.get()
		# look for the name in the dictionary
		result = self.customers.get(name, 'Not Found')
		# display the result in the info label by setting its associated StringVar
		self.info_string.set(result)

	# this method is called by the Main Menu button to destroy the current window and return to the primary
	def go_back(self):
		self.look.destroy()


# TODO: you need to create classes similar to the LookGUI class for the other tasks: Create, Update, Delete
#  -- the logic to process each choice for the OK button should be
#  -- similar to the logic used in your Name and Email Address program
# TODO: Remember to pickle your data file after each change to the dictionary
class AddGUI:
	def __init__(self, master):

		# open the file, load to customers, close file. Do this in each class
		try:
			input_file = open("customer_file.dat", 'rb')
			self.customers = pickle.load(input_file)
			input_file.close()
		except (FileNotFoundError, IOError):
			self.customers = {}

		# tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
		# when the Toplevel window is closed, it returns focus to the master window
		self.add_master = tkinter.Toplevel(master)
		self.add_master.title('Add a customer')

		# create Frames for this Toplevel window
		self.top_frame = tkinter.Frame(self.add_master)
		self.second_frame = tkinter.Frame(self.add_master)
		self.third_frame = tkinter.Frame(self.add_master)
		self.bottom_frame = tkinter.Frame(self.add_master)

		# widgets for top frame - label and entry box for name
		self.name_label = tkinter.Label(self.top_frame, text='Enter customer name to add: ')
		# Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
		self.name_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

		# pack top frame
		self.name_label.pack(side='left')
		self.name_entry.pack(side='left')

		# widgets for second frame - label and entry box for email
		self.email_label = tkinter.Label(self.second_frame, text='Enter customer email to add: ')
		# Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
		self.email_entry = tkinter.Entry(self.second_frame, width=15, font="TkDefaultFont")

		# pack second frame
		self.email_label.pack(side='left')
		self.email_entry.pack(side='left')

		# third frame - label for results
		self.info_string = tkinter.StringVar()
		self.info = tkinter.Label(self.third_frame, text='Results: ')
		self.result_label = tkinter.Label(self.third_frame, textvariable=self.info_string)

		# pack third frame
		self.info.pack(side='left')
		self.result_label.pack(side='left')

		# buttons for bottom frame
		self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add, width=10)
		self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

		# pack bottom frame
		self.add_button.pack(side='left')
		self.back_button.pack(side='left')

		# pack frames into the Toplevel window
		self.top_frame.pack()
		self.second_frame.pack()
		self.third_frame.pack()
		self.bottom_frame.pack()

	def add(self):
		name = self.name_entry.get()

		if name not in self.customers:
			email = self.email_entry.get()
			self.customers[name] = email

			try:
				input_file = open('customer_file.dat', 'wb')
				pickle.dump(self.customers, input_file)
				input_file.close()
				self.info_string.set(f'{name} has been added with email {email}.')
			except FileNotFoundError:
				self.info_string.set("Warning - Unable to save file.")
		else:
			self.info_string.set('Unable to add data. The entered name already exists.')

	def go_back(self):
		self.add_master.destroy()


class ChangeGUI:
	def __init__(self, master):

		# open the file, load to customers, close file. Do this in each class
		try:
			input_file = open("customer_file.dat", 'rb')
			self.customers = pickle.load(input_file)
			input_file.close()
		except (FileNotFoundError, IOError):
			self.customers = {}

		# tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
		# when the Toplevel window is closed, it returns focus to the master window
		self.add = tkinter.Toplevel(master)
		self.add.title('Change a customer email')

		# create Frames for this Toplevel window
		self.top_frame = tkinter.Frame(self.add)
		self.second_frame = tkinter.Frame(self.add)
		self.third_frame = tkinter.Frame(self.add)
		self.bottom_frame = tkinter.Frame(self.add)

		# widgets for top frame - label and entry box for name
		self.name_label = tkinter.Label(self.top_frame, text='Enter customer name to change their email: ')
		# Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
		self.name_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

		# pack top frame
		self.name_label.pack(side='left')
		self.name_entry.pack(side='left')

		# widgets for second frame - label and entry box for email
		self.new_email_label = tkinter.Label(self.second_frame, text='Enter new email: ')
		self.new_email_entry = tkinter.Entry(self.second_frame, width=15, font="TkDefaultFont")

		# pack second frame
		self.new_email_label.pack(side='left')
		self.new_email_entry.pack(side='left')

		# third frame - label for results
		self.new_email_confirmation_string = tkinter.StringVar()
		self.new_email_confirmation_label = tkinter.Label(self.third_frame, textvariable=self.new_email_confirmation_string)

		# pack third frame
		self.new_email_confirmation_label.pack()

		# buttons for bottom frame
		self.change_button = tkinter.Button(self.bottom_frame, text='Change', command=self.change, width=10)
		self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

		# pack bottom frame
		self.change_button.pack(side='left')
		self.back_button.pack(side='left')

		# pack frames into the Toplevel window
		self.top_frame.pack()
		self.second_frame.pack()
		self.third_frame.pack()
		self.bottom_frame.pack()

	def change(self):
		name = self.name_entry.get()

		if name in self.customers:
			email = self.new_email_entry.get()
			self.customers[name] = email

			try:
				input_file = open('customer_file.dat', 'wb')
				pickle.dump(self.customers, input_file)
				input_file.close()
				self.new_email_confirmation_string.set(f'The email for {name} is now {email}.')
			except FileNotFoundError:
				self.new_email_confirmation_string.set("Warning - Unable to save file.")
		else:
			self.new_email_confirmation_string.set('No data found. Try adding a new entry.')

	def go_back(self):
		self.add.destroy()


class DeleteGUI:
	def __init__(self, master):

		# open the file, load to customers, close file. Do this in each class
		try:
			input_file = open("customer_file.dat", 'rb')
			self.customers = pickle.load(input_file)
			input_file.close()
		except (FileNotFoundError, IOError):
			self.customers = {}

		# tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
		# when the Toplevel window is closed, it returns focus to the master window
		self.add = tkinter.Toplevel(master)
		self.add.title('Delete a customer')

		# create Frames for this Toplevel window
		self.top_frame = tkinter.Frame(self.add)
		self.middle_frame = tkinter.Frame(self.add)
		self.bottom_frame = tkinter.Frame(self.add)

		# widgets for top frame - label and entry box for name
		self.name_label = tkinter.Label(self.top_frame, text='Enter customer name to delete: ')
		# Entry box uses its own font settings, so tell it to use the TkDefaultFont we set for the primary window
		self.name_entry = tkinter.Entry(self.top_frame, width=15, font="TkDefaultFont")

		# pack top frame
		self.name_label.pack(side='left')
		self.name_entry.pack(side='left')

		# middle frame - label for results
		self.info_string = tkinter.StringVar()
		self.info = tkinter.Label(self.middle_frame, text='Results: ')
		self.result_label = tkinter.Label(self.middle_frame, textvariable=self.info_string)

		# pack middle frame
		self.info.pack(side='left')
		self.result_label.pack(side='left')

		# buttons for bottom frame
		self.add_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete, width=10)
		self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.go_back, width=10)

		# pack bottom frame
		self.add_button.pack(side='left')
		self.back_button.pack(side='left')

		# pack frames into the Toplevel window
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

	def delete(self):
		name = self.name_entry.get()

		if name in self.customers:
			email = self.customers[name]
			del self.customers[name]

			try:
				input_file = open('customer_file.dat', 'wb')
				pickle.dump(self.customers, input_file)
				input_file.close()
				self.info_string.set(f'{name} has been deleted with email {email}.')
			except FileNotFoundError:
				self.info_string.set("Warning - Unable to save file.")
		else:
			self.info_string.set("No data found. Try adding a new entry.")

	def go_back(self):
		self.add.destroy()


def main():
	# create a window and initialize the Tk library
	root = tkinter.Tk()
	# call the GUI and send it the root window
	# use _ as variable name because the variable will not be needed after instantiating GUI
	# the GUI itself will handle the remaining program logic
	_ = CrudGUI(root)
	# because the root window was initialized here, we control the mainloop from main instead of the class
	root.mainloop()


main()
