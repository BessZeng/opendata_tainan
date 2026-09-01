#載入所需套件工具
import os #處理路徑
import logging #紀錄log
import requests as rq #向server提出請求
import pandas as pandas #處理資料
from sqlalchemy import create_engine, text  #DB engine
import pymysql #連線mysql
import openpyxl # excel驅動
import urllib3 #處理url
from dotenv import load_dotenv #抓取.env資料

# 1. 載入.env

# 2. 設定log機制(純寫到file & 輸出到終端機上)
logging.basicConfig(
    level=logging.INFO, #設定紀錄層級
    format='%(asctime)s [%(levelname)s] %(filename)s (行:%(lineno)d: %(message)s)',  
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("scraper.log", encoding="utf-8"),   #寫到檔案
        logging.StreamHandler()  #寫到終端機
    ]
)

# 設定變數
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "besszeng")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "@Yunong1030012")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_NAME = os.environ.get("DB_NAME", "tainan")
DB_CHARSET = os.environ.get("DB_CHARSET", "utf8mb4")

API_URL = os.environ.get("API_URL")
EXCEL_FILENAME = os.environ.get("EXCEL_FILENAME", "tainan_house.xlsx")
