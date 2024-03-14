#!/usr/bin/env python3

import argparse
import global_decorator as gd
import data_ingest.ingest_data as ingest


def user_input() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description="""
This program...
    """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", "-f", metavar="PATH",
                        help="Path to file")
    gd.add_log_arg(parser)  # Add decorator options

    return parser


"""
############################# MAIN #############################
"""


def main():
    """
    Run the program. Accepts no inputs.
    """
    # Build and store user arguments
    parser = user_input()
    input_args = parser.parse_args()

    # Configure the logging object
    gd.set_logging(input_args)

    # Error if the user does not give an argument
    if all(value is False or value is None
           for value in vars(input_args).values()):
        parser.print_help()
        raise argparse.ArgumentError("NO ARGUMENT GIVEN BUT REQUIRED!")


# Only run if executing, not import
if __name__ == "__main__":

    main()

