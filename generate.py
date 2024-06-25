import os
import pathlib


class Generator:
    def __init__(self) -> None:
        self.html_template = pathlib.Path('src/template.html')
        self.html_index = pathlib.Path('src/index.html')
        self.entries_path = pathlib.Path('entries')

    def open_entry(self, entry_file: pathlib.Path) -> str | list:
        with open(entry_file, 'r', encoding='utf8') as f:
            return self.replace_nl(f.read())

    def inject_into_html(self, contents: list[list]) -> None:
        with open(self.html_template, 'r', encoding='utf8') as fr:
            html_template_file = fr.readlines()

        new_html_buffer = []

        pattern = lambda a: '{{' + f'{a}_content' + '}}'
        content_ids = [pattern(x[1]) for x in contents]

        for line in html_template_file:
            if line.strip() == '{{projects_template}}':
                new_html_buffer.append(self.read_project_template(line))
            elif line.strip() in content_ids:
                index = content_ids.index(line.strip())
                new_html_buffer.append(self.add_space_tab(line) + contents[index][0])
            else:
                new_html_buffer.append(line)

        with open(self.html_index, 'w+', encoding='utf8') as fw:
            fw.writelines(new_html_buffer)

    def read_project_template(self, current_line: str) -> str:
        with open(self.entries_path / 'projects.html', 'r', encoding='utf8') as f:
            template = f.readlines()
            new_template = []

            for line in template:
                new_template.append(self.add_space_tab(current_line) + line)

            return ''.join(new_template)

    @staticmethod
    def add_space_tab(current_line: str) -> str:
        w_count = 0
        t_count = 0
        w_count += current_line.count(' ')
        t_count += current_line.count('\t')
        return '\t'*t_count + ' '*w_count

    @staticmethod
    def replace_nl(text_input: str) -> str:
        html_br = '<br>'
        return text_input.replace('\n', html_br).replace('\r\n', html_br)

    def update(self) -> None:
        entries = os.listdir(self.entries_path)
        entries_path = [self.entries_path / pathlib.Path(file) for file in entries]
        entries_content = []

        for file in entries_path:
            entry = self.open_entry(file)
            entries_content.append([entry, file.stem])
        self.inject_into_html(entries_content)


if __name__ == "__main__":
    print('Updating from entry files ...')
    Generator().update()

