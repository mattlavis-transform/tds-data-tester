import csv

from classes.master import Master
from classes.quota_order_number_origin_exclusion import QuotaOrderNumberOriginExclusion


class QuotaOrderNumberOrigin(Master):

    quota_order_number_origin_exclusions = []

    def __init__(self, elem, quota_order_number_sid):
        Master.__init__(self, elem)

        self.quota_order_number_sid = quota_order_number_sid
        self.quota_order_number_origin_sid = Master.process_null(elem.find("sid"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
        self.geographical_area_id = Master.process_null(elem.find("geographicalArea/geographicalAreaId"))
        self.geographical_area_sid = Master.process_null(elem.find("geographicalArea/sid"))

        # Get origin exlusions
        for el in elem.findall('.//quotaOrderNumberOriginExclusion'):
            self.quota_order_number_origin_exclusions.append(QuotaOrderNumberOriginExclusion(el, self.quota_order_number_origin_sid))

    def __str__(self) -> str:
        return ""
