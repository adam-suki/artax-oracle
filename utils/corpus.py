import glob
import fileinput

RAW_DIR = glob.glob('data/raw/*.txt')

def build_corpus(outfilename, lof=RAW_DIR):
    with open(outfilename, 'w') as outfile, fileinput.input(lof) as fin:
        for line in fin:
            outfile.write(line)
    