import csv
from classes.master import Master


class QuotaBalanceEvent(Master):

    def __init__(self, elem, quota_definition_sid):
        Master.__init__(self, elem)
        self.quota_definition_sid = quota_definition_sid
        self.imported_amount = Master.process_null(elem.find("importedAmount"))
        self.last_import_date_in_allocation = Master.process_null(elem.find("lastImportDateInAllocation"))
        self.new_balance = Master.process_null(elem.find("newBalance"))
        self.occurrence_timestamp = Master.process_null(elem.find("occurrenceTimestamp"))
        self.old_balance = Master.process_null(elem.find("oldBalance"))

    def __str__(self) -> str:
        return ""
