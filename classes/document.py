import csv, os
import xml.etree.ElementTree as ET

from classes.measure_component import MeasureComponent
from classes.base_regulation import BaseRegulation
from classes.measure import Measure
from classes.footnote import Footnote


class Document(object):

    base_regulations = []
    measures = []
    footnotes = []

    def __init__(self, file):
        self.file = file

    def parse(self):
        Measure.measure_components = []
        self.date = self.file[7: 15]
        root_node = ET.parse(self.get_path(self.file))
        # Get base regulations
        for elem in root_node.findall('.//BaseRegulation'):
            self.base_regulations.append (BaseRegulation(elem))
        
        # Get measures and their children
        for elem in root_node.findall('.//Measure'):
            self.measures.append (Measure(elem))

        # Get footnotes
        for elem in root_node.findall('.//findFootnoteByDatesResponse/Footnote'):
            self.footnotes.append (Footnote(elem))

        print("Processing XML file from " + self.date)

        self.write_records()

    def write_records(self):
        self.make_folders()
        self.write(self.base_regulations, "base_regulations.csv")
        self.write(self.measures, "measures.csv")
        self.write(Measure.measure_components, "measure_components.csv")
        self.write(Measure.measure_components, "measure_conditions.csv")
        self.write(Measure.footnote_association_measures, "footnote_association_measures.csv")
        self.write(self.footnotes, "footnotes.csv")
        self.write(Footnote.footnote_description_periods, "footnote_description_periods.csv")

    def write(self, obj, filename):
        path = os.path.join(self.subfolder, filename)
        with open(path, 'w', newline='') as f:
            if len(obj) > 0:
                w = csv.DictWriter(f, fieldnames=vars(obj[0]))
                w.writeheader()
                for item in obj:
                    w.writerow({k: getattr(item, k) for k in vars(item)})

    def make_folders(self):
        csv_path = os.path.join(self.root, "csv")
        if not(os.path.isdir(csv_path)):
            os.mkdir(csv_path)
        self.subfolder = os.path.join(csv_path, self.date)
        if not(os.path.isdir(self.subfolder)):
            os.mkdir(self.subfolder)
    
    def get_path(self, file):
        self.root = os.path.dirname(os.path.realpath(__file__))
        self.root = os.path.join(self.root, "..")
        self.root = os.path.realpath(self.root)
        path = os.path.join(self.root, "xml")
        path = os.path.join(path, file)
        return path
