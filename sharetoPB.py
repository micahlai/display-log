import requests
import time

TEXT_FILE_PATH = '/Users/micahlai/Documents/Github/display-log/test.txt'

def get_content():
    try:
        with open(TEXT_FILE_PATH, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        return str(e), 500
def create_paste(api_dev_key, api_user_key, new_content):
    api_post_url = "https://pastebin.com/api/api_post.php"
    data = {
        'api_dev_key': api_dev_key,
        'api_user_key': api_user_key,
        'api_option': 'paste',
        'api_paste_name':'log update',
        'api_paste_code': new_content,
    }
    
    response = requests.post(api_post_url, data=data)
    
    if response.status_code == 200:
        print("Paste updated successfully. URL:", response.text)
        return response.text.removeprefix("https://pastebin.com/")
    else:
        print("Failed to update paste. Status code:", response.status_code, "Response:", response.text)
def delete_paste(api_dev_key, api_user_key, api_paste_key):
    api_post_url = "https://pastebin.com/api/api_post.php"
    data = {
        'api_dev_key': api_dev_key,
        'api_user_key': api_user_key,
        'api_paste_key': api_paste_key,
        'api_option': 'delete',
    }
    
    response = requests.post(api_post_url, data=data)
    
    if response.status_code == 200:
        print("Paste updated successfully.", response.text)
    else:
        print("Failed to update paste. Status code:", response.status_code, "Response:", response.text)
def get_user_key(api_dev_key, username, password):
    api_login_url = "https://pastebin.com/api/api_login.php"
    data = {
        'api_dev_key': api_dev_key,
        'api_user_name': username,
        'api_user_password': password
    }
    
    response = requests.post(api_login_url, data=data)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to get user key. Status code:", response.status_code, "Response:", response.text)

# Replace these variables with your actual values
api_dev_key = 'PaqUzblLbgJ1UKkumaRpRcx5mrPosO25'
username = 'anonymousshrimp'
password = 'jamesgrantconroy4'

api_user_key = get_user_key(api_dev_key, username, password)

while(True):
    new_content = get_content()
    paste_key = create_paste(api_dev_key, api_user_key,new_content)
    time.sleep(60)
    delete_paste(api_dev_key,api_user_key,paste_key)
