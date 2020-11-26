from classes.master import Master
import csv


class MeasureCondition(Master):
    def __init__(self, elem, sid):
        Master.__init__(self, elem)
        self.measure_condition_sid = Master.process_null(elem.find("sid"))
        self.measure_sid = sid
        self.condition_code = Master.process_null(elem.find("measureConditionCode/conditionCode"))
        self.component_sequence_number = Master.process_null(elem.find("conditionSequenceNumber"))
        self.condition_duty_amount = Master.process_null(elem.find("conditionDutyAmount"))
        self.condition_monetary_unit_code = Master.process_null(elem.find("monetaryUnit.monetaryUnitCode"))
        self.condition_measurement_unit_code = Master.process_null(elem.find("measurementUnit.measurementUnitCode"))
        self.condition_measurement_unit_qualifier_code = Master.process_null(elem.find("measurementUnitQualifier.measurementUnitQualifierCode"))
        self.action_code = Master.process_null(elem.find("measureAction/actionCode"))
        self.certificate_type_code = Master.process_null(elem.find("certificate/certificateType/certificateTypeCode"))
        self.certificate_code = Master.process_null(elem.find("certificate/certificateCode"))

    def __str__(self) -> str:
        return ""
