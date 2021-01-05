import time

# monotonic time is for measuring intervals and not for modelling real-world time
start = time.monotonic()
# do something here
end = time.monotonic()

difference_in_seconds = int(round(end - start))
