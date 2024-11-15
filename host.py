from server import run_server
from client import run_client
import multiprocessing

from helper import get_internal_ip

def run_host():
    ip_addr = get_internal_ip()

    server_process = multiprocessing.Process(target=run_server)
    server_process.start()

    # Wait a moment to ensure the server has started
    import time
    time.sleep(2)

    client_process = multiprocessing.Process(target=run_client, args=(ip_addr,))
    client_process.start()

    server_process.join()
    client_process.join()

if __name__ == "__main__":
    run_host()