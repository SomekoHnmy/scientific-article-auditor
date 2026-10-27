"""Build Word versions of the protocol.

Writes to protocol/build/, which is not tracked:
  protocol.docx           the protocol
  protocol-full.docx      the full protocol

Needs pandoc 3 on PATH, or its location in the PANDOC environment variable.
Styles and page setup come from reference.docx, which also marks the output as
current-format Word so that it does not open in compatibility mode.
Stops if the prompt files in prompt/ no longer match Appendix 2 of either protocol.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'build'
# the prompts in the order Appendix 2 gives them
PROMPTS = (HERE.parent / 'prompt' / 'prompt_domains_a_c.txt', HERE.parent / 'prompt' / 'prompt_domain_d.txt')
REFERENCE = HERE / 'reference.docx'
SOURCES = ('protocol', 'protocol-full')


def read(path):
    return path.read_text(encoding='utf-8').replace('\r\n', '\n')


def appendix2_prompts(text):
    start = text.index('## Appendix 2.')
    end = text.index('## Appendix 3.', start)
    prompts, pos = [], start
    while (fence := text.find('```text', pos, end)) != -1:
        body = text.index('\n', fence) + 1
        close = text.index('```', body)
        prompts.append(text[body:close])
        pos = close + 3
    return prompts


def main():
    pandoc = os.environ.get('PANDOC') or shutil.which('pandoc')
    if not pandoc:
        sys.exit('pandoc not found: put it on PATH or set PANDOC')

    prompts = [read(p) for p in PROMPTS]
    for name in SOURCES:
        if appendix2_prompts(read(HERE / f'{name}.md')) != prompts:
            sys.exit(f'the prompt files differ from Appendix 2 of {name}.md')

    OUT.mkdir(exist_ok=True)
    for name in SOURCES:
        dst = OUT / f'{name}.docx'
        subprocess.run([pandoc, '--citeproc', '--resource-path', str(HERE),
                        '--reference-doc', str(REFERENCE),
                        f'{name}.md', '-o', str(dst)], cwd=HERE, check=True)
        print('wrote', dst)


if __name__ == '__main__':
    main()
