import time as t


def get_time(title, time_start):
    result = "% 12.2f" % (t.time() - time_start)
    # print(title + ": " + result)
    return str(result).strip()
