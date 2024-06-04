from pathlib import Path
from pydantic import BaseModel, EmailStr

class AppConfig(BaseModel):
    """
    Application configuration.
    """

    # Global
    # OPENAI_API_KEY: str
    SEC_EDGAR_COMPANY_NAME: str = "OrgName"
    SEC_EDGAR_COMPANY_EMAIL: EmailStr = "org@example.com"

    # SEC Filings Downloader
    DEFAULT_STORAGE_DIR: Path = Path.cwd() / "data"
    DEFAULT_SEC_CIKS: list = [
        "0000320193",    # AAPL (Apple)
        "0001018724",    # AMZN (Amazon)
        "0001730168",    # AVGO (Broadcom)
        "0000070858",    # BAC (Bank of America)
        "0001067983",    # BRK A (Berkshire Hathaway)
        "0001652044",    # GOOGL (Alphabet Inc.)
        "0000200406",    # JNJ (Johnson & Johnson)
        "0000019617",    # JPM (JPMorgan Chase & Co.)
        "0000059478",    # LLY (Eli Lilly)
        "0001326801",    # META (Meta Platforms)
        "0000789019",    # MSFT (Microsoft)
        "0001065280",    # NFLX (Netflix)
        "0001045810",    # NVDA (NVIDIA)
        "0001318605",    # TSLA (Tesla)
        "0000731766",    # UNH (UnitedHealth Group Inc.)
    ]
    DEFAULT_SEC_FILING_TYPES: list = [
        "10-K",  # Annual report
        "10-Q",  # Quarterly report
        "8-K",   # Current report
    ]

AppConfig = AppConfig()