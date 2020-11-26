import csv

from classes.master import Master
from classes.goods_nomenclature_description import GoodsNomenclatureDescription


class GoodsNomenclatureDescriptionPeriod(Master):

    goods_nomenclature_descriptions = []

    def __init__(self, elem, goods_nomenclature_item_id, goods_nomenclature_sid, productline_suffix):
        Master.__init__(self, elem)
        self.goods_nomenclature_item_id = goods_nomenclature_item_id
        self.goods_nomenclature_sid = goods_nomenclature_sid
        self.productline_suffix = productline_suffix
        self.goods_nomenclature_description_period_sid = Master.process_null(elem.find("sid"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))

        for elem in elem.findall('.//goodsNomenclatureDescription'):
            self.goods_nomenclature_descriptions.append(GoodsNomenclatureDescription(elem, self.goods_nomenclature_item_id, self.goods_nomenclature_sid, self.goods_nomenclature_description_period_sid, self.productline_suffix))

    def __str__(self) -> str:
        return ""
