import requests
from bson import ObjectId
import datetime
import pytz

from send_messages import send_inventory_retain_sms


def get_utc_time_count():
    current_time = datetime.datetime.now(pytz.utc)
    hours = int(current_time.strftime('%H'))
    minutes = int(current_time.strftime('%M'))
    return hours * 60 + minutes

def retain_stock_dev():
        url = f"https://765ip88erb.execute-api.ap-south-1.amazonaws.com/dev/v1/retain_inventory"
        validate_res = requests.put(url=url)
        print(validate_res.json())
        print("response")
        if validate_res.json()['state']:
            send_inventory_retain_sms()
        return

def retain_stock_prod():
        url = f"https://3vz73bk5y0.execute-api.ap-south-1.amazonaws.com/prod/v1/retain_inventory"
        validate_res = requests.put(url=url)
        print(validate_res.json())
        print("response")
        if validate_res.json()['state']:
            send_inventory_retain_sms()
        return

def automation_operation():
        utc_count = get_utc_time_count()
        print("Automation - ",utc_count)
        level_1 = 16*60+30
        level_2 = 18*60+28
        # level_1 = 7 * 60 + 40
        # level_2 = 7 * 60 + 55
        if utc_count>=level_1 and utc_count<=level_2:
            print("Operation")
            retain_stock_dev()
            retain_stock_prod()
        return

# retain_stock_prod()