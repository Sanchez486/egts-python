# EGTS Python lib + translator for egts and wialon
Installation steps are very messy, sorry about that:
1. Go to egts-python (project root directory)
2. Make a copy of setup_egts.py and rename it to setup.py
3. Run "python setup.py install"
4. Run "pip install ."
5. Delete setup.py, then make a copy of setup_yandex_translator.py and rename it to setup.py
6. Run "python setup.py install"
7. Run "pip install ."
8. cd yandex_translator_exe/
9. Run "pyinstaller egts-translator.py --onefile --hidden-import=yandex_translator"
10. You can find your output exe file in yandex_translator_exe\dist\egts-translator.exe
