from classes.master import Master
import csv


class AdditionalCodeDescription(Master):
    def __init__(self, elem, additional_code_type_id, additional_code, additional_code_sid, additional_code_description_period_sid):
        Master.__init__(self, elem)
        self.additional_code_description_period_sid = additional_code_description_period_sid
        self.additional_code_type_id = additional_code_type_id
        self.additional_code = additional_code
        self.additional_code_sid = additional_code_sid
        self.description = Master.process_null(elem.find("description"))
        self.language_id = Master.process_null(elem.find("language/languageId"))

    def __str__(self) -> str:
        return ""
