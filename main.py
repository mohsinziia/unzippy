import os
import os.path
from unzip import unzip
import customtkinter as ctk
from customtkinter import filedialog
import tkinter as tk

source_file_path = ""
destination_folder_path = ""

def changePathName(list: tk.Listbox, path: str):
  list.insert(0, path)
  list.delete(first=1, last=1)

def selectSourceFile(list: tk.Listbox):
  global source_file_path
  source_file_path = filedialog.askopenfilename(defaultextension=".zip", filetypes=[("Zip Files", "*.zip")], initialdir="D:\Mohsin's Stuff\Downloads", title="Select a file")
  changePathName(list, os.path.basename(source_file_path))

def selectDestinationFolder(list: tk.Listbox):
  global destination_folder_path
  destination_folder_path = filedialog.askdirectory(initialdir="D:\Mohsin's Stuff\Downloads", title="Select a folder")
  changePathName(list, os.path.basename(destination_folder_path))

def unzip_file(label: ctk.CTkLabel, option):
  # 1 => Create new folder with same name as the zip file and extract the contents into that folder
  # 2 => Directly extract all the files
  extract_to_folder = option == 1

  print("unzipping")
  unzipped_path = destination_folder_path + "/" + os.path.basename(source_file_path)[0:-4]
  print(unzipped_path)

  if not source_file_path or not destination_folder_path:
      label.configure(text="Please select source file and destination folder path", text_color="red")
      print("Please select source file and destination folder path")
      return

  if os.path.isdir(unzipped_path):
      print(f"Source file path: {source_file_path}")
      label.configure(text="Unzipped folder already exists at destination folder path", text_color="red")
      return
  if extract_to_folder:
    unzip(source_file_path, unzipped_path)
  else:
    unzip(source_file_path, destination_folder_path)
    
  label.configure(text="File unzipped successfully", text_color="green")
  print("File unzipped successfully")



def main():
  DARK_COLOR = "#191922"
  ACCENT_COLOR = "#5D3FD3"

  app = ctk.CTk(fg_color=DARK_COLOR)
  app.geometry("800x500")
  app.resizable(width=False, height=False)
  font_family="Arial Rounded MT Bold"

  unzippy_label = ctk.CTkLabel(master=app, width=400, height=50, text_color="white", font=ctk.CTkFont(family=font_family, size=40))
  unzippy_label.pack(pady=40)

  frame = ctk.CTkFrame(master=app, fg_color=DARK_COLOR, width=500, height=150)
  frame.grid_propagate(False)
  frame.columnconfigure(0, weight=0)
  
  source_file_listbox = tk.Listbox(master=frame, height=1, border=0, font=(font_family, 20))
  source_file_listbox.grid(row=0, column=1, sticky=tk.W + tk.E)
  
  source_file_button = ctk.CTkButton(master=frame, text="Source File", fg_color=ACCENT_COLOR, corner_radius=20, height=40, text_color="white", cursor="hand2", font=(font_family, 20), command=lambda : selectSourceFile(source_file_listbox))
  source_file_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx=6)

  spacer1 = tk.Label(frame, text="", bg=DARK_COLOR, height=3)
  spacer1.grid(row=1, column=0)

  destination_folder_listbox = tk.Listbox(master=frame, height=1, border=0, font=(font_family, 20))
  destination_folder_listbox.grid(row=2, column=1, sticky=tk.W + tk.E)

  destination_folder_button = ctk.CTkButton(master=frame, text="Destination Folder", fg_color=ACCENT_COLOR, text_color='white', corner_radius=20, cursor="hand2", height=40, font=(font_family, 20), command=lambda : selectDestinationFolder(destination_folder_listbox))
  destination_folder_button.grid(row=2, column=0, sticky=tk.W+tk.E, padx=6)
  

  frame.pack(pady=(0, 20))
  options_frame = ctk.CTkFrame(app, bg_color=DARK_COLOR, fg_color=DARK_COLOR)
  options_frame.columnconfigure(0, weight=1)
  radio_var = tk.IntVar(master=options_frame, value=0)

  def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

  radiobutton_1 = ctk.CTkRadioButton(master=options_frame, text="Extract to folder",text_color="white", bg_color=DARK_COLOR, font=(font_family, 20), command=radiobutton_event, variable= radio_var, value=1)
  radiobutton_2 = ctk.CTkRadioButton(master=options_frame, text="Extract files",text_color="white", bg_color=DARK_COLOR, font=(font_family, 20),command=radiobutton_event, variable= radio_var, value=2)

  radiobutton_1.grid(row=0, column=0, sticky=ctk.E + ctk.W, pady=(0,20))
  radiobutton_2.grid(row=1, column=0, sticky=ctk.E + ctk.W,)
  options_frame.pack()


  unzip_status_label = ctk.CTkLabel(master=app, text_color=DARK_COLOR, padx=10, pady=10, font=(font_family, 20))
  unzip_status_label.pack()

  unzip_button = ctk.CTkButton(master=app, text="Unzip", fg_color=ACCENT_COLOR, corner_radius=20, height=40, text_color="white", cursor="hand2", font=(font_family, 20), command=lambda: unzip_file(unzip_status_label, radio_var.get()))
  unzip_button.pack()

  app.mainloop()
