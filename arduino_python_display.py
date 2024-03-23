import tkinter as tk
from tkinter import ttk
import serial
import time #Required to use delay functions
import threading
#Test

# Function to sort flight data by arrival time
def sort_by_arrival_time(data):
    return sorted(data, key=lambda x: x["arrival_time"])

# Function to sort flight data by flight name
def sort_by_flight_name(data):
    return sorted(data, key=lambda x: x["flight"])

# Function to create GUI
def create_gui():
    root = tk.Tk()
    root.title("Arduino Inputs")

    # Set up the title label
    title_label = tk.Label(root, text="Qn1. What is SIA?", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=1, pady=20)  # Add some padding around the title label

    # Create a frame to hold the boxes
    box_frame = tk.Frame(root)
    box_frame.grid(row=1, column=0)

    # Define the number of rows and columns
    rows = 3
    columns = 2

    # Dummy plane arrival data (can be replaced with actual data)
    plane_data = [
        {"flight": "SQ123", "arrival_time": "10:00 AM"},
        {"flight": "SQ456", "arrival_time": "11:30 AM"},
        {"flight": "SQ789", "arrival_time": "1:00 PM"},
        {"flight": "SQ246", "arrival_time": "2:30 PM"},
        {"flight": "SQ135", "arrival_time": "4:00 PM"},
        {"flight": "SQ579", "arrival_time": "5:30 PM"}
    ]

    # Create the boxes and display plane arrival data
    box_widgets = []
    for i in range(rows):
        for j in range(columns):
            Box_text = "True" if j == 0 else "False"
            box = tk.Label(box_frame, text=Box_text, bg="white", width=30, height=7, relief="solid", borderwidth=1, font=("Helvetica", 15))
            # Align the text to the right side
            box.grid(row=i, column=j, padx=10, pady=10, sticky="e")  # Add some padding around the boxes and align text to the right
            box_widgets.append(box)
            
    # Function to refresh treeview with sorted data
    def refresh_treeview(sort_key):
        tree.delete(*tree.get_children())
        if sort_key == "arrival_time_asc":
            sorted_data = sort_by_arrival_time(plane_data)
        elif sort_key == "arrival_time_desc":
            sorted_data = sort_by_arrival_time(plane_data)[::-1]
        elif sort_key == "flight_name":
            sorted_data = sort_by_flight_name(plane_data)
        for idx, data in enumerate(sorted_data, start=1):
            tree.insert("", "end", values=(idx, data["flight"], data["arrival_time"]))

    # Create a frame for the flight data table
    table_frame = tk.Frame(root)
    table_frame.grid(row=1, column=1, padx=20)

    # Create a treeview widget for displaying the flight data
    tree = ttk.Treeview(table_frame, columns=("Index", "Flight", "Arrival Time"), show="headings")
    tree.heading("Index", text="Index")
    tree.heading("Flight", text="Flight", command=lambda: refresh_treeview("flight_name"))
    tree.heading("Arrival Time", text="Arrival Time", command=lambda: refresh_treeview("arrival_time_asc"))
    tree.grid(row=0, column=0)

    # Insert flight data into the treeview
    refresh_treeview("arrival_time_asc")
    
    ser = serial.Serial('COM4', 9600)  # Adjust 'COM4' to your Arduino's serial port
    time.sleep(2)

    def arduino_handler():
        while True:
            data = ser.readline().decode().strip()
            if data == "L1":
                box_widgets[-2].config(bg="green")
            elif data == "L2":
                box_widgets[-4].config(bg="red")
            elif data == "R1":
                box_widgets[-1].config(bg="red")
            elif data == "R2":
                box_widgets[-3].config(bg="green")
            else:
                for i in box_widgets:
                    i.config(bg="white")

    threading.Thread(target=arduino_handler, daemon=True).start()
    
    # Timer
    timer_label = tk.Label(root, text="Timer: 00:00", font=("Helvetica", 12))
    timer_label.grid(row=2, column=0, pady=10)

    # Function to update timer
    def update_timer():
        elapsed_time = 0
        while True:
            mins, secs = divmod(elapsed_time, 60)
            timer_label.config(text=f"Timer: {mins:02d}:{secs:02d}")
            root.update()
            time.sleep(1)
            elapsed_time += 1

    # Start a separate thread to update timer
    timer_thread = threading.Thread(target=update_timer)
    timer_thread.daemon = True
    timer_thread.start()
    root.mainloop()

# Start the application
if __name__ == "__main__":
    create_gui()