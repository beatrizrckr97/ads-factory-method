from .reports.transactions_report import TransactionsReport
<<<<<<< HEAD
from .reports.sales_report import SalesReport
=======
>>>>>>> upstream/main

class ReportFactory:
    def create_report(self, report_type):
        if report_type == "transactions":
            return TransactionsReport()
<<<<<<< HEAD
        elif report_type == "sales":
            return SalesReport()
=======
        else:
            raise ValueError("Tipo de relatório inválido")
>>>>>>> upstream/main
