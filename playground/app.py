from requests import get
import sys
from json import dump

if __name__ == "__main__":
    files = get("http://serve:5000/").json()
    results = dict()

    print("file;apparent_encoding")

    for file in files:
        r = get(
            "http://serve:5000/" + file
        )

        if r.ok is False:
            print(file, r)
            exit()

        print(file + ";" + str(r.apparent_encoding))
        results[file] = r.apparent_encoding

    print("EOF;EOF")

    with open("/results/dump-" + str(sys.version_info.major) + "." + str(sys.version_info.minor) + ".json", "w") as fp:
        dump(results, fp, indent=4)
