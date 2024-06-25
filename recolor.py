import sys
import subprocess
import pathlib


class Recolor:
    def __init__(self, old_color: str, color: str) -> None:
        self.tw_main_file = lambda a: pathlib.Path(f'src/static/css/tw_{a}.css')
        self.tw_output_file = lambda a: pathlib.Path(f'src/static/css/{a}.css')
        self.old_color: str = old_color
        self.color: str = color
        self.npx_cmd: list = [
                'npx', 'tailwindcss',
                '-i', str(self.tw_main_file(self.color)),
                '-o', str(self.tw_output_file(self.color))
                ]

    def run(self) -> None:
        with open(self.tw_main_file(self.old_color), 'r', encoding='utf8') as rf:
            tw_css = rf.read()

        new_tw_css = tw_css.replace(self.old_color, self.color)

        with open(self.tw_main_file(self.color), 'w+', encoding='utf8') as wf:
            wf.write(new_tw_css)


        # Shell injection was fixed with Python 3.12 - don't panic!
        #
        # # Quote:
        #
        # Changed in version 3.12: Changed Windows shell search order for shell=True. 
        # The current directory and %PATH% are replaced with %COMSPEC% and %SystemRoot%\System32\cmd.exe. 
        # As a result, dropping a malicious program named cmd.exe into a current directory no longer works.
        #
        # https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module
        subprocess.run(self.npx_cmd, shell=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Need 2 arguments. <old color> <new color>')
        sys.exit(1)

    print(f'Recoloring: "{sys.argv[1]}" to "{sys.argv[2]}"')

    Recolor(sys.argv[1], sys.argv[2]).run()

    print('Recolor done')

