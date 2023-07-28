from cx_Freeze import setup, Executable

# add files
files = ['images/calculator.ico']

# target
target = Executable(
    script="calculator.py",
    base="Win32GUI",
    icon="images/calculator.ico"
)


# setup cx_Freeze
setup(
    name="Calculator",
    version="1.0",
    description="calculator for basic operations",
    author="Meriam Zahra",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)
