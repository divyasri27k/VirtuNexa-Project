
# URL Shortener Tool with Click Analytics

## Features
- Console-based user interface
- Shorten long URLs
- Retrieve original URLs using short code
- Track click counts
- (Optional) Generate analytics report with Pandas

## Requirements
- Python 3.x
- pandas (for analytics)

## How to Run
```bash
python main.py
```

## Project Structure
- `main.py` - Console UI
- `shortener.py` - URL shortening logic
- `db.py` - SQLite handling
- `analytics.py` - Optional analytics report
- `data/urls.db` - SQLite database (auto-created)
- `logs/activity.log` - User activity log
