from classes.master import Master
import csv


class FootnoteDescription(Master):
    def __init__(self, elem, footnote_type_id, footnote_id, footnote_description_period_sid):
        Master.__init__(self, elem)
        self.footnote_description_period_sid = footnote_description_period_sid
        self.footnote_type_id = footnote_type_id
        self.footnote_id = footnote_id
        self.description = Master.process_null(elem.find("description"))
        self.language_id = Master.process_null(elem.find("language/languageId"))

    def __str__(self) -> str:
        return ""
