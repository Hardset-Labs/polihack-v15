class LearningMinutesDayMockup:
    def __init__(self, chapter, question, answer, dummy_answers, explanation):
        self.chapter = chapter
        self.question = question
        self.answer = answer
        self.dummy_answers = dummy_answers
        self.explanation = explanation

    def __str__(self):
        return f"Chapter: {self.chapter}\nQuestion: {self.question}\nAnswer: {self.answer}\nDummy Answers: {self.dummy_answers}\nExplanation: {self.explanation}"

class ChapterMockup:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __str__(self):
        return f"Chapter: {self.name}\nQuestions: {len(self.questions)}"

class QuestionMockup:
    def __init__(self, question, answer, dummy_answers, explanation):
        self.question = question
        self.answer = answer
        self.dummy_answers = dummy_answers
        self.explanation = explanation

    def __str__(self):
        return f"Question: {self.question}\nAnswer: {self.answer}\nDummy Answers: {self.dummy_answers}\nExplanation: {self.explanation}"

def parse_text(text):
    chapters = []
    questions = []

    lines = text.replace('\n\n', '\n').replace('    ', '').split('\n')
    print(lines)
    for line in lines:
        if line.startswith('chapter'):
            if questions:
                chapters.append(ChapterMockup(chapter_name, questions))
                questions = []
            chapter_name = line.split(': "')[1].replace('"', '')
        elif line.startswith('question'):
            question = line.split(': "')[1].replace('"', '')
        elif line.startswith('answer'):
            answer = line.split(': "')[1].replace('"', '')
        elif line.startswith('dummy_answer1'):
            dummy_answer1 = line.split(': "')[1].replace('"', '')
        elif line.startswith('dummy_answer2'):
            dummy_answer2 = line.split(': "')[1].replace('"', '')
        elif line.startswith('dummy_answer3'):
            dummy_answer3 = line.split(': "')[1].replace('"', '')
        elif line.startswith('explanation'):
            explanation = line.split(': "')[1].replace('"', '')
            questions.append(QuestionMockup(question, answer, [dummy_answer1, dummy_answer2, dummy_answer3], explanation))

    return chapters

if __name__ == '__main__':
    # Example text
    example_text = """
    chapter1: "Analiza sistemelor utilizand locul radacinilor 1"
    question1: "Care sunt caracteristicile de baza ale raspunsului tranzitoriu a unui sistem in bucla inchisa?"
    answer1: "Legate de localizarea polilor sistemului inchis."
    dummy_answer1_1: "Depind de numarul de zerouri."
    dummy_answer2_1: "Nu sunt importante."
    dummy_answer3_1: "Sunt complet aleatorii."
    explanation1: "Caracteristicile de baza ale raspunsului tranzitoriu sunt legate de pozitia polilor sistemului inchis."
    
    question2: "De ce este important sa determinam cum se modifica polii in planul s cand parametrul sistemului este variabil?"
    answer2: "Pentru a intelege influenta variabilei asupra stabilitatii sistemului."
    dummy_answer1_2: "Nu este important sa se faca aceasta determinare."
    dummy_answer2_2: "Nu exista variatie in pozitia polilor cu modificarea parametrului."
    dummy_answer3_2: "Polii nu se schimba niciodata."
    explanation2: "Determinarea modului in care se modifica polii este esentiala pentru analiza stabilitatii sistemului."
    
    question3: "Ce reprezinta locul radacinilor intr-un sistem analizat?"
    answer3: "Reprezentarea grafica a radacinilor ecuatiei caracteristice a sistemului inchis."
    dummy_answer1_3: "Un set de numere complexe aleatoare."
    dummy_answer2_3: "O abordare teoretica fara legatura cu realitatea."
    dummy_answer3_3: "O simpla supozitie despre comportamentul sistemelor."
    explanation3: "Locul radacinilor ofera o reprezentare grafica a pozitiilor polilor sistemului in functie de un parametru."
    
    question4: "Care este conditia de faza pentru locul radacinilor?"
    answer4: "Conditia de faza este de ±180 grade (π radiani) pentru unghiul polilor."
    dummy_answer1_4: "Conditia de faza este de ±90 grade."
    dummy_answer2_4: "Conditia de faza este de ±270 grade."
    dummy_answer3_4: "Conditia de faza este de 0 grade."
    explanation4: "Conditia de faza indica un unghi de ±180 grade pentru pozitia polilor pe locul radacinilor."
    
    question5: "Ce reprezinta functia de transfer a sistemului deschis?"
    answer5: "Hd(s) = kG(s)H(s)."
    dummy_answer1_5: "Hd(s) = G(s) / H(s)."
    dummy_answer2_5: "Hd(s) = G(s) + H(s)."
    dummy_answer3_5: "Hd(s) = kG(s) / H(s)."
    explanation5: "Functia de transfer a sistemului deschis este Hd(s) = kG(s)H(s), unde k este un parametru variabil."
    
    chapter2: "Analiza sistemelor utilizand locul radacinilor 2"
    question1: "Care sunt polii sistemului deschis pentru functia de transfer kG(s) = k1 / (s(s + 2))?"
    answer1: "Polii sistemului deschis sunt 0 si -2, care nu depind de k."
    dummy_answer1_1: "Polii sistemului deschis sunt 1 si 2."
    dummy_answer2_1: "Polii sistemului deschis sunt -1 si 1."
    dummy_answer3_1: "Polii sistemului deschis sunt -3 si 2."
    explanation1: "Polii sistemului deschis pentru aceasta functie de transfer sunt 0 si -2, independent de variatia lui k."
    
    question2: "Cum se modifica polii sistemului inchis pentru functia de transfer kG(s) = k1 / (s(s + 2)) in functie de k?"
    answer2: "Polii sistemului inchis depind de k si se deplaseaza in planul s."
    dummy_answer1_2: "Polii sistemului inchis sunt statici si nu se schimba cu k."
    dummy_answer2_2: "Polii sistemului inchis sunt invers proportionali cu k."
    dummy_answer3_2: "Polii sistemului inchis sunt irelevanti."
    explanation2: "Polii sistemului inchis variaza in pozitie conform cu modificarea parametrului k."
    
    question3: "Ce reprezinta raspunsul la treapta sub-amortizat in cazul functiei de transfer kG(s) = 50 / (s^2 + 2s + 50)?"
    answer3: "Raspunsul la treapta este oscilant."
    dummy_answer1_3: "Raspunsul la treapta este critic amortizat."
    dummy_answer2_3: "Raspunsul la treapta este supra-amortizat."
    dummy_answer3_3: "Raspunsul la treapta este sub-amortizat."
    explanation3: "Pentru aceasta functie de transfer, un raspuns la treapta sub-amortizat duce la oscilatii in sistem."
    
    question4: "Ce reprezinta locul radacinilor pentru toate valorile unui parametru din sistem?"
    answer4: "Locul radacinilor este reprezentarea grafica a radacinilor ecuatiei caracteristice a sistemului inchis pentru toate valorile unui parametru din sistem."
    dummy_answer1_4: "Locul radacinilor nu are nicio relevanta pentru parametrii sistemului."
    dummy_answer2_4: "Locul radacinilor reprezinta doar polii sistemului deschis."
    dummy_answer3_4: "Locul radacinilor se refera doar la zerourile sistemului."
    explanation4: "Locul radacinilor ofera o reprezentare grafica a evolutiei polilor sistemului inchis in functie de un parametru variabil."
    
    question5: "Ce conditie trebuie sa indeplineasca un raport de polinoame ın kG(s)H(s) pentru a se incadra ın locul radacinilor?"
    answer5: "Conditia de faza trebuie sa fie ±180o(2q+1), q=0,1,2,..."
    dummy_answer1_5: "Conditia de faza trebuie sa fie ±90o(2q), q=0,1,2,..."
    dummy_answer2_5: "Conditia de faza trebuie sa fie 0o."
    dummy_answer3_5: "Conditia de faza trebuie sa fie ±180o(2q), q=0,1,2,..."
    explanation5: "Conditia de faza specifica un unghi de ±180o(2q+1) care trebuie fi indeplinit pentru a se incadra in locul radacinilor."
    
    chapter3: "Analiza sistemelor utilizand locul radacinilor 3"
    question1: "Cum se calculeaza valoarea absoluta a unui numar complex?"
    answer1: "|s| = sqrt(a^2 + b^2)"
    dummy_answer1_1: "|s| = a + b"
    dummy_answer2_1: "|s| = a - b"
    dummy_answer3_1: "|s| = a * b"
    explanation1: "Valoarea absoluta a unui numar complex (s) este radical din suma patratelor partilor reale si imaginare."
    
    question2: "Cum se masoara faza unui numar complex?"
    answer2: "Faza se masoara de la axa reala pozitiva ın sens trigonometric."
    dummy_answer1_2: "Faza se masoara de la axa reala negativa ın sens trigonometric."
    dummy_answer2_2: "Faza se masoara de la axa imaginara pozitiva."
    dummy_answer3_2: "Faza se masoara de-a lungul diagonalei."
    explanation2: "Faza unui numar complex se masoara de la axa reala pozitiva ın sens trigonometric."
    
    question3: "Ce reprezinta produsul a doua numere complexe?"
    answer3: "Produsul a doua numere complexe este un alt numar complex."
    dummy_answer1_3: "Produsul a doua numere complexe este mereu real."
    dummy_answer2_3: "Produsul a doua numere complexe este un numar rational."
    dummy_answer3_3: "Produsul a doua numere complexe nu este definit."
    explanation3: "Produsul a doua numere complexe rezulta intr-un alt numar complex, avand o parte reala si o parte imaginara."
    
    question4: "Care este formula pentru calcularea raportului a doua numere complexe?"
    answer4: "s1 / s2 = |s1| / |s2| * sqrt(a1^2 + b1^2) / sqrt(a2^2 + b2^2) * exp(i * (arctan(b1/a1) - arctan(b2/a2)))"
    dummy_answer1_4: "s1 / s2 = |s1 * s2|"
    dummy_answer2_4: "s1 / s2 = |s1 - s2|"
    dummy_answer3_4: "s1 / s2 = sqrt(s1) * sqrt(s2)"
    explanation4: "Formula pentru calcularea raportului a doua numere complexe implica raportul modulului si diferenta fazei acestora."
    
    question5: "Ce reprezinta faza lui r + 3 pentru un numar complex r?"
    answer5: "Unghiul de la axa reala pozitiva la linia care uneste r cu radacina lui r + 3."
    dummy_answer1_5: "Faza lui r + 3 este mereu 0 grade."
    dummy_answer2_5: "Faza lui r + 3 este invers proportionala cu r."
    dummy_answer3_5: "Faza lui r + 3 este constanta indiferent de r."
    explanation5: "Faza lui r + 3 reprezinta unghiul masurat in sens trigonometric de la axa reala pozitiva la linia care uneste r cu radacina lui r + 3."
    
    chapter4: "Analiza sistemelor utilizand locul radacinilor 4"
    question1: "Ce reprezinta punctul de desprindere de pe axa reala intr-un loc al radacinilor?"
    answer1: "Punctul de desprindere reprezinta locul unde locul radacinilor incepe dintr-un pol si se termina la un zero sau la infinit."
    dummy_answer1_1: "Punctul de desprindere nu are semnificatie."
    dummy_answer2_1: "Punctul de desprindere este un punct fix indiferent de ecuatia caracteristica."
    dummy_answer3_1: "Punctul de desprindere este mereu la origine."
    explanation1: "Punctul de desprindere indica inceputul locului radacinilor care vine dintr-un pol si se termina la un zero sau la infinit."
    
    question2: "Cum se determina numarul de ramuri ale locului radacinilor?"
    answer2: "Numarul de ramuri este dat de numarul de poli ai sistemului deschis (np)."
    dummy_answer1_2: "Numarul de ramuri este dat de numarul de zerouri ai sistemului deschis."
    dummy_answer2_2: "Numarul de ramuri este constant pentru orice sistem."
    dummy_answer3_2: "Numarul de ramuri este dat de numarul de ramuri imaginare."
    explanation2: "Numarul de ramuri ale locului radacinilor este determinat de numarul de poli ai sistemului deschis."
    
    question3: "Ce reprezinta simetria locului radacinilor fata de axa reala?"
    answer3: "Locul radacinilor este simetric fata de axa reala, avand aceeasi forma de o parte si de alta a acesteia."
    dummy_answer1_3: "Locul radacinilor este complet asimetric."
    dummy_answer2_3: "Locul radacinilor este doar parțial simetric."
    dummy_answer3_3: "Locul radacinilor nu are nicio regula de simetrie."
    explanation3: "Simetria locului radacinilor fata de axa reala indica aceeasi configuratie a radacinilor de o parte si de alta a axei."
    
    question4: "Cum se localizeaza segmentele de pe axa reala care apartin locului radacinilor?"
    answer4: "Segmentele de pe axa reala apartin locului radacinilor daca sunt intre un numar impar de poli si zerouri ai sistemului deschis."
    dummy_answer1_4: "Segmentele de pe axa reala sunt oricare cu exceptia celor la extremitati."
    dummy_answer2_4: "Segmentele de pe axa reala apartin doar locului radacinilor daca intalnesc un pol."
    dummy_answer3_4: "Segmentele de pe axa reala apartin locului radacinilor doar daca tind spre zero."
    explanation4: "Segmentele de pe axa reala fac parte din locul radacinilor daca sunt intre un numar impar de poli si zerouri ai sistemului deschis."
    
    question5: "Cum se deteremina unghiul de plecare din polii complecsi si unghiul cu care locul radacinilor ajunge in zerouri?"
    answer5: "Unghiul de plecare din polii complecsi si unghiul de ajungere in zerouri se determina din conditia de faza a locului radacinilor."
    dummy_answer1_5: "Unghiul de plecare din polii complecsi este mereu 90 de grade."
    dummy_answer2_5: "Unghiul de plecare este diferit in functie de modulul polilor."
    dummy_answer3_5: "Unghiul de plecare nu are importanta pentru locul radacinilor."
    explanation5: "Unghiurile de plecare din polii complecsi si de ajungere in zerouri sunt stabilite de cerintele de faza ale locului radacinilor."
    
    chapter5: "Analiza sistemelor utilizand locul radacinilor 5"
    question1: "Care este explicatia conceptului de loc radacinilor si relevanta acestuia in analiza sistemelor?"
    answer1: "Locul radacinilor este reprezentarea grafica a evolutiei polilor sistemului ınchis pentru diverse valori ale unui parametru din sistem, fiind esential pentru analiza stabilitatii si comportamentului sistemelor."
    dummy_answer1_1: "Locul radacinilor nu are nicio importanta in analiza sistemelor."
    dummy_answer2_1: "Locul radacinilor este obscur si greu de inteles."
    dummy_answer3_1: "Locul radacinilor este doar o reprezentare estetica a polilor."
    explanation1: "Locul radacinilor ofera o perspectiva grafica a modului in care variaza pozitiile polilor sistemului ınchis in functie de un parametru, fiind esential pentru evaluarea stabilitatii sistemelor."
    
    question2: "Ce reprezinta criteriul Routh-Hurwitz in contextul locului radacinilor?"
    answer2: "Criteriul Routh-Hurwitz se foloseste pentru a identifica intersectia cu axa imaginara a locului radacinilor si pentru a evalua stabilitatea sistemelor."
    dummy_answer1_2: "Criteriul Routh-Hurwitz este irelevant pentru locul radacinilor."
    dummy_answer2_2: "Criteriul Routh-Hurwitz se ocupa exclusiv de analiza polilor reali."
    dummy_answer3_2: "Criteriul Routh-Hurwitz este aplicabil doar sistemelor lineare."
    explanation2: "Criteriul Routh-Hurwitz ofera informatii despre intersectia cu axa imaginara pe locul radacinilor si ajuta la evaluarea stabilitatii sistemelor."
    
    question3: "Cum se determina punctul de desprindere in cadrul locului radacinilor si care este relevanta sa?"
    answer3: "Pentru a determina punctul de desprindere, se calculeaza solutiile ecuatiei caracteristice derivate si se determina unghiul de plecare, fiind relevant pentru identificarea comportamentului sistemului la limita."
    dummy_answer1_3: "Punctul de desprindere nu are o validitate practica."
    dummy_answer2_3: "Punctul de desprindere este irelevant in analiza sistemelor."
    dummy_answer3_3: "Punctul de desprindere indica punctul de origine pe locul radacinilor."
    explanation3: "Determinarea punctului de desprindere ajuta la identificarea comportamentului sistemului in situatii limita si la evaluarea sa in conditii critice."
    
    question4: "Care este relevanta asimptotelor in contextul locului radacinilor?"
    answer4: "Asimptotele ofera informatii despre directia si comportamentul locului radacinilor pe masura ce acesta se extinde spre infinit, permitand o interpretare grafica a stabilitatii sistemelor."
    dummy_answer1_4: "Asimptotele nu influenteaza locul radacinilor si nu ofera informatii relevante."
    dummy_answer2_4: "Asimptotele se refera doar la pozitia polilor."
    """

    # Parse the text
    parsed_data = parse_text(example_text)

    # Print the parsed data
    for chapter in parsed_data:
        print(chapter)
        for question in chapter.questions:
            print(question)
