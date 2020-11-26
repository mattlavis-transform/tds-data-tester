import csv

from classes.master import Master
from classes.additional_code_description_period import AdditionalCodeDescriptionPeriod


class AdditionalCode(Master):

    additional_code_description_periods = []

    def __init__(self, elem):
        Master.__init__(self, elem)
        self.additional_code_sid = Master.process_null(elem.find("sid"))
        self.additional_code = Master.process_null(elem.find("additionalCodeCode"))
        self.additional_code_type_id = Master.process_null(elem.find("additionalCodeType/additionalCodeTypeId"))

        for elem in elem.findall('.//additionalCodeDescriptionPeriod'):
            self.additional_code_description_periods.append(AdditionalCodeDescriptionPeriod(elem, self.additional_code_type_id, self.additional_code, self.additional_code_sid))

    def __str__(self) -> str:
        return ""
