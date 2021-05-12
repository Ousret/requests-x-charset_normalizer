from json import load
from os.path import exists
from typing import Dict, Optional


def cp_name(name: Optional[str]) -> str:
    if name is None:
        return 'N/A'
    return name.lower().replace('windows-', 'cp').replace('-', '_').replace('iso_', 'iso').replace('ibm', 'cp')


def is_equivalent(cp_a: Optional[str], cp_b: Optional[str]) -> bool:
    cp_name_a: str = cp_name(cp_a)
    cp_name_b: str = cp_name(cp_b)

    if cp_name_a == 'ibm855' and cp_name_b == "cp855":
        return True

    if cp_name_a == "euc_jp" and cp_name_b == "euc_jis_2004":
        return True

    if cp_name_a == "shift_jis" and (cp_name_b == "cp932" or cp_name_b == "shift_jis_2004"):
        return True

    if cp_name_a == "euc_kr" and cp_name_b == "cp949":
        return True

    if cp_name_a == "maccyrillic" and cp_name_b == "mac_cyrillic":
        return True

    if cp_name_a == "iso8859_1" and cp_name_b == "cp1252":
        return True

    if cp_name_a == "iso8859_7" and cp_name_b == "cp1253":
        return True

    return cp_name_a == cp_name_b


if __name__ == "__main__":

    if exists("./results/dump-2.7.json") is False or exists("./results/dump-3.8.json") is False:
        print("Missing either 2.7 or 3.8 dump")
        exit(1)

    r27: Dict[str, Optional[str]]
    r38: Dict[str, Optional[str]]

    with open("./results/dump-2.7.json", "r") as fp:
        r27 = load(fp)

    with open("./results/dump-3.8.json", "r") as fp:
        r38 = load(fp)

    c: int = 0

    print("file;chardet;charset_normalizer")

    for file, apparent_encoding in r27.items():
        if not is_equivalent(apparent_encoding, r38[file]):
            print(f"{file};{apparent_encoding};{r38[file]}")
            c += 1

    print("EOF;EOF")

    print("Ratio ", (1.0 - round(c / len(r27.keys()), 3)) * 100.)
