import pyautogui
import webbrowser
import time
cart_pos = 966, 560
url = "https://www.amazon.in/Lenovo-Ideapad-81UT00JBIN-Extended-Warranty/dp/B08L9QLD8L/ref=sr_1_2_sspa?crid=2NFHRXRL2WVXB&dchild=1&keywords=lenovo+ideapad+s145+laptop&qid=1610346938&sprefix=lenovo+idea%2Caps%2C425&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNjhHS0c5MVFKRU1YJmVuY3J5cHRlZElkPUEwNzEzMDUxMjRIV0JSWklPSkJFMiZlbmNyeXB0ZWRBZElkPUEwMzE5NjU1Mk8wREhTMDhOOUxBTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
webbrowser.open(url)
time.sleep(5)
pyautogui.click(cart_pos)
