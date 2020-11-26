import csv
from classes.master import Master


class QuotaBlockingPeriod(Master):

    def __init__(self, elem, quota_definition_sid):
        Master.__init__(self, elem)
        self.quota_definition_sid = quota_definition_sid
        self.quota_blocking_period_sid = Master.process_null(elem.find("sid"))
        self.blocking_start_date = Master.process_null(elem.find("blockingStartDate"))
        self.blocking_end_date = Master.process_null(elem.find("blockingEndDate"))
        self.blocking_period_type = Master.process_null(elem.find("blockingPeriodType"))
        self.description = Master.process_null(elem.find("description"))

    def __str__(self) -> str:
        return ""
