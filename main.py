
import tkinter as tk
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry("500x500+450+150")
root.title("Productivity Tracker")

font_style = ("Times", 9)

# Start Time Label
start_time_label = tk.Label(root, text="Start Time:", font= font_style)
start_time_label.place(x=20, y=20)

# Start Time Entry Box
start_time_entry = tk.Entry(root, font= font_style)
start_time_entry.place(x=100, y=20)

# End Time Label
end_time_label = tk.Label(root, text="End Time:", font= font_style)
end_time_label.place(x=20, y=50)

# End Time Entry Box
end_time_entry = tk.Entry(root, font= font_style)
end_time_entry.place(x=100, y=50)

def exit_program():
    confirm_window = tk.Toplevel(root)
    confirm_window.geometry("300x100+500+200")
    confirm_window.title("Confirm Exit")

    confirm_label = tk.Label(confirm_window, text="Are you sure you want to exit?", font=font_style)
    confirm_label.pack(pady=10)

    yes_button = tk.Button(confirm_window, text="Yes", command=root.destroy, font=font_style)
    yes_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(confirm_window, text="No", command=confirm_window.destroy, font=font_style)
    no_button.pack(side=tk.RIGHT, padx=10)

exit_button = tk.Button(root, text="Exit", command=exit_program, font=font_style)
exit_button.place(x=20, y=300)

# Goals Label
def open_goal_window():
    goal_window = tk.Toplevel(root)
    goal_window.geometry("300x200+500+200")
    goal_window.title("Goals")

    goal_label = tk.Label(goal_window, text="Enter your goals:", font=font_style)
    goal_label.pack(pady=10)

    goal_entry = tk.Entry(goal_window, font=font_style)
    goal_entry.pack(pady=10)

    def submit_goal():
        goal = goal_entry.get()
        goal_display_label.config(text=goal)

    submit_button = tk.Button(goal_window, text="Submit", command=submit_goal, font=font_style)
    submit_button.pack(pady=10)

    goal_display_label = tk.Label(goal_window, text="", font=font_style)
    goal_display_label.pack(pady=10)


goals_button = tk.Button(root, text="Goals", command=open_goal_window, font=font_style)
goals_button.place(x=20, y=100)

# Reminder Label
def open_reminder_window():
    reminder_window = tk.Toplevel(root)
    reminder_window.geometry("300x200+500+200")
    reminder_window.title("Reminder")

    reminder_label = tk.Label(reminder_window, text="Enter your reminder:", font=font_style)
    reminder_label.pack(pady=10)

    reminder_entry = tk.Entry(reminder_window, font=font_style)
    reminder_entry.pack(pady=10)

    def submit_reminder():
        reminder = reminder_entry.get()
        reminder_display_label.config(text=reminder)

    submit_button = tk.Button(reminder_window, text="Submit", command=submit_reminder, font=font_style)
    submit_button.pack(pady=10)

    reminder_display_label = tk.Label(reminder_window, text="", font=font_style)
    reminder_display_label.pack(pady=10)


reminder_button = tk.Button(root, text="Reminder", command=open_reminder_window, font=font_style)
reminder_button.place(x=100, y=100)
def create_piechart():
    # Get the productivity value
    productivity_str = productivity_display_label.cget("text")
    productivity = float(productivity_str.split()[0])

    # Create the pie chart
    labels = ["Productive Time", "Unproductive Time"]
    sizes = [productivity, 24.0 - productivity]
    colors = ["green", "red"]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    ax.set_title("Productivity Chart")

    # Embed the chart in a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Create a window to display the canvas
    chart_window = tk.Toplevel(root)
    chart_window.geometry("400x400+550+200")
    chart_window.title("Productivity Chart")
    chart_window.protocol("WM_DELETE_WINDOW", canvas.get_tk_widget().destroy)
    chart_canvas = canvas.get_tk_widget()
    chart_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

productivity_label = tk.Label(root, text="Productivity:", font=font_style)
productivity_label.place(x=20, y=150)


productivity_display_label = tk.Label(root, text="", font=font_style)
productivity_display_label.place(x=100, y=150)

def calculate_productivity():
    print("calculate_productivity() function is being called")
    start_time_str = start_time_entry.get()
    end_time_str = end_time_entry.get()


    if start_time_str and end_time_str:
        start_time = datetime.datetime.strptime(start_time_str, "%H:%M")
        end_time = datetime.datetime.strptime(end_time_str, "%H:%M")
        time_diff = end_time - start_time
        productivity = round(time_diff.seconds / 60, 2)
        productivity_display_label.config(text=f"{productivity} minutes")
    else:
        productivity_display_label.config(text="Please enter valid start and end times")

calculate_productivity_button = tk.Button(root, text="Calculate Productivity", command=calculate_productivity, font=font_style)
calculate_productivity_button.place(x=20, y=200)
create_piechart_button = tk.Button(root, text="Create Chart", command=create_piechart, font=font_style)
create_piechart_button.place(x=20, y=250)

root.mainloop()