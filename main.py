import os
from classes.document import Document


def main():
    folder = os.path.dirname(os.path.realpath(__file__))
    folder = os.path.join(folder, "xml")

    for filename in os.listdir(folder):
        if filename.endswith(".xml"):
            document = Document(filename)
            document.parse()
        else:
            continue

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
