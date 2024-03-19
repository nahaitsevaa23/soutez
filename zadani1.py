nactena_data=[]
soubor = open("input.txt")
for radek_souboru in soubor:
    udej_na_radku = radek_souboru[:-1]
    
    ciselny_udej = int(udej_na_radku)
    nactena_data.append(ciselny_udej)
soubor.close()
#print(nactena_data)
for i, cislo in enumerate(nactena_data):
    x = nactena_data[0]
    if x < cislo and  x<8113:
        x = cislo
        print(x,"//  vetší")
    
    else:()
#while True:
 #   if i == len(nactena_data):
  #      break
