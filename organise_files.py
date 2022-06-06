import os

base_dir = os.path.join(os.path.expanduser("~"), "downloads")


def move(root_dir, destination_dir, file):
    source = os.path.join(root_dir, file)
    destination = os.path.join(destination_dir, file)
    os.rename(source, destination)


def organise_file():
    for files in os.listdir(base_dir):
        if files.endswith(".jpeg") or files.endswith(".jpg") or files.endswith(".png"):
            images_dir = os.path.join(base_dir, "images")
            if not os.path.isdir(images_dir):
                os.makedirs(images_dir)
            move(base_dir, images_dir, files)

        elif files.endswith(".pdf"):
            pdf_dir = os.path.join(base_dir, "pdfs")
            if not os.path.isdir(pdf_dir):
                os.makedirs(pdf_dir)
            move(base_dir, pdf_dir, files)

        elif files.endswith(".epub"):
            pdf_dir = os.path.join(base_dir, "epubs")
            if not os.path.isdir(pdf_dir):
                os.makedirs(pdf_dir)
            move(base_dir, pdf_dir, files)

        elif files.endswith(".mp4"):
            videos_dir = os.path.join(base_dir, "videos")
            if not os.path.isdir(videos_dir):
                os.makedirs(videos_dir)
            move(base_dir, videos_dir, files)


organise_file()
