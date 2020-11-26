import csv

from classes.master import Master
from classes.footnote_description_period import FootnoteDescriptionPeriod


class Footnote(Master):

    footnote_description_periods = []

    def __init__(self, elem):
        Master.__init__(self, elem)
        self.footnote_id = Master.process_null(elem.find("footnoteId"))
        self.footnote_type_id = Master.process_null(elem.find("footnoteType/footnoteTypeId"))

        for elem in elem.findall('.//footnoteDescriptionPeriod'):
            self.footnote_description_periods.append(FootnoteDescriptionPeriod(elem, self.footnote_type_id, self.footnote_id))


    def __str__(self) -> str:
        return ""
