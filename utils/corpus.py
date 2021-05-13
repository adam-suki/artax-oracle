import re
import glob
import fileinput

RAW_DIR = glob.glob('data/raw/*.txt')
DROP_LIST = ['[', 'Kurt Cobain', 'Dave Grohl', 'Verse', 'Chorus', 'Outro', 'Intro', 'Guitar Solo]', 'Pre-Chorus', 'Bridge', 'Refrain', 'Instrumental', 'found sound', 'Hook']

def build_corpus(outfilename: str,
                 clean_file: bool = True, 
                 lof: list[str] = RAW_DIR, 
                 drop_lines: list[str] = DROP_LIST) -> None:
    """Combines all inputted text files within and prepares the file for training 

    Args:
        :param ``outfilename``: Output file's name
        :param ``clean_file``: Processes raw text, removing unnecessary and empty lines (default: True)
        :param ``lof``: List of files to be processed.
        :param ``drop_lines``: List of patterns to be look for when deciding to drop a line or not
    Returns:
        None
    """
    with open(outfilename, 'w') as outfile, fileinput.input(lof) as fin:
        for line in fin:
            outfile.write(line)
    if clean_file:
        process_corpus(outfilename, drop_lines)


def process_corpus(outfilename: str,
                   drop_lines: list[str]) -> None:
    """Combines all inputted text files within and prepares the file for training 

    Args:
        :param ``outfilename``: output file's name
        :param ``drop_lines``: List of patterns to be look for when deciding to drop a line or not
    Returns:
        None
    """
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