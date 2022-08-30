import argparse
from typing import TextIO


def make_library(f: TextIO) -> dict[str, str]:
    out: dict[str, str] = {}
    tmp = ''.join(f.readlines())
    seqs = tmp.split('@')
    for line in seqs:
        if line:
            seq = line.split('\n')
            out[seq[0]] = seq[1]
    return out


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the names from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    lib = make_library(args.fastq)
    out = [key for key in lib]
    print('\n'.join(out))


if __name__ == '__main__':
    main()
