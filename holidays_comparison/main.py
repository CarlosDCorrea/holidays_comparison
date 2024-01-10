import argparse

from .holidays_comparison import perform_comparison


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='holidays-comparison',
                                     description="""
                                     This program allows users to compare two countries holidays,
                                     it allows the user to know what holidays both countries share and
                                     what of them dont""",
                                     epilog="Dev. Carlos Correa")

    parser.add_argument('--y',
                        '-year',
                        type=int,
                        help="""
                        The year where the comparison is going to be made,
                        this is the name of the sheet as well for every year,
                        if None, the current year will be use
                        """)

    args = parser.parse_args()
    perform_comparison(args)
