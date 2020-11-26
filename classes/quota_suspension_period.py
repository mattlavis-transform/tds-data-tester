import csv
from classes.master import Master


class QuotaSuspensionPeriod(Master):

    def __init__(self, elem, quota_definition_sid):
        Master.__init__(self, elem)
        self.quota_definition_sid = quota_definition_sid
        self.quota_suspension_period_sid = Master.process_null(elem.find("sid"))
        self.suspension_start_date = Master.process_null(elem.find("suspensionStartDate"))
        self.suspension_end_date = Master.process_null(elem.find("suspensionEndDate"))
        self.description = Master.process_null(elem.find("description"))

    def __str__(self) -> str:
        return ""
