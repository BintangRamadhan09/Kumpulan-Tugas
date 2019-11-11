nilai = 85
if nilai > 80 :
    print(f'Nilai Anda {nilai}, Anda Lulus!')
elif nilai < 40 :
    print(f'Nilai Anda {nilai},Anda tidak lulus')
else :
    print(f'Nilai Anda {nilai},Anda Remedial')

jomblo = True; nganggur =True

if jomblo == True and nganggur == True:
    print('Anda jomvlo pengangguran')
elif jomblo and not nganggur:
    print('Anda Kurang Piknik')
elif not jomblo and nganggur:
    print('Anda kurang asoy')
else:
    print('Anda Tajir')


# Tugas 

nilai = 45 

if nilai >= 82:
    print('A')
elif nilai >= 72 and nilai <= 81:
    print('B')
elif nilai >= 62 and nilai <= 71:
    print('C')
elif nilai >= 52 and nilai <= 62:
    print('D')
else:
    print('E')