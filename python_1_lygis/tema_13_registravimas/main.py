# try:
#     print(2/0)
# except ZeroDivisionError:
#     logging.error("I can't", exec_info=True)


try:
    input = 25 / 0
    print(input)
except Exception as e:
    print(f"Error {e}")
else:
    print("No error occured")
finally:
    print("I will always run")