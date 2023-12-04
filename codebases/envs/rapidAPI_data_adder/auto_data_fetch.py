import requests
import json
import os
import csv
import time
from datetime import datetime, date

currency_from = "JPY"
currency_to = "USD"

now = datetime.now()


url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function":"FX_INTRADAY","interval":"5min","to_symbol":currency_to,"from_symbol":currency_from,"datatype":"json","outputsize":"compact"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "ef282bdcfcmsh18c656c591cb885p1b2f17jsn14744cad9cfc"
    }

csv_filename = f"C:\\Users\\tashin\Desktop\\AriSafTech Projects\\1. trading_bot\\1. FOREX\\auto_trade\\data\\{currency_from.lower()}_{currency_to.lower()}.csv"
csv_headers = ["timestamp", "open", "high", "low", "close"]
logger_filename = "logger.txt"


def str_to_timestamp(timestamp_as_str: str) -> datetime:
    return datetime.strptime(timestamp_as_str, "%Y-%m-%d %H:%M:%S")

def log_the_error(error):
    current_date = date.today()
    current_time = now.strftime("%H:%M:%S")
    with open(logger_filename, 'a+', encoding="utf-8") as logger:
        logger.write(f"Date: {current_date}  Time: {current_time} \n\tError: {error}\n\n")


# while Loop for keeping the script alive
while True:
    # flag = file access success; data-type: Boolean(initial false)
    result = None
    has_file_access = False
    has_headers = False
    has_data = False
    latest_existing_timestamp = datetime.min
    interval = 300
    # status = check if the api access is successful or not(false by default)
    status = False
    # Try
    try:
        # Try to access the api and read the data
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            status = True
            data = json.loads(response.text)
            result = data["Time Series FX (5min)"]
        # execute if the API status is OK
        if status == True and result != None:
            while (not has_file_access and interval > 1):
                try:
                    if os.path.exists(csv_filename):
                        with open(csv_filename, "r", encoding="utf-8", newline="") as f:
                            has_headers = f.readline() != ""
                            has_data = f.readline() != ""
                            if has_data:
                                latest_existing_timestamp = str_to_timestamp(f.readlines()[-1].split(',')[0])


                    with open(csv_filename, "a+", encoding="utf-8", newline="") as f:
                        has_file_access = True

                        if not has_headers:
                            f.write(f"{','.join(csv_headers)}\n")

                        arr = []
                        for timestamp, values in result.items():
                            if str_to_timestamp(timestamp) <= latest_existing_timestamp:
                                break
                            arr.append(f"{timestamp},{values['1. open']},{values['2. high']},{values['3. low']},{values['4. close']}\n")
                        
                        for _ in range(len(arr)):
                            f.write(arr.pop()) 
                        
                    
                # log the error in a logger file
                except OSError as os_error:
                    log_the_error(os_error)
                except Exception as error:
                    log_the_error(error) 
                finally:
                    interval -= 1
                    time.sleep(1.0)
                 
    # Catch block for writing the logger into a file system
    except Exception as error:
        log_the_error(error)
   
    # sleep for 5 mins to get in 5mins interval 
    finally:
        time.sleep(interval)    # 300 sec = 5 mins
    
