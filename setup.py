from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['numpy','pandas','bs4','requests','json','sqlite3','xlwings','tkinter'], 'excludes': []}

base = None

executables = [
    Executable('main.py', base=base)
]

setup(name='AWS Analyze',
      version = '1.0',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
