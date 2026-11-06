"""Site identity and edition date; source access dates remain per-reference."""
from datetime import date

SITE_TITLE = 'Mind Uploading Research Guide'
DATE = '2026-11-07'

_date = date.fromisoformat(DATE)
_months = ('January', 'February', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December')
DATE_JA = f'{_date.year}年{_date.month}月{_date.day}日'
DATE_EN = f'{_date.day} {_months[_date.month - 1]} {_date.year}'
EDITION_JA = f'{_date.year}年{_date.month}月版'
EDITION_EN = f'{_months[_date.month - 1]} {_date.year}'
ASSET_VERSION = DATE.replace('-', '')
