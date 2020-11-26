from classes.master import Master
import csv


class FootnoteAssociationMeasure(Master):
    def __init__(self, elem, sid):
        Master.__init__(self, elem)
        self.measure_sid = sid
        self.footnote_type_id = Master.process_null(elem.find("footnote/footnoteType/footnoteTypeId"))
        self.footnote_id = Master.process_null(elem.find("footnote/footnoteId"))

    def __str__(self) -> str:
        return ""
