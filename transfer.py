# coding=utf-8

import pathlib
import sys

REDIRECT_HOST = "127.0.0.1"


def transfer(input_file: pathlib.Path, output_file: pathlib.Path):
    with input_file.open(mode="r") as input_fp, output_file.open(mode="w") as output_fp:
        for line in input_fp:
            if not line:
                continue
            elif line.startswith("#"):
                output_fp.write(line)
            else:
                output_fp.write(REDIRECT_HOST + " " + line)


if __name__ == "__main__":
    transfer(
        input_file=pathlib.Path(sys.argv[1]),
        output_file=pathlib.Path(__file__).parent / "anti-ad-adaway.txt",
    )
