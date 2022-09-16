import picar_4wd as fc

speed = 30

def main():
    while True :
        fc.forward(speed)
        fc.time.sleep(0.4)
        fc.turn_left(speed)
        fc.time.sleep(0.4)
        fc.turn_left(speed)
        fc.time.sleep(0.4)
        fc.turn_left(speed)
        fc.time.sleep(1)
        fc.stop()
        fc.backward(speed)
        fc.time.sleep(0.4)
        fc.turn_right(speed)
        fc.time.sleep(0.4)
        fc.turn_right(speed)
        fc.time.sleep(0.4)
        fc.turn_right(speed)
        fc.stop()
        fc.time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
