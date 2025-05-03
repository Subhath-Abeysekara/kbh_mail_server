import requests
import urllib.parse
import time

USER_ID = "94772034169"
PASSWORD = "2530"

def send_message(message , contacts):
  TO_NUMBERS = contacts

  MESSAGE = message
  encoded_message = urllib.parse.quote(MESSAGE)

  for number in TO_NUMBERS:
    api_url = f"https://textit.biz/sendmsg/index.php?id={USER_ID}&pw={PASSWORD}&to={number}&text={encoded_message}"

    try:
        response = requests.get(api_url)
        print(f"📤 Sending to {number} - Response: {response.text}")

        if "OK" in response.text:
            print(f"✅ SMS sent to {number}")
        else:
            print(f"❌ Failed to send to {number}: {response.text}")

        time.sleep(5)

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error sending to {number}: {e}")

# send_message("message" , ["0779421354"])

def send_inventory_retain_sms():
    contacts = ["0779421354" , '0705071971']
    message = "Retain Stock Is Updated Successfully"
    send_message(message=message , contacts=contacts)

def send_message_api_ops(message):
    contacts = ["0779421354",'0705071971']
    send_message(message=message, contacts=contacts)
