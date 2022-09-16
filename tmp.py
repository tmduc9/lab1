import picar_4wd as fc

speed = 30

def main():
    while True :
        fc.forward(speed)
        fc.time.sleep(0.4)
        fc.left(speed)
        fc.time.sleep(0.4)
        fc.left(speed)
        fc.time.sleep(0.4)
        fc.left(speed)
        fc.time.sleep(1)
        fc.stop()
        fc.backward(speed)
        fc.time.sleep(0.4)
        fc.right(speed)
        fc.time.sleep(0.4)
        fc.right(speed)
        fc.time.sleep(0.4)
        fc.right(speed)
        fc.stop()
        fc.time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
