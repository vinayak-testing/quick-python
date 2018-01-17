import sys


def main():
    print("This is our replace script to demonstrate input output redirection")
    content = sys.stdin.read()
    sys.stdout.write(content.replace(sys.argv[1], sys.argv[2]))


main()

