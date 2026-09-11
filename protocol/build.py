"""Build Word versions of the protocol.

Writes to protocol/build/, which is not tracked:
  protocol.docx           the protocol
  protocol-full.docx      the full protocol

Needs pandoc 3 on PATH, or its location in the PANDOC environment variable.
Styles and page setup come from reference.docx, which also marks the output as
current-format Word so that it does not open in compatibility mode.
Stops if prompt/base_prompt.txt no longer matches Appendix 2 of either protocol.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'build'
PROMPT = HERE.parent / 'prompt' / 'base_prompt.txt'
REFERENCE = HERE / 'reference.docx'
SOURCES = ('protocol', 'protocol-full')


def read(path):
    return path.read_text(encoding='utf-8').replace('\r\n', '\n')


def appendix2_prompt(text):
    start = text.index('## Appendix 2.')
    body = text.index('\n', text.index('```text', start)) + 1
    return text[body:text.index('```', body)]


def main():
    pandoc = os.environ.get('PANDOC') or shutil.which('pandoc')
    if not pandoc:
        sys.exit('pandoc not found: put it on PATH or set PANDOC')

    prompt = read(PROMPT)
    for name in SOURCES:
        if appendix2_prompt(read(HERE / f'{name}.md')) != prompt:
            sys.exit(f'prompt/base_prompt.txt differs from Appendix 2 of {name}.md')

    OUT.mkdir(exist_ok=True)
    for name in SOURCES:
        dst = OUT / f'{name}.docx'
        subprocess.run([pandoc, '--citeproc', '--resource-path', str(HERE),
                        '--reference-doc', str(REFERENCE),
                        f'{name}.md', '-o', str(dst)], cwd=HERE, check=True)
        print('wrote', dst)


if __name__ == '__main__':
    main()
