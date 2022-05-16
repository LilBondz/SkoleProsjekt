# Lager en funksjon som spørr hva du har lyst til å gjøre
def meny():
    # Printer tekst med valg om hva du vill gjøre
    print("Velg et valg:")
    print("1: Registrer deltaker")
    print("2: List ut deltakere")
    print("3: Registrer tid på deltaker")
    print("0: Avslutt")
    # Henter brukerens valg og lagrer i en variabel
    valg = int(input("Valg: "))
    # Returnerer valget så programmet vet hva funksjonen kom fram til
    return valg

# Funksjon for registrering av en deltaker
def registrerDeltaker():
    # Printer at brukeren skal registrere en deltaker
    print("Registrer deltaker")
    # henter bruker input for fornavnet til deltakeren
    fornavn = input("Fornavn: ")
    # henter bruker input for etternavnet til deltakeren
    etternavn = input("Etternavn: ")
    # henter bruker input for deltakerens deltakernummer
    deltakernummer = input("Deltakerens nummer: ")
    # Putter alle variablene brukeren har skrevet inn i en dictionary
    deltaker = {"fornavn":fornavn, "etternavn":etternavn, "nr":deltakernummer, "tid":0}
    # Returnerer deltaker dictionaryen
    return deltaker

# Funksjon for å printe ut alle deltakerene
def listUtDeltakere(deltakere):
    # printer ut infor om at deltakerne blir listet ut
    print("Lister ut deltakere")
    # Kjører en for loop for hver deltaker i deltakere listen
    for deltaker in deltakere:
        # Printer en tom linje
        print("")
        # Printer ut deltakernummer
        print(f'Deltakernummer: {deltaker["nr"]}')
        # printer ut fornavnet på deltakeren
        print(f'fornavn: {deltaker["fornavn"]}')
        # Printer ut etternavn
        print("Etternavn: " + deltaker["etternavn"])
        # Printer ut tiden på deltakeren
        print(f"Tid: {deltaker['tid']}")

# Lager funksjon for registrering av tid en deltaker fikk
def registrerTid():
    # Printer registreting av tid
    print("Registrering av tid")
    # Funksjonen er ikke ferdig utviklet så funksjonen informerer bare brukeren om dette
    print("Funksjonen er ikke utviklet :) ")
    return

# Main funksjon som styrer hele programmet
def main():
    # Lager en deltakere liste
    deltakere = []
    # Starter en uendelig loop
    while True:
        # Printer at programmet løpetider
        print("Program Løpetider.")
        # Blank linje
        print("")
        # lager en variabel som heter valg som får data fra return fra meny funksjonen
        valg = meny()
        # Hvis vlag variabelen er 0
        if valg == 0:
            # Stopper den loopen og programmet stopper
            break
        # Elles hvis valg er 1
        elif valg == 1:
            # Lager deltaker variabel med return fra registrer deltaker
            deltaker = registrerDeltaker()
            # Legger dictionaryen fra deltaker inn i deltakere listen
            deltakere.append(deltaker)
        # Ellers hvis vlag er 2
        elif valg == 2:
            # Kjører den list ut deltakere funksjonen med deltakere listen som variabel
            listUtDeltakere(deltakere)
        # Ellers hvis valg er 3
        elif valg == 3:
            # Kjører funksjon for registreting av tid på en deltaker
            registrerTid()
        # Hvis vlag ikke er en av de forrige tallene
        else:
            # Printer den ut at menyvalget ikke finnes
            print("Menyvalget finnes ikke")

# Starter main funksjonen
main()