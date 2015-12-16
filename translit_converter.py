# generate MONK labels for Arabic
import os, re

def deNoise(text):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return(text)

def removeNonArabic(text):
    text = re.sub("[A-Za-z0-9]", "@", text)
    return(text)

def dictReplace(text, dic):
    for k, v in dic.items():
        text = text.replace(k, v)
    return(text)

def dictReplaceRev(text, dic):
    for k, v in dic.items():
        text = text.replace(v, k)
    return(text)

translit = {
    '،'   : ',',
# letters
    'ء'  : 'c',
    'ؤ'  : 'u',
    'ئ'  : 'i',
    'ا'  : 'A',
    'إ'  : 'i',
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
}

sFolder  = "./originals/"
t1Folder = "./ascii/"
t2Folder = "./arabic/"

def converter(fileName):
    with open(sFolder+fileName, "r", encoding="utf8") as f1:
        f1 = f1.read()
        
        
        ar = deNoise(f1)
        ar = removeNonArabic(ar)

        tranAr = dictReplace(ar, translit)
        ArRev = dictReplaceRev(tranAr, translit)

        with open(t1Folder+fileName, "w", encoding="utf8") as f9:
            f9.write(tranAr)
        with open(t2Folder+fileName, "w", encoding="utf8") as f9:
            f9.write(ArRev)        
        print("File %s has been converted..." % fileName)
        
def main():
    lof = os.listdir(sFolder)
    for f in lof:
        converter(f)

main()
    



        
