nactena_data=[]
pocet = 0
pozice_x = 0
pozice_y = 1
dalsi_precteni = False 
soubor = open("input.txt")
for radek_souboru in soubor:
    udej_na_radku = radek_souboru[:-1]
    
    ciselny_udej = int(udej_na_radku)
    nactena_data.append(ciselny_udej)
soubor.close()

#print(nactena_data)
for i, cislo in enumerate(nactena_data):
    while True:
        y = nactena_data[pozice_y]
        x = nactena_data[pozice_x]
            
        if x < y:
            pozice_x = pozice_x + 1
            pozice_y = pozice_y + 1
            x = y
            
            pocet = pocet + 1
            print(x,"//  vetší","pocet =", pocet )
            dalsi_precteni = True
        if x > y:
            pocet = pocet
            pozice_x = pozice_x + 1
            pozice_y = pozice_y + 1
            
#while True:
 #   if i == len(nactena_data):
  #      break
