import time 



def wait_half_a_sec():
    time.sleep(0.5)
    print("half a sec")


def wait_entire_sec():
    time.sleep(1)
    print("entire sec")


wait_entire_sec()
wait_entire_sec()
wait_entire_sec()
wait_half_a_sec()
wait_half_a_sec()
wait_half_a_sec()
