import csv

from classes.master import Master
from classes.goods_nomenclature_description_period import GoodsNomenclatureDescriptionPeriod
from classes.goods_nomenclature_indent import GoodsNomenclatureIndent
from classes.footnote_association_goods_nomenclature import FootnoteAssociationGoodsNomenclature


class GoodsNomenclature(Master):

    goods_nomenclature_description_periods = []
    goods_nomenclature_indents = []
    footnote_association_goods_nomenclatures = []

    def __init__(self, elem):
        Master.__init__(self, elem)
        self.goods_nomenclature_sid = Master.process_null(elem.find("sid"))
        self.goods_nomenclature_item_id = Master.process_null(elem.find("goodsNomenclatureItemId"))
        self.producline_suffix = Master.process_null(elem.find("produclineSuffix"))
        self.statistical_indicator = Master.process_null(elem.find("statisticalIndicator"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))

        # Get description periods
        for el in elem.findall('.//goodsNomenclatureDescriptionPeriod'):
            self.goods_nomenclature_description_periods.append(GoodsNomenclatureDescriptionPeriod(el, self.goods_nomenclature_item_id, self.goods_nomenclature_sid, self.producline_suffix))

        # Get indents
        for el in elem.findall('.//goodsNomenclatureIndents'):
            self.goods_nomenclature_indents.append(GoodsNomenclatureIndent(el, self.goods_nomenclature_item_id, self.goods_nomenclature_sid, self.producline_suffix))

        # Get footnote associations
        for el in elem.findall('.//footnoteAssociationGoodsNomenclature'):
            self.footnote_association_goods_nomenclatures.append(FootnoteAssociationGoodsNomenclature(el, self.goods_nomenclature_item_id, self.goods_nomenclature_sid, self.producline_suffix))

    def __str__(self) -> str:
        return ""
