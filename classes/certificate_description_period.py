import csv

from classes.master import Master
from classes.certificate_description import CertificateDescription


class CertificateDescriptionPeriod(Master):

    certificate_descriptions = []

    def __init__(self, elem, certificate_type_code, certificate_code):
        Master.__init__(self, elem)
        self.certificate_type_code = certificate_type_code
        self.certificate_code = certificate_code
        self.certificate_description_period_sid = Master.process_null(elem.find("sid"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))

        for elem in elem.findall('.//certificateDescription'):
            self.certificate_descriptions.append(CertificateDescription(elem, self.certificate_type_code, self.certificate_code, self.certificate_description_period_sid))

    def __str__(self) -> str:
        return ""
