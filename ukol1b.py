nactena_data=[]
pozice1 = 1 # 1
pozice2 = 2 # 2
pozice3 = 3 # 3
pocet = 0
dalsi_precteni = False 
soubor = open("input.txt")
for radek_souboru in soubor:
    udej_na_radku = radek_souboru[:-1]
    
    ciselny_udej = int(udej_na_radku)
    nactena_data.append(ciselny_udej)
    
soubor.close()

"""while True:
    print(nactena_data)"""
    
for i, trojice in enumerate(nactena_data):
    soucet_prvni_trojice = nactena_data[0] + nactena_data[1] + nactena_data[2]
    x = soucet_prvni_trojice
    print(x)
    """if not dalsi_precteni:
        soucet_trojice = soucet_prvni_trojice
    if x < soucet_trojice:
        x = soucet_trojice
        pocet = pocet + 1
        pozice1 = pozice1 + 1
        pozice2 = pozice2 + 1
        pozice3 = pozice3 + 1
        
        print(x,"// je vetší", " pocet je", pocet)
        dalsi_precteni = True
    else:
        pozice1 = pozice1 + 1
        pozice2 = pozice2 + 1
        pozice3 = pozice3 + 1
        x = soucet_trojice
        dalsi_precteni = True
    if dalsi_precteni:
        soucet_trojice = (nactena_data[pozice1]) + (nactena_data[pozice2]) + (nactena_data[pozice3])"""
        
        
    