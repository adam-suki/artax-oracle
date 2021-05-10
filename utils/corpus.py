import re
import glob
import fileinput

RAW_DIR = glob.glob('data/raw/*.txt')
DROP_LIST = ['[', 'Kurt Cobain', 'Dave Grohl', 'Verse', 'Chorus', 'Outro', 'Intro', 'Guitar Solo]', 'Pre-Chorus', 'Bridge', 'Refrain', 'Instrumental', 'found sound', 'Hook']

def build_corpus(outfilename, clean_file=True, lof=RAW_DIR, drop_lines=DROP_LIST):
    with open(outfilename, 'w') as outfile, fileinput.input(lof) as fin:
        for line in fin:
            outfile.write(line)
    if clean_file:
        process_corpus(outfilename, drop_lines)


def process_corpus(outfilename, drop_lines):
    new_lines = re.compile('\n{2,9}')
    with open(outfilename) as f:
        contents = f.read()
    contents = re.sub(new_lines, '\n\n', contents.strip())
    with open(outfilename, 'w') as f:
        f.write(contents)
    with open(outfilename) as oldfile, open(str(outfilename.split('.')[0] + '_processed.txt'), 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in drop_lines):
                newfile.write(line)