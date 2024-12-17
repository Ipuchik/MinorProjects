import time

print("Press enter to start the stopwatch.")
input() # wait for user to press enter
print("Stopwatch started.")
start_time = time.time()

# using try-except block to handle a keyboard interrupt
try:
    while True:
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        print("Elapsed time: %.2f seconds" % elapsed_time, end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopwatch stopped.")
