
import logging

logging.debug("Tai yra derinimo žinutė")
logging.info("Tai yra informacinė žinutė")
logging.warning("Tai yra įspėjimo žinutė")
logging.error("Tai yra klaidos žinutė")
logging.critical("Tai yra kritinė žinutė")

# -----------------IŠVESTIS-------------------
# WARNING:root:Tai yra įspėjimo žinutė
# ERROR:root:Tai yra klaidos žinutė
# CRITICAL:root:Tai yra kritinė žinutė


import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.debug("Tai yra derinimo žinutė")
logging.info("Tai yra informacinė žinutė")

# -----------------------KONSOLĖS IŠVESTIS-----------------------
# 2024-10-09 21:33:34 - root - DEBUG - Tai yra derinimo žinutė
# 2024-10-09 21:33:34 - root - INFO - Tai yra informacinė žinutė



import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levellevel)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
name = input("Įveskite savo vardą: ")
logging.info(f"{name} sėkmingai prisijungė!")

# ----------------------data.log FAILO TURINYS--------------------
# 2024-10-09 21:35:42 - root - INFO - Tomas sėkmingai prisijungė!
# 2024-10-09 21:35:53 - root - INFO - Karolis sėkmingai prisijungė!
# 2024-10-09 21:35:56 - root - INFO - Rytis sėkmingai prisijungė!



import logging

a = 10
b = 0

try:
    c = a / b
except Exception as e:
    logging.exception("Įvyko išimtis!")
  
# ------------------------KONSOLĖS IŠVESTIS-----------------------
# ERROR:root:Įvyko išimtis!
# Traceback (most recent call last):
#   File "/home/user/projects/python/log_exception.py", line 7, in <module>
#     c = a / b
#         ~~^~~
# ZeroDivisionError: division by zero