import csv
from classes.master import Master


class GoodsNomenclatureIndent(Master):

    def __init__(self, elem, goods_nomenclature_item_id, goods_nomenclature_sid, productline_suffix):
        Master.__init__(self, elem)
        self.goods_nomenclature_item_id = goods_nomenclature_item_id
        self.goods_nomenclature_sid = goods_nomenclature_sid
        self.goods_nomenclature_indent_sid = Master.process_null(elem.find("sid"))
        self.productline_suffix = productline_suffix
        self.number_indents = Master.process_null(elem.find("numberIndents"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))

    def __str__(self) -> str:
        return ""
