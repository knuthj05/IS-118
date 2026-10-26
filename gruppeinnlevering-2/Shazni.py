
# IS-118 - Gruppeinnlevering 2
# Interaktiv historie: Erling som prosjektleder

print("=" * 50)
print("ERLING: EN UTFORDRENDE PROSJEKTLEDERROLLE")
print("=" * 50)

print("\nErling leder et prosjekt for å utvikle en digital medborgerportal.")
print("Teamet har konflikter, og den første prototypen skal være klar om tre uker.")
print("Du spiller rollen som Erling. Valgene dine påvirker prosjektets utvikling.\n")


# BESLUTNINGSPUNKT 1: Silje og Elias

print("\n--- BESLUTNING 1: KONFLIKTEN MELLOM SILJE OG ELIAS ---")
print("Silje ønsker et kreativt design, mens Elias prioriterer sikkerhet og kostnader.")
print("A: Samle Silje og Elias til et felles møte.")
print("B: Snakke med dem hver for seg først.")

choice1 = input("Hva velger du? (A/B): ").strip().upper()

while choice1 not in ["A", "B"]:
    print("Ugyldig valg. Skriv A eller B.")
    choice1 = input("Hva velger du? (A/B): ").strip().upper()

if choice1 == "A":
    print("\nErling arrangerer et felles møte.")
    print("De får diskutert problemene, men møtet blir litt anspent.")
else:
    print("\nErling snakker med dem individuelt.")
    print("Begge får forklart sine bekymringer, men det tar tid å finne en løsning.")


# BESLUTNINGSPUNKT 2: Hamdi og Hallgeir

print("\n--- BESLUTNING 2: INNBYGGERMEDVIRKNING ---")
print("Hamdi ønsker å bruke kommunens eksisterende plattform.")
print("Hallgeir ønsker en mer åpen løsning for innbyggerne.")
print("A: Arrangere et møte for å finne et kompromiss.")
print("B: La dem prøve å finne en løsning selv foreløpig.")

choice2 = input("Hva velger du? (A/B): ").strip().upper()

while choice2 not in ["A", "B"]:
    print("Ugyldig valg. Skriv A eller B.")
    choice2 = input("Hva velger du? (A/B): ").strip().upper()

if choice2 == "A":
    print("\nErling arrangerer et møte.")
    print("Hamdi og Hallgeir diskuterer behovene sine og prøver å finne en felles løsning.")
else:
    print("\nErling lar dem arbeide videre hver for seg.")
    print("De får mer tid til arbeidet, men uenigheten kan vokse.")


# BESLUTNINGSPUNKT 3: TEAMETS MOTIVASJON

print("\n--- BESLUTNING 3: MOTIVASJON OG FREMDIFT ---")
print("Prototypen skal være klar om tre uker.")
print("A: Prioritere tillit, samarbeid og en teamaktivitet.")
print("B: Prioritere oppgaver og frister for å bli ferdig i tide.")

choice3 = input("Hva velger du? (A/B): ").strip().upper()

while choice3 not in ["A", "B"]:
    print("Ugyldig valg. Skriv A eller B.")
    choice3 = input("Hva velger du? (A/B): ").strip().upper()

if choice3 == "A":
    print("\nErling setter av tid til å styrke samarbeidet.")
    print("Teamet får mulighet til å bygge tillit, men fremdriften kan bli langsommere.")
else:
    print("\nErling prioriterer oppgaver og tidsfrister.")
    print("Teamet kan arbeide raskere, men konfliktene kan forbli uløste.")


# AVSLUTNING: BESTEM SLUTTRESULTATET

print("\n" + "=" * 50)
print("PROSJEKTETS SLUTTRESULTAT")
print("=" * 50)

# Et enkelt poengsystem basert på valgene

score = 0

if choice1 == "A":
    score += 1

if choice2 == "A":
    score += 1

if choice3 == "A":
    score += 1

if score >= 2:
    print("\nSLUTT 1: STYRKET SAMARBEID")
    print("Erling har prioritert dialog og relasjoner i minst to beslutninger.")
    print("Teamet får bedre muligheter til å gjenoppbygge tillit og gå mot norming-fasen.")

elif score == 1:
    print("\nSLUTT 2: DELVIS LØST")
    print("Noen utfordringer er håndtert, men andre gjenstår.")
    print("Teamet samarbeider videre, men relasjonene er fortsatt sårbare.")

else:
    print("\nSLUTT 3: PROSJEKTET FORSINKES")
    print("Erling har valgt å utsette dialog og prioritere andre oppgaver.")
    print("Konfliktene kan fortsette, og prosjektet risikerer å bli forsinket.")

print("\nTakk for at du spilte!")
