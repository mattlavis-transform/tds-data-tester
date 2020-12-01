from config import config
from classes.goods_nomenclature import GoodsNomenclature
from classes.additional_code import AdditionalCode
import csv, os
import psycopg2
import glob
import datetime
import xml.etree.ElementTree as ET

from classes.measure_component import MeasureComponent
from classes.base_regulation import BaseRegulation
from classes.measure import Measure
from classes.measure_condition import MeasureCondition
from classes.footnote import Footnote
from classes.footnote_description_period import FootnoteDescriptionPeriod
from classes.certificate import Certificate
from classes.certificate_description_period import CertificateDescriptionPeriod
from classes.additional_code import AdditionalCode
from classes.additional_code_description_period import AdditionalCodeDescriptionPeriod
from classes.goods_nomenclature import GoodsNomenclature
from classes.goods_nomenclature_description_period import GoodsNomenclatureDescriptionPeriod
from classes.quota_order_number import QuotaOrderNumber
from classes.quota_order_number_origin import QuotaOrderNumberOrigin
from classes.quota_definition import QuotaDefinition



class Document(object):

    base_regulations = []
    measures = []
    footnotes = []
    certificates = []
    additional_codes = []
    goods_nomenclatures = []
    quota_order_numbers = []
    quota_definitions = []

    def __init__(self, file):
        self.file = file

    def parse(self):
        Measure.measure_components = []
        self.date = self.file[7: 15]
        root_node = ET.parse(self.get_path(self.file))
        # Get base regulations
        for elem in root_node.findall('.//BaseRegulation'):
            self.base_regulations.append (BaseRegulation(elem))
        
        # Get measures and their children
        for elem in root_node.findall('.//Measure'):
            self.measures.append (Measure(elem))

        # Get footnotes
        for elem in root_node.findall('.//findFootnoteByDatesResponse/Footnote'):
            self.footnotes.append (Footnote(elem))

        # Get additional codes
        for elem in root_node.findall('.//findAdditionalCodeByDatesResponse/AdditionalCode'):
            self.additional_codes.append (AdditionalCode(elem))

        # Get goods nomenclatures
        for elem in root_node.findall('.//findGoodsNomenclatureByDatesResponse/GoodsNomenclature'):
            self.goods_nomenclatures.append (GoodsNomenclature(elem))

        # Get quota order numbers
        for elem in root_node.findall('.//QuotaOrderNumber'):
            self.quota_order_numbers.append (QuotaOrderNumber(elem))

        # Get quota definitions
        for elem in root_node.findall('.//QuotaDefinition'):
            self.quota_definitions.append (QuotaDefinition(elem))

        print("Processing XML file from " + self.date)

        self.write_records()

    def write_records(self):
        self.make_folders()

        # Regulations
        self.write(self.base_regulations, "base_regulations.csv")

        # Measures
        self.write(self.measures, "measures.csv")
        self.write(Measure.measure_components, "measure_components.csv")
        self.write(Measure.measure_components, "measure_conditions.csv")
        self.write(MeasureCondition.measure_condition_components, "measure_condition_components.csv")
        self.write(Measure.footnote_association_measures, "footnote_association_measures.csv")
        self.write(Measure.measure_excluded_geographical_areas, "measure_excluded_geographical_areas.csv")

        # Footnotes
        self.write(self.footnotes, "footnotes.csv")
        self.write(Footnote.footnote_description_periods, "footnote_description_periods.csv")
        self.write(FootnoteDescriptionPeriod.footnote_descriptions, "footnote_descriptions.csv")

        # Certificates
        self.write(self.certificates, "certificates.csv")
        self.write(Certificate.certificate_description_periods, "certificate_description_periods.csv")
        self.write(CertificateDescriptionPeriod.certificate_descriptions, "certificate_descriptions.csv")

        # Additional codes
        self.write(self.additional_codes, "additional_codes.csv")
        self.write(AdditionalCode.additional_code_description_periods, "additional_code_description_periods.csv")
        self.write(AdditionalCodeDescriptionPeriod.additional_code_descriptions, "additional_code_descriptions.csv")

        # Goods nomenclatures
        self.write(self.goods_nomenclatures, "goods_nomenclatures.csv")
        self.write(GoodsNomenclature.footnote_association_goods_nomenclatures, "footnote_association_goods_nomenclatures.csv")
        self.write(GoodsNomenclature.goods_nomenclature_description_periods, "goods_nomenclature_description_periods.csv")
        self.write(GoodsNomenclature.goods_nomenclature_indents, "goods_nomenclature_indents.csv")
        self.write(GoodsNomenclatureDescriptionPeriod.goods_nomenclature_descriptions, "goods_nomenclature_descriptions.csv")

        # Quota order numbers
        self.write(self.quota_order_numbers, "quota_order_numbers.csv")
        self.write(QuotaOrderNumber.quota_order_number_origins, "quota_order_number_origins.csv")
        self.write(QuotaOrderNumberOrigin.quota_order_number_origin_exclusions, "quota_order_number_origin_exclusions.csv")

        # Quota definitions
        self.write(self.quota_definitions, "quota_definitions.csv")
        self.write(QuotaDefinition.quota_balance_events, "quota_balance_events.csv")
        self.write(QuotaDefinition.quota_blocking_periods, "quota_blocking_periods.csv")
        self.write(QuotaDefinition.quota_suspension_periods, "quota_suspension_periods.csv")

    def write(self, obj, filename):
        path = os.path.join(self.subfolder, filename)
        with open(path, 'w', newline='') as f:
            if len(obj) > 0:
                w = csv.DictWriter(f, fieldnames=vars(obj[0]), quoting=csv.QUOTE_MINIMAL)
                w.writeheader()
                for item in obj:
                    w.writerow({k: getattr(item, k) for k in vars(item)})

    def make_folders(self, folder_name='csv'):
        csv_path = os.path.join(self.root, folder_name)
        if not(os.path.isdir(csv_path)):
            os.mkdir(csv_path)
        self.subfolder = os.path.join(csv_path, self.date)
        if not(os.path.isdir(self.subfolder)):
            os.mkdir(self.subfolder)
    
    def get_path(self, file):
        self.root = os.path.dirname(os.path.realpath(__file__))
        self.root = os.path.join(self.root, "..")
        self.root = os.path.realpath(self.root)
        path = os.path.join(self.root, "xml")
        path = os.path.join(path, file)
        return path

    def generate_diff_report(self, date_as_string):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
        
            # create a cursor
            cur = conn.cursor()
            
            # analyze the files
            self.export_db_data_to_csv(cur, 'csv', date_as_string)
          
            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def export_db_data_to_csv(self, cur, folder, subfolder):
        csvs_path = os.path.join(self.root, folder, subfolder, "*.csv")
        self.make_folders('db_data')
        db_data_path = os.path.join(self.root, "db_data", subfolder)
        print("Analyzing files:")

        for fname in glob.glob(csvs_path):
            basename = os.path.basename(fname)
            print(f" - {basename}...")
            with open(fname) as f:
                file_lines = f.readlines()
                if file_lines:
                    fields = file_lines[0]
                    table_name = f"{basename[:-4]}_oplog"
                    f = open(f"{db_data_path}/{basename}", "w")
                    if fields:
                        f.write(fields)
                        try:
                            # BitZesty had made it easy for us to detect which record comes from which file by attaching the filename field to every table
                            cur.execute(f"SELECT {fields} from {table_name} where filename LIKE '%{subfolder}%'")
                            data = cur.fetchall()
                            for row in data:
                              data_line = ""
                              for x in row:
                                  if isinstance(x, datetime.datetime):
                                      x = x.strftime('%Y-%m-%dT%H:%M:%S')
                                  elif x is None:
                                      x = ''
                                  elif x == True:
                                      x = '1'
                                  elif x == False:
                                      x = '0'
                                  data_line+=str(x) + ','
                              f.write(data_line[:-1]+"\n")
                        except (Exception, psycopg2.DatabaseError) as error:
                            f.write(str(error)+"\n")
                            f.close()
                            cur.execute("rollback")
                        finally:
                            f.close()

                    