import PyPDF2
import pyttsx3
from deep_translator import GoogleTranslator

def readFile(path, N):
    assistante = pyttsx3.init()

    livre = open(path, "rb")
    lecture = PyPDF2.PdfReader(livre)
    pages = len(lecture.pages)
    debutlecture = lecture.pages[0]
    texte = debutlecture.extract_text()

    print("* Le texte en français:")
    traductionFile = GoogleTranslator(source="auto", target="fr").translate_file(path)
    print(traductionFile)

    while N < 1 or N > 5:
        N = int(input("Choisissez un nombre entre 1 et 5 : "))

    if N == 1:
        print("Traduction en Anglais: \n")
        traductionFile = GoogleTranslator(source="auto", target="en").translate_file(path)
        print(traductionFile)
        assistante.say(traductionFile)

    elif N == 2:
        print("Traduction en Italienne: \n")
        traductionFile = GoogleTranslator(source="auto", target="it").translate_file(path)
        print(traductionFile)
        assistante.say(traductionFile)

    elif N == 3:
        print("Traduction en Allemande:\n ")
        traductionFile = GoogleTranslator(source="auto", target="de").translate_file(path)
        print(traductionFile)
        assistante.say(traductionFile)

    elif N == 4:
        print("Traduction en Espaniol: \n")
        traductionFile = GoogleTranslator(source="auto", target="es").translate_file(path)
        print(traductionFile)
        assistante.say(traductionFile)

    elif N == 5:
        print("Traduction en Russian: \n")
        traductionFile = GoogleTranslator(source="auto", target="ru").translate_file(path)
        print(traductionFile)
        assistante.say("ahmed." + traductionFile)

    assistante.runAndWait()
