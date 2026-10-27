"""
With a Graphic User Interface (GUI), plan a Bachelor's degree classes (not including general education classes) over several semesters, and plan weekly schedule of classes for the next semester.
"""

from tkinter import *
# from tkinter import ttk  # for adding tabs to window
from tkinter import filedialog, messagebox # for saving a file and opening a file
import re
from dataclasses import dataclass

from substring_extraction import extract_multiple_bracketed_subtext

# How get data on degree catalog (SUU Professional Chemistry)? Couldn't use an API. 
# 05OCT26 went to website, looked at source, copied text part listing courses and 
# credits for main part of emphasis. 

course_abbr_and_name_pattern = r'View course details for (.*?)" onClick='
credit_pattern = r'</a> <strong>(.*?)</strong> Credit\(s\)'
current_path = r"C:\\Users\\prest\\OneDrive\\Documents\\AIO Python\\personal_projects\\personal_projects\\"
with open(current_path + "course_html.txt", "r", encoding="utf-8") as file:
    file_contents = file.read()
course_abbr_and_names = extract_multiple_bracketed_subtext(course_abbr_and_name_pattern, file_contents)
course_credits_str = extract_multiple_bracketed_subtext(credit_pattern, file_contents)
course_credits = [int(c) for c in course_credits_str]
"""TODO: get patterns and extract for: 
co-requisite: str
pre-requisites: list of str
can_pre-req_be_concurrent: Boolean
semester_offered: list of str
credits: int  </a> <strong>4</strong> Credit(s)
fee: float"""
print(f"length of course names = {len(course_abbr_and_names)}\n{course_abbr_and_names=}\n{len(course_credits)}\n{course_credits=}")
# Pattern in strings in course_abbr_and_names: 'course_abbreviation_name course_abbreviation_number - course_name'
	# extract abbreviation parts and course name when make instances' values.
course_dict = {}
for i, course in enumerate(course_abbr_and_names):
	parts = course.split() # split strings on space
	name_joined = " ".join(parts[3:]) # join already split course name
	# dictionary key example is "CHEM 1210", value is ["course name", credit: int].
	course_dict[parts[0] + " " + parts[1]] = [name_joined, course_credits[i]]

print(f"\n{course_dict["PHYS 2210"]=}")

# Save data in instances of a Class for Course.
"""
Attributes:
abbreviation_name (CHEM): str
Abbreviation_number: str (or int)
course_name: str
co-requisite: str
pre-requisites: list of str
can_pre-req_be_concurrent: Boolean
semester_offered: list of str
credits: int
fee: float
has_passed: Boolean
grid_row: int=0
grid_column: int=0

Methods:
get Course (a Class) attribute.
check if have passed a course
"""
"""
Key Rules for @dataclass Fields and Methods:
• Type Hints are Required: Every field in a dataclass must have a type hint (e.g., radius_meters: float). 
  If you omit the type hint, the decorator will completely ignore the variable and won't add it to the __init__ constructor.
• Default Values Last: Just like standard function signatures, any field with a default value 
  (like notes: Optional[str] = None) must come after all fields that do not have default values.
• The self Keyword: Methods inside a dataclass behave exactly like normal class methods. 
  They require self as the first argument to access the fields.
• Mutable Defaults Warning: If you want a list, dictionary, or set as a default value, 
  do not use = []. Use field(default_factory=list) instead to avoid bugs where multiple class instances share the exact same list.
"""
@dataclass # This built-in decorator eliminates the boilerplates of assigning self.x = x over multiple lines.
class Course:
	"""
	Representing a course in a Bachelor's degree program.
	"""
	# Type-hinted attributes (with multi-line formatting)
	abbreviation_name: str
	abbreviation_number: int
	course_name: str
	co_requisite: 'Course' # or None
	pre_requisites: list['Course']
	can_pre_req_be_concurrent: bool
	semester_offered: list[str]
	credits: int
	fee: float
	has_passed: bool
	grid_row: int = 0
	grid_column: int = 0
	# notes: Optional[str] = None  # Field with a default value

	# def calculate_momentum(self) -> float:
	

	# Wanted to test the dataclass decorator now to maake sure it works. 24OCT26 PA.
	# def p_method(self):
	# 	print(f"\nthe dataclass decorator works!")

# tester_course = Course("bio", 101, "Intro to BioloGy", None, ["pr1", "pr2"], False, ["Spring Even", "Fall"], 3, 20.22, True)

# for attribute, value in vars(tester_course).items():
#     print(f"{attribute}: {value}")

# tester_course.p_method()
"""
GUI elements might need/want:
menubar: file: open, save, exit. Edit: update passed courses.
Open a file
Save a file
Add window tabs
Grid layout
Labels
(listbox)
User input
(Scale or) progress bar
Drag and drop (widgets)
message box
"""

home_top_row = 10 # integer
home_right_end_column = 10 # integer

# function that after Course label drag and dropped, checks if pre-requistite is finished or already planned in a past semester.
def check_pre_requisites(course_instance: Course):
	"""
	After Course label drag and dropped, checks if pre-requistites are finished or already planned in past semester(s).

	Returns a list of two Booleans for 
	if all pre-requisites are finished and 
	if all pre-requisites already planned in past semester(s).
	"""
	# check if pre-reqs all finished

	not_passed_courses = []
	# if not all finished, which ones not finished and check if already planned, and display message.
	if course_instance.pre_requisites != []:
		for pre_req in course_instance.pre_requisites:
			if pre_req.has_passed == False:
				# add abbreviation name and number to a list for display on message box.
				not_passed_courses.append(f"{pre_req.abbreviation_name} {pre_req.abbreviation_number}")
				# check pre req grid coordinates to course's grid coordinates
				if pre_req.grid_column >= course_instance.grid_column:
					# display message that need to take pre req before course.
					messagebox.showwarning(
						title= "Take Pre-requisite Course", 
						message= f"Need to take pre-requisite course, {pre_req.abbreviation_name} {pre_req.abbreviation_number}, before taking {course_instance.abbreviation_name} {course_instance.abbreviation_number}."
					)
				# if pre req in home area
				elif pre_req.grid_column < home_right_end_column and pre_req.grid_row > home_top_row:
					continue
				elif pre_req.grid_column < course_instance.grid_column and pre_req.grid_row > home_top_row and pre_req.has_passed == False:
					# display message that since did not pass pre req, cannot take course at that semester.
					messagebox.showwarning(
											title= "Failed Pre-requisite Course", 
											message= f"Need to pass pre-requisite course, {pre_req.abbreviation_name} {pre_req.abbreviation_number}, before taking {course_instance.abbreviation_name} {course_instance.abbreviation_number}."
										)
					# return course's label to home area. NOTE: home area should be left and below of all scheduling tables/area.
					# home area: try 6 labels wide (or 5).
					pass

# try a custom class for labels for semester season and year.
"""
SemesterLabel
Attributes:
season: str
year: int
grid_row: int=0
grid_column: int=0
"""

# function to check if a course dropped into one of its correct season for semester (and even or odd year, if applicable). How do that??

# function to update has_passed attribute (to True) of a course.
def update_passing_course(course_instance: 'Course'):
	'''Change a Course's has_passed value to True.'''
	course_instance.has_passed = True

# Make GUI labels for all not completed courses and have them all displayed (at least when a new file made. If opening an existing file, show any not placed?)

# NOTE: any functions used in GUI widgets needs to be defined above Tk() start of GUI.

'''
# function for a submit button; just for educational info.
def submit():
	username = entry_instance_variable.get()
	# thing to do like print(username)
'''
def drag_start(event):
	widget_variable = event.widget
	widget_variable.startX = event.x
	widget_variable.startY = event.y

def drag_motion(event):
    widget_variable = event.widget
    x = widget_variable.winfo_x() - widget_variable.startX + event.x
    y = widget_variable.winfo_y() - widget_variable.startY + event.y
    widget_variable.place(x=x, y=y)

def saveFile():
	file_variable = filedialog.asksaveasfile(initialdir="C:\\____\\____\\____", defaultextension='.fileExtention', filetypes=[("Text file", ".txt"), ("HTML file", ".html"), ("All files", ".*")])
	file_content = variable_content_to_save.get(1.0, END) # in video example, a Text widget was saved, but had str(Text widget.get(1.0, END))
	file_variable.write(file_content)
	file.close()

# Basic GUI
"""
from tkinter import *
# from tkinter import ttk  # for adding tabs to window
# from tkinter import filedialog # for saving a file and opening a file

window = Tk()
window.geometry("IntxInt")
window.title("")

'''
# Notebook widget for adding tabs to a window
notebook_variable = ttk.Notebook(window)  # widget that manages a collection of windows/displays
tab1 = Frame(notebook_variable)
tab2 = Frame(notebook_variable)
notebook_variable.add(tab1, text="Tab 1")
notebook_variable.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both") # expand to fill any space not otherwise used. # fill space on x and y axis.
# Example to put a widget in a tab
# Label(tab1, text="Wazup", width=50, height=25).pack()
'''

# Menu bar
menubar Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=function_name_only)
fileMenu.add_command(label="Save", command=function_name_only)
# top - - - -  is called tearoff
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)  # leave as quit

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Update Passed Courses", command=function_name_only)


# grid.  (just for notes, widget.pack() adds widget to window.)
# widget.grid(row=0, column=0, columnspan=int)

# Label: bd is border width. bg is background color. fg is text color. If use an image, use compound= 'top, left, etc".
Label(window, text="string", font=("font_name", size:int, "bold, etc"), fg="color name or hexadecimal", bg="color", bd=int, pad or padx or pady= int)

# Entry is user input textbox for single line.
Entry(window)
entry_variable.insert(0, "string") # default text

button_variable = Button(window, text="string")
# activebackground and activeforeground are the colors when the button is being clicked.
button_variable.config(command=function_name_only, font=("font_name", size:int, "bold, etc"), bg=, etc.) # changes with .config() effect immediately without needing to recreate the widget.

# something to show visually progress to end of degree; how much courses passed so far.
# by Progressbar? Does progress bar always shown in window?
bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)
percent = StringVar()
text = StringVar()
percent_label = Label(window, textvariable=percent).pack()
text_label = Label(window, textvariable=text).pack()
# make a function for the edit Update Passed Courses that one thing it does is update progress bar. In that function, need:
percent.set(str(int(number_passed_courses_or_credits / total_number_of_courses_or_credits * 100)) + "%")
text.set(str(number_passed_courses_or_credits) + "/" + str(total_number_of_courses_or_credits) + " total credits completed" OR " total number of courses planned"

# Drag and drop
# following for more than one Label
label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)

#label.bind(event, drag_start)
label.bind("<Button-L>", drag_start) # 2nd is a function
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-L>", drag_start)
label2.bind("<B1-Motion>", drag_motion)


window.mainloop()
"""
