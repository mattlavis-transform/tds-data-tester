import csv

from classes.master import Master
from classes.footnote_description_period import FootnoteDescriptionPeriod


class Certificate(Master):

    certificate_description_periods = []

    def __init__(self, elem):
        Master.__init__(self, elem)
        self.certificate_code = Master.process_null(elem.find("certificateCode"))
        self.certificate_type_code = Master.process_null(elem.find("certificateType/certificateTypeCode"))

        for elem in elem.findall('.//certificateDescriptionPeriod'):
            self.certificate_description_periods.append(CertificateDescriptionPeriod(elem, self.certificate_type_code, self.certificate_code))

    def __str__(self) -> str:
        return ""
