import os
import re

id_pattern = re.compile(r'^.\d+$')


token = os.environ.get("TOKEN","7176123540:AAFtY7Vepb1_0j4Z835LdOr9uomHvNT_C_o")
app_id = int(os.environ.get("APP_ID", 15657755))
app_hash = os.environ.get("API_HASH", "7cce51d4664d010b90ad690e0d5121ad")
allowed = [int(user) if id_pattern.search(user) else user for user in os.environ.get('AUTH_USERS', '5003133371').split()]

help_text = """
Hello I'm Terminal Bot which will Execute your Commands.

With this bot you can execute system commands on your server.

**if you not owner of this bot You can not use me because I'm private...
So you run one of these for yourself [here](https://github.com/moshe-coh/Terminal-Bot)**

**My Commands For Owner Only:**

🔹 /st - speed test
🔹 /ip - ip details
🔹 /stats - disk space
🔹 /cd - change working dir
🔹 /my_files - file manager
🔹 And All System Commands...

"""
