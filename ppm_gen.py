# need a way to see an image .
# many complex formats are there to render it , but using a simple format here


def main():
    IMAGE_WIDTH = 256
    IMAGE_HEIGHT = 256

    ## render
    print(f"P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255")

    for j in range(0, IMAGE_HEIGHT):
        for i in range(0, IMAGE_WIDTH):
            r = float(i) / (IMAGE_WIDTH - 1)
            g = float(j) / (IMAGE_HEIGHT - 1)
            b = 0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(f"{ir} {ig} {ib}")


if __name__ == "__main__":
    main()
