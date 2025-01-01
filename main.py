import tkinter as tk
from tkinter import filedialog
import os
from unzip import unzip

def main():
  class Component:
    def __init__(self, root, button_text, label_text):
        self.frame = tk.Frame(root, padx=0, pady=20)
        self.frame.columnconfigure(0, weight=1)
        self.path = tk.StringVar()
        self.button = tk.Button(self.frame, text=button_text, command=self.open_dialog, background="blue", font=('Arial', 20))
        self.button.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.path_label = tk.Label(self.frame, text=label_text, font=('Arial', 14), background="green")
        self.path_label.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.frame.pack()

  class SourceFile(Component):
      def __init__(self, root):
          super().__init__(root, "Open Source File", "Source File: ")
      
      def open_dialog(self):
          self.path.set(filedialog.askopenfilename(defaultextension=".zip", filetypes=[("Zip Files", "*.zip")], initialdir="D:\Mohsin's Stuff\Downloads", title="Select a file"))
          self.path_label.config(text=f"Source File: {os.path.basename(self.path.get())}")

  class DestinationFolder(Component):
      def __init__(self, root):
          super().__init__(root, "Open Destination Folder", "Destination Folder Path: ")

      def open_dialog(self):
          self.path.set(filedialog.askdirectory(initialdir="D:\Mohsin's Stuff\Downloads", title="Select a folder"))
          self.path_label.config(text=f"Destination Folder Path: {self.path.get()}")

  class UnzipFile:
      def __init__(self, root, source_file, destination_path):
          self.source_file = source_file
          self.destination_path = destination_path
          self.button = tk.Button(root, text="Unzip File", comman=self.unzip_file, font=('Arial', 18))
          self.button.pack()
          self.label = tk.Label(root, text="", font=('Arial', 14))
          self.label.pack()
      
      def unzip_file(self):
          unzipped_path = self.destination_path.path.get() + "/" + os.path.basename(self.source_file.path.get())[0:-4]
          print(unzipped_path)
          if os.path.isdir(unzipped_path):
              self.label.config(text="Unzipped folder already exists at destination folder path", foreground="red")
              return

          if self.source_file.path.get() and self.destination_path.path.get():
              unzip(self.source_file.path.get(), self.destination_path.path.get())
              self.label.config(text="File unzipped successfully", foreground='green')
              print("File unzipped successfully")
          else:
              self.label.config(text="Please select source file and destination folder path", foreground="red")
              print("Please select source file and destination folder path")

  root = tk.Tk()
  root.title("File List Viewer")

  root.geometry("1000x300")
  root.resizable(True, False)

  source_file = SourceFile(root)
  destination_path = DestinationFolder(root)
  unzip_file = UnzipFile(root, source_file, destination_path)


  root.mainloop()
