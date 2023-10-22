import os

base_dir = os.path.join(os.path.expanduser("~"), "downloads")


def move(root_dir, destination_dir, file):
    source = os.path.join(root_dir, file)
    destination = os.path.join(destination_dir, file)
    os.rename(source, destination)


def organise_files2():
    directories = []
    all_items = os.listdir(base_dir)
    for item in all_items:
        if os.path.isdir(os.path.join(base_dir, item)):
            directories.append(item)
    for files in os.listdir(base_dir):
        file_extension = files.split(".")[-1]
        if file_extension not in directories:
            destination_dir = os.path.join(base_dir, file_extension)
            os.makedirs(destination_dir)
            move(base_dir, destination_dir, files)
        elif not os.path.isdir(os.path.join(base_dir, files)):
            destination_dir = os.path.join(base_dir, file_extension)
            move(base_dir, destination_dir, files)


organise_files2()
