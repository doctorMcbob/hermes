import hermes
import threading

def get_file(filename):
    with open(filename, "a") as f:
        for data, conn in hermes.listen(8080, log_function=print):
            f.write(data)

def send_file(filename):
    with open(filename) as f:
        hermes.send(f.read(), 8080, log_function=print)

thread = threading.Thread(target=get_file, args=("data.txt",))

thread.start()

send_file("hermes.py")
