import csv
from classes.master import Master
from classes.quota_balance_event import QuotaBalanceEvent
from classes.quota_blocking_period import QuotaBlockingPeriod
from classes.quota_suspension_period import QuotaSuspensionPeriod


class QuotaDefinition(Master):

    quota_balance_events = []
    quota_blocking_periods = []
    quota_suspension_periods = []

    def __init__(self, elem):
        Master.__init__(self, elem)
        self.quota_definition_sid = Master.process_null(elem.find("sid"))
        self.quota_order_number_id = Master.process_null(elem.find("quotaOrderNumber/quotaOrderNumberId"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
        self.quota_order_number_sid = Master.process_null(elem.find("quotaOrderNumber/sid"))
        self.volume = Master.process_null(elem.find("volume"))
        self.initial_volume = Master.process_null(elem.find("initialVolume"))
        self.measurement_unit_code = Master.process_null(elem.find("measurementUnit/measurementUnitCode"))
        self.maximum_precision = Master.process_null(elem.find("maximumPrecision"))
        self.critical_state = Master.process_null(elem.find("criticalState"))
        self.critical_threshold = Master.process_null(elem.find("criticalThreshold"))
        self.monetary_unit_code = Master.process_null(elem.find("monetaryUnit/monetaryUnitCode"))
        self.measurement_unit_qualifier_code = Master.process_null(elem.find("measurementUnitQualifier/measurementUnitQualifierCode"))
        self.description = Master.process_null(elem.find("description"))

        # Get balance events
        for el in elem.findall('.//quotaBalanceEvent'):
            self.quota_balance_events.append(QuotaBalanceEvent(el, self.quota_definition_sid))

        # Get blocking periods
        for el in elem.findall('.//quotaBlockingPeriod'):
            self.quota_blocking_periods.append(QuotaBlockingPeriod(el, self.quota_definition_sid))

        # Get suspension periods
        for el in elem.findall('.//quotaSuspensionPeriod'):
            self.quota_suspension_periods.append(QuotaSuspensionPeriod(el, self.quota_definition_sid))

    def __str__(self) -> str:
        return ""
