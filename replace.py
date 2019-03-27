import sys


def main():
    content = sys.stdin.read()
    sys.stdout.write(content.replac(sys.argv[1], sys.argv[2]))


main()