import threading
import time
from sub_time import timer


def main_loop():
    i = 11
    for number in range(i):
        print(f"Main Thread: {number}")
        time.sleep(1)

def start_threads():
    main_thread = threading.Thread(target=main_loop)
    timer_thread = threading.Thread(target=timer)

    timer_thread.start()
    main_thread.start()

    main_thread.join()
    timer_thread.join()


if __name__ == "__main__":
    start_threads()
