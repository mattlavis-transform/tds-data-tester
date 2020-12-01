class Master(object):
    def __init__(self, elem):

        self.operation = elem.find("metainfo/opType").text
        # self.national = 1 if elem.find("metainfo/origin").text == "N" else 0
        # self.hjid = elem.find("hjid").text
        # self.operation_date = "2021-01-01"
        # self.status = elem.find("metainfo/status").text
        # self.transactionDate = elem.find("metainfo/transactionDate").text

    @staticmethod
    def process_null(elem):
        if elem is None:
            return ""
        else:
            return elem.text
