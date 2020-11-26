from classes.master import Master
import csv


class CertificateDescription(Master):
    def __init__(self, elem, certificate_type_code, certificate_code, certificate_description_period_sid):
        Master.__init__(self, elem)
        self.certificate_description_period_sid = certificate_description_period_sid
        self.certificate_type_code = certificate_type_code
        self.certificate_code = certificate_code
        self.description = Master.process_null(elem.find("description"))
        self.language_id = Master.process_null(elem.find("language/languageId"))

    def __str__(self) -> str:
        return ""
