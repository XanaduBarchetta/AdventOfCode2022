import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    stream = f.readline()  # Inefficient, sure...
    chars_read = 4
    window = stream[:4]
    while len(set(window)) < 4:
        chars_read += 1
        window = stream[chars_read-4:chars_read]
    print(chars_read)
