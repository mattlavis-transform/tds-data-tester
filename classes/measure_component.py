from classes.master import Master
import csv


class MeasureComponent(Master):
    def __init__(self, elem, sid):
        Master.__init__(self, elem)
        self.measure_sid = sid
        self.duty_expression_id = Master.process_null(elem.find("dutyExpression/dutyExpressionId"))
        self.duty_amount = Master.process_null(elem.find("dutyAmount"))
        self.monetary_unit_code = Master.process_null(elem.find("monetaryUnit/monetaryUnitCode"))
        self.measurement_unit_code = Master.process_null(elem.find("measurementUnit/measurementUnitCode"))
        self.measurement_unit_qualifier_code = Master.process_null(elem.find("measurementUnitQualifier/measurementUnitQualifierCode"))

    def __str__(self) -> str:
        return ""
