import pdfkit
from pathlib import Path
from typing import List, Optional
from tqdm.contrib.itertools import product
from sec_edgar_downloader import Downloader

def _download_sec_filing(
    company_name: str,
    company_email: str,
    storage_dir: str,
    filing_type: str,
    cik: str,
    limit=None, 
    before=None, 
    after=None,
    download_details=True,
):
    """
    Download SEC filing for given CIK and filing type.
    """
    dl = Downloader(company_name, company_email, storage_dir)
    dl.get(filing_type, cik, limit=limit, before=before, after=after, download_details=download_details)

def _convert_to_pdf(storage_dir: str):
    """
    Converts all html files in a directory to PDF files.

    # Assumed directory structure:
    # storage_dir
    # ├── sec-edgar-filings
    # │   ├── filing_type
    # │   │   ├── cik
    # │   │   │   ├── filing #
    # │   │   │   │   ├── primary-document.html
    # │   │   │   │   ├── primary-document.pdf
    """

    data_dir = Path(storage_dir) / "sec-edgar-filings"

    for filing_type_dir in data_dir.iterdir():
        for cik_dir in filing_type_dir.iterdir():
            for filing_dir in cik_dir.iterdir():
                filing_html = filing_dir / "primary-document.html"
                filing_pdf = filing_dir / "primary-document.pdf"
                if filing_html.exists() and not filing_pdf.exists():
                    print("- Converting {}".format(filing_html))
                    input_path = str(filing_html.absolute())
                    output_path = str(filing_pdf.absolute())
                    try:
                        options = {'enable-local-file-access': None}
                        pdfkit.from_file(input_path, output_path, options=options, verbose=True)
                        print(f"Successfully converted {input_path} to {output_path}")
                    except Exception as e:
                        print(f"Error converting {input_path} to {output_path}: {e}")

def main(
    company_name: str,
    company_email: str,
    storage_dir: str,
    file_types: List[str],
    ciks: List[str],
    before: Optional[str] = None,
    after: Optional[str] = None,
    limit: Optional[int] = 5,
    convert_to_pdf: bool = True,
):
    print(f'Downloading filings to "{Path(storage_dir).absolute()}"')
    print(f"File Types: {file_types}")

    for symbol, file_type in product(ciks, file_types):
        try:
            filing_dir = Path(storage_dir) / "sec-edgar-filings" / symbol / file_type
            if filing_dir.exists():
                print(f"- Filing for {symbol} {file_type} already exists, skipping")
            else:
                print(f"- Downloading filing for {symbol} {file_type}")
                _download_sec_filing(company_name, company_email, storage_dir, file_type, symbol, limit, before, after)
        except Exception as e:
            print(
                f"Error downloading filing for symbol={symbol} & file_type={file_type}: {e}"
            )

    if convert_to_pdf:
        print("Converting html files to pdf files")
        _convert_to_pdf(storage_dir)