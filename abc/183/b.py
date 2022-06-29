def main():
    SX, SY, GX, GY = map(int, input().split())

    print((SY*GX+SX*GY) / (SY+GY))

if __name__ == "__main__":
    main()
