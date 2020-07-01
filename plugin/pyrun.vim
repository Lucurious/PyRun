call remote#host#RegisterPlugin('python3', '/home/luc/dot/config/nvim/plugged/PyRun/rplugin/python3/pyrun.py', [
      \ {'sync': v:false, 'name': 'RunCell', 'type': 'command', 'opts': {}},
      \ {'sync': v:false, 'name': 'SetRunWindow', 'type': 'command', 'opts': {}},
      \ ])

if !exists('g:pyrun_delimiter')
    let g:pyrun_delimiter = '#$#'
endif
