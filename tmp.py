import picar_4wd as fc

speed = 30

def main():

    fc.forward(speed)
    fc.time.sleep(2)
    fc.turn_left(speed)
    fc.time.sleep(2)
    fc.forward(speed)
    fc.turn_left(speed)
    fc.time.sleep(2)
    fc.forward(speed)
    fc.time.sleep(2)
    fc.turn_left(speed)
    fc.time.sleep(2)
    fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
