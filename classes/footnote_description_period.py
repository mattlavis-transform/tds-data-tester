import csv

from classes.master import Master
from classes.footnote_description import FootnoteDescription


class FootnoteDescriptionPeriod(Master):

    footnote_descriptions = []

    def __init__(self, elem, footnote_type_id, footnote_id):
        Master.__init__(self, elem)
        self.footnote_type_id = footnote_type_id
        self.footnote_id = footnote_id
        self.footnote_description_period_sid = Master.process_null(elem.find("sid"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))

        for elem in elem.findall('.//footnoteDescription'):
            self.footnote_descriptions.append(FootnoteDescription(elem, self.footnote_type_id, self.footnote_id, self.footnote_description_period_sid))

    def __str__(self) -> str:
        return ""
