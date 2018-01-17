from optparse import  OptionParser


def main():
    parser = OptionParser()
    parser.add_option("-f", '--filename', dest="filename", help="write report to file"
                      , metavar="FILENAME")
    parser.add_option("-x", "--xray", dest="xray", help="specify xray strength factor")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose"
                      , default=True, help="don't print status message to stdout")
    (options, args) = parser.parse_args()

    print("options:", str(options))
    print("arguments:", args)


main()
