import requests
import re

def calculate_khamis_roche(
  cage: str,
  csex: str,
  cheightmeter: str,
  ckg: str,
  mcheightmeter: str,
  fcheightmeter: str
):  

  url = ("https://www.calculator.net/height-calculator.html?"
        "ctype=metric&"
        "ptype=1&"
        f"cage={cage}&"
        f"csex={csex}&"
        f"cheightmeter={cheightmeter}&"
        f"ckg={ckg}&"
        f"mcheightmeter={mcheightmeter}&"
        f"fcheightmeter={fcheightmeter}&"
        "x=00&y=00")


  response = requests.request("GET", url)

  html = response.text

  tags = re.findall(r"<font color='green'>(.*?)</font>", html, re.DOTALL)

  for tag in tags:
    try:
      total = float(
        tag.split(" ")[0]
      )

      print(total)
      return total
    except Exception as e:
      print(f"ERROR: {e}")
      return 0.0