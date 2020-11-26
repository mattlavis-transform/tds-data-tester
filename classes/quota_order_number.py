import csv

from classes.master import Master
from classes.quota_order_number_origin import QuotaOrderNumberOrigin


class QuotaOrderNumber(Master):

    quota_order_number_origins = []

    def __init__(self, elem):
        Master.__init__(self, elem)
        self.quota_order_number_sid = Master.process_null(elem.find("sid"))
        self.quota_order_number_id = Master.process_null(elem.find("quotaOrderNumberId"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))

        # Get origins
        for el in elem.findall('.//quotaOrderNumberOrigin'):
            self.quota_order_number_origins.append(QuotaOrderNumberOrigin(el, self.quota_order_number_sid))

    def __str__(self) -> str:
        return ""
