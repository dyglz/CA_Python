# Vartotojo įvestis

import logging

logging.basicConfig(
    filename="uzd1_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

while True:
    user_input = input("Enter a phrase (or Q to quit): ")
    if user_input.lower() == "q":
        print("End of the program")
        break

    logging.info(f"User input: {user_input}")