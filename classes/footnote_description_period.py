from classes.master import Master
import csv


class FootnoteDescriptionPeriod(Master):
    def __init__(self, elem, footnote_type_id, footnote_id):
        Master.__init__(self, elem)
        self.footnote_type_id = footnote_type_id
        self.footnote_id = footnote_id
        self.footnote_description_period_sid = Master.process_null(elem.find("sid"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))

    def __str__(self) -> str:
        return ""
