from classes.master import Master
import csv


class BaseRegulation(Master):
    def __init__(self, elem):
        Master.__init__(self, elem)
        self.base_regulation_role = Master.process_null(elem.find("regulationRoleType/regulationRoleTypeId"))
        self.base_regulation_id = Master.process_null(elem.find("baseRegulationId"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
        self.community_code = Master.process_null(elem.find("communityCode"))
        self.regulation_group_id = Master.process_null(elem.find("regulationGroup/regulationGroupId"))
        self.replacement_indicator = Master.process_null(elem.find("replacementIndicator"))
        self.stopped_flag = Master.process_null(elem.find("stoppedFlag"))
        self.information_text = Master.process_null(elem.find("informationText"))
        self.approved_flag = Master.process_null(elem.find("approvedFlag"))
        self.published_date = Master.process_null(elem.find("publishedDate"))
        self.officialjournal_number = Master.process_null(elem.find("officialjournalNumber"))
        self.officialjournal_page = Master.process_null(elem.find("officialjournalPage"))
        self.effective_end_date = Master.process_null(elem.find("effectiveEndDate"))
        self.antidumping_regulation_role = Master.process_null(elem.find("antidumpingRegulationRole"))
        self.related_antidumping_regulation_id = Master.process_null(elem.find("relatedAntidumpingRegulationId"))
        self.complete_abrogation_regulation_role = Master.process_null(elem.find("completeAbrogationRegulationRole"))
        self.complete_abrogation_regulation_id = Master.process_null(elem.find("explicitAbrogationRegulationRole"))
        self.explicit_abrogation_regulation_role = Master.process_null(elem.find("explicitAbrogationRegulationId"))
        self.explicit_abrogation_regulation_id = Master.process_null(elem.find("explicitAbrogationRegulationId"))

    def __str__(self) -> str:
        return ""
