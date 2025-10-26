import time

def main():
    for i in range(4):
        print(f"\rLoading... {i+1}/4", end="")
        time.sleep(1)

if __name__ == ("__main__"):
    main()