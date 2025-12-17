import time

def log_execution(func):
    def wrapper():
        print(f"[LOG] {func.__name__} started")
        start = time.time()

        func()   # call actual function

        end = time.time()
        print(f"[LOG] {func.__name__} ended")
        print(f"[LOG] Execution Time: {end - start:.2f} seconds\n")
    return wrapper


@log_execution
def process_data():
    print("Processing data...")
    time.sleep(2)


@log_execution
def generate_report():
    print("Generating report...")
    time.sleep(1)


@log_execution
def upload_file():
    print("Uploading file...")
    time.sleep(3)


# calling functions
process_data()
generate_report()
upload_file()
