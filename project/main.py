from project.annual_report.annual_report_downloader import AnnualReportDownloader

def main():
    annual_report = AnnualReportDownloader()
    annual_report.get_annual_report_urls(company='nvidia-corporation')
    print(annual_report.urls)
    print(annual_report.companies)
    annual_report.download_annual_reports()
    print(annual_report.create_output_paths().values())

if __name__ == "__main__": main()
