import argparse

trans_table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "卂乃匚刀乇千厶卄工勹片乚爪𠘨口尸甲尺己丅凵リ山乂丫乙")


def make_extra_thicc(text: str) -> str:
    return text.translate(trans_table)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT")
    options = parser.parse_args()

    print(make_extra_thicc(options.INPUT))


if __name__ == "__main__":
    main()
