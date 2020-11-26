from classes.measure_component import MeasureComponent
from classes.measure_condition import MeasureCondition
from classes.footnote_association_measure import FootnoteAssociationMeasure
from classes.master import Master
import csv


class Measure(Master):
    measure_components = []
    measure_conditions = []
    footnote_association_measures = []

    def __init__(self, elem=None):
        if elem is not None:
            Master.__init__(self, elem)
            self.measure_sid = Master.process_null(elem.find("sid"))
            self.measure_type_id = Master.process_null(elem.find("measureType/measureTypeId"))
            self.geographical_area_id = Master.process_null(elem.find("geographicalArea/geographicalAreaId"))
            self.goods_nomenclature_item_id = Master.process_null(elem.find("goodsNomenclature/goodsNomenclatureItemId"))
            self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
            self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
            self.measure_generating_regulation_role = Master.process_null(elem.find("measureGeneratingRegulationRole/regulationRoleTypeId"))
            self.measure_generating_regulation_id = Master.process_null(elem.find("measureGeneratingRegulationId"))
            self.justification_regulation_role = Master.process_null(elem.find("justificationRegulationRole/regulationRoleTypeId"))
            self.justification_regulation_id = Master.process_null(elem.find("justificationRegulationId"))
            self.stopped_flag = Master.process_null(elem.find("stoppedFlag"))
            self.geographical_area_sid = Master.process_null(elem.find("geographicalArea/sid"))
            self.goods_nomenclature_sid = Master.process_null(elem.find("goodsNomenclature/sid"))
            self.ordernumber = Master.process_null(elem.find("ordernumber"))
            self.additional_code_type_id = Master.process_null(elem.find("additionalCode/additionalCodeType/additionalCodeTypeId"))
            self.additional_code_id = Master.process_null(elem.find("additionalCode/additionalCodeCode"))
            self.additional_code_sid = Master.process_null(elem.find("additionalCode/sid"))
            self.reduction_indicator = Master.process_null(elem.find("reductionIndicator"))
            self.export_refund_nomenclature_sid = None

            for elem in elem.findall('.//measureComponent'):
                self.measure_components.append(MeasureComponent(elem, self.measure_sid))

            for elem in elem.findall('.//measureCondition'):
                self.measure_conditions.append(MeasureCondition(elem, self.measure_sid))

            for elem in elem.findall('.//footnoteAssociationMeasure'):
                self.footnote_association_measures.append(FootnoteAssociationMeasure(elem, self.measure_sid))

    def __str__(self) -> str:
        return ""
