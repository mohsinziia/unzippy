from zipfile import ZipFile


def unzip(src_path, dest_path):
  with ZipFile(src_path, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print("Extracting all the files...")
    zip.extractall(dest_path)
    print("Done")
