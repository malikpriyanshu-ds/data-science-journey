import time

password = "never give up"
total_wrong_attempts = 0
max_attempts = 5

while True:
    attempt = 3

    while attempt > 0:
        your_pass = input("Enter your password(or type exit): ")

        if your_pass == password:
            print("Access granted✅")
            break

        elif your_pass.lower() == "exit":
            print("See you again...")
            break

        elif your_pass.strip() == "":
            print("Empty input not allowed")
            continue

        attempt -= 1
        total_wrong_attempts += 1

        print(f"Wrong Password❌\nAttempts left: {attempt}")
        print(f"Total wrong attempts: {total_wrong_attempts}")
        time.sleep(1)

        if total_wrong_attempts >= max_attempts:
            print("\nLimit crossed📛")
            print("System blocked for 24 hours")
            exit()

    else:
        print("Too many attempts❗")
        print("System locked for 5 seconds...")

        for i in range(5, 0, -1):
            print(f"Locked....{i}", end="\r")
            time.sleep(1)

        print("\nSystem restarting...\n")
        continue
    break
