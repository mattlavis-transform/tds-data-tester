from classes.master import Master
import csv


class GoodsNomenclatureDescription(Master):
    def __init__(self, elem, goods_nomenclature_item_id, goods_nomenclature_sid, goods_nomenclature_description_period_sid, productline_suffix):
        Master.__init__(self, elem)
        self.goods_nomenclature_description_period_sid = goods_nomenclature_description_period_sid
        self.goods_nomenclature_item_id = goods_nomenclature_item_id
        self.goods_nomenclature_sid = goods_nomenclature_sid
        self.productline_suffix = productline_suffix
        self.description = Master.process_null(elem.find("description"))
        self.language_id = Master.process_null(elem.find("language/languageId"))

    def __str__(self) -> str:
        return ""
