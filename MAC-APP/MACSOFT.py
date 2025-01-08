from tkinter import * 
import platform
import psutil
import subprocess
import time
from tkcalendar import Calendar
import webbrowser  # Import webbrowser for opening URLs

# Initialize the main window
root = Tk()
root.title('DV-soft')
root.geometry('850x500+300+170')
root.resizable(False, False)
root.configure(bg='#292e2e')

# Icon
icon_image = PhotoImage(file="dv.png")
root.iconphoto(False, icon_image)

Body = Frame(root, width=900, height=600, bg="#d6d6d6")
Body.pack(padx=20, pady=20, side=TOP)

# Left Hand Side Frame
LHS = Frame(Body, width=310, height=435, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
LHS.place(x=10, y=10)

# Logo
photo = PhotoImage(file="laptop.png")
myimage = Label(LHS, image=photo, background="#f4f5f5")
myimage.place(x=2, y=20)

my_system = platform.uname()

# System Information Labels
l1 = Label(LHS, text=my_system.node, bg="#f4f5f5", font=("Acumin variable concept", 8, 'bold'), justify="center")
l1.place(x=20, y=200)

l2 = Label(LHS, text=f"version: {my_system.version}", bg="#f4f5f5", font=("Acumin variable concept", 10, 'bold'), justify="center")
l2.place(x=20, y=225)

l3 = Label(LHS, text=f"system: {my_system.system}", bg="#f4f5f5", font=("Acumin variable concept", 9, 'bold'), justify="center")
l3.place(x=20, y=250)

l4 = Label(LHS, text=f"Machine: {my_system.machine}", bg="#f4f5f5", font=("Acumin variable concept", 7, 'bold'), justify="center")
l4.place(x=20, y=285)

l5 = Label(LHS, text=f"Total RAM installed: {round(psutil.virtual_memory().total / 1000000000, 2)} GB", bg="#f4f5f5", font=("Acumin variable concept", 12, 'bold'), justify="center")
l5.place(x=20, y=310)

l6 = Label(LHS, text=f"processo: {my_system.version}", bg="#f4f5f5", font=("Acumin variable concept", 7, 'bold'), justify="center")
l6.place(x=20, y=340)

# Right Hand Side Frame
RHS = Frame(Body, width=470, height=230, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
RHS.place(x=330, y=10)

system = Label(RHS, text='System', font=("Acimun variable concept", 20), bg="#f4f5f5")
system.place(x=10, y=10)

############################### Battery Functionality
def convertTime(seconds):
    if seconds == psutil.POWER_TIME_UNLIMITED:
        return "Charging"
    elif seconds == psutil.POWER_TIME_UNKNOWN:
        return "Unknown"
    else:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

def none():
    battery = psutil.sensors_battery()
    percent = battery.percent
    time = convertTime(battery.secsleft)

    lbl.config(text=f"{percent}%")
    lbl_plug.config(text=f'Plugged in: {str(battery.power_plugged)}')
    lbl_time.config(text=f'{time} remaining')

    # Battery status label
    battery_label = Label(RHS, text="Battery Status", font=("Acumin Variable Concept", 10), bg="#f4f5f5")
    battery_label.place(x=15, y=45)

    # Initialize battery_png with a default value
    battery_png = PhotoImage(file="battery.png")  # Default image

    if battery.power_plugged:
        battery_png = PhotoImage(file="charging.png")
    # Update the label with the correct image
    battery_label.config(image=battery_png)
    battery_label.image = battery_png  # Keep a reference to avoid garbage collection

    # Schedule the function to run again after 1000 ms (1 second)
    lbl.after(1000, none)

# Labels for battery information
lbl = Label(RHS, font=("Acumin variable concept", 40, 'bold'), bg="#f4f5f5")
lbl.place(x=200, y=40)

lbl_plug = Label(RHS, font=("Acumin Variable Concept", 10), bg="#f4f5f5")
lbl_plug.place(x=20, y=100)

# Create the second label for time
lbl_time = Label(RHS, font=("Acumin Variable Concept", 15), bg="#f4f5f5")
lbl_time.place(x=200, y=100)

# Start the battery status update
none()

# Right Hand Side Bottom Frame
RHB = Frame(Body, width=470, height=190, bg="#f4f5f5", highlightbackground="#adacb1", highlightthickness=1)
RHB.place(x=330, y=255)

apps = Label(RHB, text='Apps', font=('Acumin Variable Concept', 15), bg='#f4f5f5')
apps.place(x=10, y=10)

# Function to open Google search box
def open_google_search():
    search_window = Toplevel()
    search_window.title("Google Search")
    search_window.geometry("310x100+1170+570")  # Set width and height for the search window
    search_window.resizable(False, False)  # Prevent resizing

    # Entry field for search query
    search_entry = Entry(search_window, width=40)
    search_entry.pack(pady=20)

    # Function to perform the search
    def perform_search():
        query = search_entry.get()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")

    # Button to perform the search
    search_button = Button(search_window, text="Search", command=perform_search)
    search_button.pack(pady=5)

# Unified button functionality
def open_app(app_name):
    window = Toplevel()
    window.title(app_name)
    window.geometry("600x400")
    label = Label(window, text=f"{app_name} Window", font=("Acumin variable concept", 20), bg="#f4f5f5")
    label.pack(pady=40)

# Function to show current time
def show_time():
    time_window = Toplevel()
    time_window.title("Current Time")
    time_window.geometry("850x100+300+10")  # Set width, height, and position (x=400, y=200)
    time_window.resizable(False, False)  # Prevent resizing
    current_time = time.strftime("%H:%M:%S")  # Get current time
    time_label = Label(time_window, text=current_time, font=("Acumin variable concept", 45), bg="#f4f5f5")  # Smaller font size
    time_label.pack(pady=20)

# Function to open the calendar window
def open_calendar():
    calendar_window = Toplevel()
    calendar_window.title("Calendar")
    calendar_window.geometry("300x250+10+170")  # Set width, height, and position (x=10, y=10)
    calendar_window.resizable(False, False)  # Prevent resizing

    # Create a calendar widget
    cal = Calendar(calendar_window, selectmode='day')
    cal.pack(pady=20)

def open_files():
    # Create a new Toplevel window
    files_window = Toplevel()
    files_window.title("Open Files")
    files_window.geometry("290x130+10+10")  # Set width and height for the small window
    files_window.resizable(False, False)  # Prevent resizing

    # Function to open the file explorer
    def open_files_explorer():
        subprocess.run("explorer", shell=True)

    # Create a button to open the file explorer
    open_button = Button(files_window, text="Open File Explorer", command=open_files_explorer)
    open_button.pack(pady=20)

def open_settings():
    settings_window = Toplevel()
    settings_window.title("Settings")
    settings_window.geometry("300x200+10+470")  # Set width, height, and position
    settings_window.resizable(False, False)  # Prevent resizing

    # Wi-Fi
    wifi_state = False  # Default state
    def toggle_wifi():
        nonlocal wifi_state
        wifi_state = not wifi_state  # Toggle state
        if wifi_state:
            # Command to enable Wi-Fi (Windows)
            subprocess.run([" netsh", "interface", "set", "interface", "Wi-Fi", "enabled"])
            wifi_button.config(text="On")
        else:
            # Command to disable Wi-Fi (Windows)
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "disabled"])
            wifi_button.config(text="Off")

    wifi_frame = Frame(settings_window)
    wifi_frame.pack(pady=10)

    wifi_label = Label(wifi_frame, text="Wi-Fi:")
    wifi_label.pack(side=LEFT)

    wifi_button = Button(wifi_frame, text="Off", font=("Acumin variable concept", 12), command=toggle_wifi)
    wifi_button.pack(side=LEFT)

    # Bluetooth
    bluetooth_state = False  # Default state
    def toggle_bluetooth():
        nonlocal bluetooth_state
        bluetooth_state = not bluetooth_state  # Toggle state
        if bluetooth_state:
            # Command to enable Bluetooth (Windows)
            subprocess.run(["powershell", "-Command", "Get-PnpDevice -FriendlyName 'Bluetooth' | Enable-PnpDevice"])
            bluetooth_button.config(text="On")
        else:
            # Command to disable Bluetooth
            subprocess.run(["powershell", "-Command", "Get-PnpDevice -FriendlyName 'Bluetooth' | Disable-PnpDevice"])
            bluetooth_button.config(text="Off")

    bluetooth_frame = Frame(settings_window)
    bluetooth_frame.pack(pady=10)

    bluetooth_label = Label(bluetooth_frame, text="Bluetooth:")
    bluetooth_label.pack(side=LEFT)

    bluetooth_button = Button(bluetooth_frame, text="Off", font=("Acumin variable concept", 12), command=toggle_bluetooth)
    bluetooth_button.pack(side=LEFT)

# Example of how to create a button to open the settings window
settings_button = Button(RHB, text="Settings", command=open_settings)
settings_button.place(x=270, y=50)

def open_task_manager():
    task_window = Toplevel()
    task_window.title("Task Manager")
    task_window.geometry("300x350+1170+170")
    
    tasks = []

    task_entry = Entry(task_window, width=30)
    task_entry.pack(pady=10)

    def add_task():
        task = task_entry.get()
        if task:
            tasks.append(task)
            update_task_listbox()
            task_entry.delete(0, END)

    def delete_task():
        try:
            selected_task_index = task_listbox.curselection()[0]
            del tasks[selected_task_index]
            update_task_listbox()
        except IndexError:
            pass

    def update_task_listbox():
        task_listbox.delete(0, END)
        for task in tasks:
            task_listbox.insert(END, task)

    add_button = Button(task_window, text="Add Task", command=add_task)
    add_button.pack(pady=5)

    delete_button = Button(task_window, text="Delete Task", command=delete_task)
    delete_button.pack(pady=5)

    task_listbox = Listbox(task_window, width=50, height=10)
    task_listbox.pack(pady=10)

# Button images
weather_img = PhotoImage(file='weather.png')
clock_img = PhotoImage(file='clock.png')
calendar_img = PhotoImage(file='calendar.png')
settings_img = PhotoImage(file='settings.png')
ludo_img = PhotoImage(file='ludo.png')
camera_img = PhotoImage(file='camera.png')
files_img = PhotoImage(file='files.png')
google_img = PhotoImage(file='google.png')
tasks_img = PhotoImage(file='tasks.png')
tools_img = PhotoImage(file='tools.png')
tasks_img = PhotoImage(file='tasks.png')  # Load the task.png image

# Creating buttons with unified function
weather = Button(RHB, image=weather_img, bd=0, command=lambda: open_app("Weather"))
weather.place(x=15, y=50)

clock = Button(RHB, image=clock_img, bd=0, command=show_time)  # Clock button
clock.place(x=100, y=50)

calendar_button = Button(RHB, image=calendar_img, bd=0, command=open_calendar)  # Calendar button
calendar_button.place(x=185, y=50)

settings = Button(RHB, image=settings_img, bd=0, command=open_settings)  # Open settings window
settings.place(x=270, y=50)

ludo = Button(RHB, image=ludo_img, bd=0, command=lambda: open_app("Ludo"))
ludo.place(x=355, y=50)

camera = Button(RHB, image=camera_img, bd=0, command=lambda: open_app("Camera"))
camera.place(x=15, y=120)

files = Button(RHB, image=files_img, bd=0, command=open_files)  # Open file explorer
files.place(x=100, y=120)

google = Button(RHB, image=google_img, bd=0, command=open_google_search)  # Open Google search box
google.place(x=185, y=120)

tasks = Button(RHB, image=tasks_img, bd=0, command=open_task_manager)
tasks.place(x=270, y=120)

tools = Button(RHB, image=tools_img, bd=0, command=lambda: open_app("Tools"))
tools.place(x=355, y=120)

# Start the main loop
root.mainloop()
