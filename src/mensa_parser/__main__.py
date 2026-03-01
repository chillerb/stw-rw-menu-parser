#!/usr/bin/env python3

from mensa_parser.main import get_todays_menu

def main():
    data = get_todays_menu()
    print(data)


if __name__ == "__main__":
    main()
