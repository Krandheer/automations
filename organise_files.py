import os

base_dir = os.path.join(os.path.expanduser("~"), "downloads")


def move(root_dir, destination_dir, file):
    """
    move files from source to destination using rename function
    """
    source = os.path.join(root_dir, file)
    destination = os.path.join(destination_dir, file)
    os.rename(source, destination)


def organise_file():
    """
    find the file to be moved/organised
    """
    images = ["jpeg", "jpg", "png"]
    for files in os.listdir(base_dir):
        file_extension = files.split(".")[-1]
        if file_extension in images:
            images_dir = os.path.join(base_dir, "images")
            if not os.path.isdir(images_dir):
                os.makedirs(images_dir)
            move(base_dir, images_dir, files)

        elif file_extension in ["epub", "pdf"]:
            books_and_docs = os.path.join(base_dir, f"{file_extension}s")
            if not os.path.isdir(books_and_docs):
                os.makedirs(books_and_docs)
            move(base_dir, books_and_docs, files)

        elif file_extension == "mp4":
            videos_dir = os.path.join(base_dir, "videos")
            if not os.path.isdir(videos_dir):
                os.makedirs(videos_dir)
            move(base_dir, videos_dir, files)


organise_file()
