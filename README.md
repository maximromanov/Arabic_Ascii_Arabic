# Arabic_Ascii_Arabic (Python 3.4)

The script converts Arabic text into an ASCII transliteration that can be used with text analysis programs that do not support Arabic script (for example, R for Windows).

[Python 3.4 must be installed; earlier versions work with Unicode files differently]

1. Put your texts into ./originals/
2. Run the script (on Windows, a double-click on the script "translit_converter.py" should do the trick)
3. New files will appear in ./ascii/ and in ./arabic/

The script (translit_converter.py) does the following:
1. removes all short vowels
2. replaces all Latin letters and numbers with "@"
3. transliterates Arabic into ASCII characters (saving into ./ascii/)
4. transliterates ASCII back into Arabic (saving into ./arabic/)---for control purposes mostly

Transliteration Table (Simplified Buckwalter):

    'ء'  : 'c',
    'ؤ'  : 'u',
    'ئ'  : 'i',
    'ا'  : 'A',
    'إ'  : 'I',
    'أ'  : 'a',
    'آ'  : 'O',
    'ب'  : 'b',
    'ة'  : 'o',
    'ت'  : 't',
    'ث'  : 'v',
    'ج'  : 'j',
    'ح'  : 'H',
    'خ'  : 'x',
    'د'  : 'd',
    'ذ'  : 'V',
    'ر'  : 'r',
    'ز'  : 'z',
    'س'  : 's',
    'ش'  : 'E',
    'ص'  : 'S',
    'ض'  : 'D',
    'ط'  : 'T',
    'ظ'  : 'Z',
    'ع'  : 'C',
    'غ'  : 'g',
    'ف'  : 'f',
    'ق'  : 'q',
    'ك'  : 'k',
    'ل'  : 'l',
    'م'  : 'm',
    'ن'  : 'n',
    'ه'  : 'h',
    'و'  : 'w',
    'ى'  : 'Y',
    'ي'  : 'y',

