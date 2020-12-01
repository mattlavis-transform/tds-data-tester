from classes.master import Master
import csv


class MeasureExcludedGeographicalArea(Master):
    def __init__(self, elem, sid):
        Master.__init__(self, elem)
        self.measure_sid = sid
        self.excluded_geographical_area = Master.process_null(elem.find("geographicalArea/geographicalAreaId"))
        self.geographical_area_sid = Master.process_null(elem.find("geographicalArea/sid"))

    def __str__(self) -> str:
        return ""
