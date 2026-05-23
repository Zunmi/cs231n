import argparse
import os
import shutil
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
    env_bin = os.path.dirname(sys.executable)
    env["PATH"] = env_bin + os.pathsep + env.get("PATH", "")

    nbconvert_cmd = shutil.which("jupyter-nbconvert")
    if nbconvert_cmd is None:
        nbconvert_cmd = [sys.executable, "-m", "nbconvert"]
    else:
        nbconvert_cmd = [nbconvert_cmd]

    os_args = nbconvert_cmd + ["--log-level", "CRITICAL", "--to", "pdf"]
    if shutil.which("xelatex", path=env["PATH"]) is None and shutil.which("tectonic", path=env["PATH"]) is not None:
        os_args.append("--PDFExporter.latex_command=['tectonic','{filename}']")
        os_args.append("--PDFExporter.bib_command=['true']")
    for f in files:
        subprocess.run(os_args + [f], check=True, env=env)
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
