import pynvim


@pynvim.plugin
class PyRun(object):
    def __init__(self, vim):
        self.vim = vim
        self.python_buffer = None

    @pynvim.command('RunCell')
    def run_cell(self):
        if not self.python_buffer or not self.python_buffer.valid:
            self.vim.err_write('Please make sure to set a python window.\n')
            return
        code = self.get_code()
        self.python_buffer.append(code+'\n')

    @pynvim.command('SetRunWindow')
    def set_run_window(self):
        self.python_buffer = self.vim.current.buffer
        self.vim.command('term python')

    def get_code(self):
        cursor_row = self.vim.current.window.cursor[0]
        start_row = cursor_row
        end_row = cursor_row + 1
        delim = self.vim.eval("g:pyrun_delimiter")

        start_line = self.vim.current.buffer[start_row]
        while not start_line.startswith(delim) and start_row > 0:
            start_row -= 1
            if start_row > 0:
                start_line = self.vim.current.buffer[start_row]

        end_line = self.vim.current.buffer[end_row]
        while not end_line.startswith(delim) and end_row < len(self.vim.current.buffer):
            end_row += 1
            if end_row < len(self.vim.current.buffer):
                end_line = self.vim.current.buffer[end_row]

        return self.vim.current.buffer[start_row:end_row]
