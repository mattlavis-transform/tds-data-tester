import csv

from classes.master import Master
from classes.additional_code_description import AdditionalCodeDescription


class AdditionalCodeDescriptionPeriod(Master):

    additional_code_descriptions = []

    def __init__(self, elem, additional_code_type_id, additional_code, additional_code_sid):
        Master.__init__(self, elem)
        self.additional_code_type_id = additional_code_type_id
        self.additional_code = additional_code
        self.additional_code_sid = additional_code_sid
        self.additional_code_description_period_sid = Master.process_null(elem.find("sid"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))

        for elem in elem.findall('.//additionalCodeDescription'):
            self.additional_code_descriptions.append(AdditionalCodeDescription(elem, self.additional_code_type_id, self.additional_code, self.additional_code_sid, self.additional_code_description_period_sid))

    def __str__(self) -> str:
        return ""
