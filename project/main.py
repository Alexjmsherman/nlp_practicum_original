from project.annual_report.annual_report_downloader import AnnualReportDownloader
from project.documents.doc_extractor import extract_document_text
from project.database.db_populator import db_populator

def main():
    annual_report = AnnualReportDownloader(company='southwest-airlines-co')
    annual_report.get_annual_report_urls()
    print(annual_report.urls)
    print(annual_report.companies)
    annual_report.download_annual_reports()
    print(annual_report.create_output_paths().values())

    for doc in extract_document_text:
        # load into database
        pass

if __name__ == "__main__": main()
