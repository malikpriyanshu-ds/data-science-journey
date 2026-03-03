import time

try:
    while True:
        now = time.localtime()
        formatted = time.strftime("%H:%M:%S", now)
        print(formatted, end="\r")

except KeyboardInterrupt:
    print("\nClock stopped successfully✅")
