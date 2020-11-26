import csv
from classes.master import Master


class FootnoteAssociationGoodsNomenclature(Master):
    def __init__(self, elem, goods_nomenclature_item_id, goods_nomenclature_sid, productline_suffix):
        Master.__init__(self, elem)
        self.goods_nomenclature_item_id = goods_nomenclature_item_id
        self.goods_nomenclature_sid = goods_nomenclature_sid
        self.productline_suffix = productline_suffix
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
        self.footnote_type = Master.process_null(elem.find("footnote/footnoteType/footnoteTypeId"))
        self.footnote_id = Master.process_null(elem.find("footnote/footnoteId"))

    def __str__(self) -> str:
        return ""
