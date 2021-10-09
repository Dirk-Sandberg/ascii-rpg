from kivy.uix.label import Label

kv = """
<TextLog>:
    text: ''
    Label:
        text: root.text
"""
class TextLog(Label):
    def add_line(self, line):
        # This could go in a separate class for the Log text area
        lines = []
        colors = ['CCCCCC', '999999', '666666', '333333']
        current_lines = self.text.splitlines()[::-1]
        for i, text in enumerate(current_lines):
            if i < 4:
                text = text[text.find(']')+1:text.find('[/')]
                text = f'[color={colors[i]}]{text}[/color]'
                lines.append(text)
        while len(lines) < 2:
            lines = ['\n'] + lines
        lines = lines[::-1]
        lines.append(f'[color=FFFFFF]{line}[/color]')
        self.text = '\n'.join(x for x in lines)
