import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        messagebox.showerror("Error", "Failed to open video file.")
        return
    
    # Get video properties
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Read all frames
    frame_list = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_list.append(frame)
    
    # Release capture once frames are read
    cap.release()
    
    # Write frames in reverse order
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for frame in reversed(frame_list):
        out.write(frame)
    
    # Release output and close windows
    out.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Info", "Video reversed successfully.")

def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def save_file(entry):
    file_path = filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("AVI files", "*.avi")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def start_reversing(input_entry, output_entry):
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select both input and output files.")
        return
    reverse_video(input_path, output_path)

# GUI setup
root = tk.Tk()
root.title("Video Reverser")

input_label = tk.Label(root, text="Input Video:")
input_label.grid(row=0, column=0, padx=10, pady=5)

input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)

input_button = tk.Button(root, text="Browse", command=lambda: browse_file(input_entry))
input_button.grid(row=0, column=2, padx=10, pady=5)

output_label = tk.Label(root, text="Output Video:")
output_label.grid(row=1, column=0, padx=10, pady=5)

output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)

output_button = tk.Button(root, text="Save As", command=lambda: save_file(output_entry))
output_button.grid(row=1, column=2, padx=10, pady=5)

reverse_button = tk.Button(root, text="Reverse Video", command=lambda: start_reversing(input_entry, output_entry))
reverse_button.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
