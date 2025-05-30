
import pandas as pd
import sqlite3

def generate_report():
    conn = sqlite3.connect("data/urls.db")
    df = pd.read_sql_query("SELECT * FROM urls", conn)
    df.to_csv("logs/url_report.csv", index=False)
    print("Report saved as 'logs/url_report.csv'")
