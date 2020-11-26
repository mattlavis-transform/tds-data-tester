import os
from classes.document import Document


def main():
    folder = os.path.dirname(os.path.realpath(__file__))
    folder = os.path.join(folder, "xml")

    files = os.listdir(folder)
    files.sort()
    for filename in files:
        if "20201111T000000" in filename:
        # if "2020" in filename:
            if filename.endswith(".xml"):
                document = Document(filename)
                document.parse()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
