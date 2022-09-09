import picar_4wd as fc

# speed = 30

def main():
    while True :
        scan_list = fc.scan_step(25)
        if not scan_list:
            continue

        tmp = scan_list[3:8]
        print(tmp)

        if tmp != [2,2,2,2,2]:
            fc.stop()
            fc.backward(30)
            fc.time.sleep(0.2)
            fc.turn_right(20)
            fc.time.sleep(0.2)
        else:
            fc.forward(50)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
