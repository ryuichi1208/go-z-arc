import sys
import optparse

def opt_parse():
    parser = optparse.OptionParser()
    parser.add_option('-o', '--output',
                      dest="output_filename",
                      default="default.out",
                      )

    parser.add_option('-v', '--verbose',
                  dest="verbose",
                  default=False,
                  action="store_true",
                  )

    parser.add_option('--version',
                      dest="version",
                      default=1.0,
                      type="float",
                      )

    options, _ = parser.parse_args()

    return options


def main(options):
    print(options.output_filename)

if __name__ == "__main__":
    options = opt_parse()
    main(options)

