import SRI
import threading

if __name__ == "__main__":
    threading.Thread(target=SRI.dashboard).start()