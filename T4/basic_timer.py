import time

def slow_function():
    print("-- slow_function start --")
    time.sleep(3) # waits for x seconds
    print("-- slow_function stop --")

start_time = time.time() # creates timestamp

print("- calling slow_function -")
slow_function()

end_time = time.time()

elapsed_time = end_time - start_time
print(f"time diff: {elapsed_time}")