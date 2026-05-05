import argparse
import os
import subprocess
import sys

try:
    from PyPDF2 import PdfMerger

    MERGE = True
except ImportError:
    print("Could not find PyPDF2. Leaving pdf files unmerged.")
    MERGE = False


def main(files, pdf_name):
    env = os.environ.copy()
    env["PATH"] = os.path.dirname(sys.executable) + os.pathsep + env.get("PATH", "")
    os_args = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--log-level",
        "CRITICAL",
        "--to",
        "pdf",
    ]
    for f in files:
        os_args.append(f)
        result = subprocess.run(os_args, env=env)
        os_args.pop()
        if result.returncode != 0:
            print("Failed to create PDF {}.".format(f), file=sys.stderr)
            print(
                "Run the command above without --log-level CRITICAL for details, "
                "or make sure pandoc and a LaTeX distribution are installed.",
                file=sys.stderr,
            )
            sys.exit(result.returncode)
        print("Created PDF {}.".format(f))
    if MERGE:
        pdfs = [f.split(".")[0] + ".pdf" for f in files]
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(pdf_name)
        merger.close()
        for pdf in pdfs:
            os.remove(pdf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # We pass in a explicit notebook arg so that we can provide an ordered list
    # and produce an ordered PDF.
    parser.add_argument("--notebooks", type=str, nargs="+", required=True)
    parser.add_argument("--pdf_filename", type=str, required=True)
    args = parser.parse_args()
    main(args.notebooks, args.pdf_filename)
