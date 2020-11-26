import csv

from classes.master import Master


class QuotaOrderNumberOriginExclusion(Master):
    def __init__(self, elem, quota_order_number_origin_sid):
        Master.__init__(self, elem)

        self.quota_order_number_origin_sid = quota_order_number_origin_sid
        self.excluded_geographical_area_sid = Master.process_null(elem.find("geographicalArea/sid"))

    def __str__(self) -> str:
        return ""
