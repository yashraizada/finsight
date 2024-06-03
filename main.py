from src.sec import download_sec_filings
from src.core.config import AppConfig

print(AppConfig)

download_sec_filings.main(AppConfig.SEC_EDGAR_COMPANY_NAME, 
                  AppConfig.SEC_EDGAR_COMPANY_EMAIL, 
                  AppConfig.DEFAULT_STORAGE_DIR, 
                  AppConfig.DEFAULT_SEC_FILING_TYPES, 
                  AppConfig.DEFAULT_SEC_CIKS)