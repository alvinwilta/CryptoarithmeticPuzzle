import os
import time

def loadfile(): #memilih file mana yang akan diparse
    entries = os.listdir("../test")
    i = 0
    for entry in entries:
        print(str(i) + ". " + entry)
        i+=1
    idx = input("ketik nomor teks yang ingin diparse: ")
    namafile = entries[int(idx)]
    return namafile
    
def parser(namafile,lines): #membaca file txt dan mengubahnya menjadi list
    with open("../test/"+namafile,"r") as f:
        lines = f.read().splitlines()
    return lines

def strip(lines): #membersihkan list dari karakter yang tidak digunakan
    del lines[len(lines)-2]
    i=0
    for line in lines:
        line = line.replace("+","")
        line = line.replace("-","")
        line = line.replace(" ","")
        lines[i] = line
        i += 1
    return lines

def cek_string(list_string): #mengecek apakah terdapat string >10 karakter
    cek = True
    for string in list_string:
        if len(string) > 10:
            cek = False
            break
    return cek

def ulang_program():
    x = input("Apakah anda masih inggin menggunakan program? (0/1)")
    if x==str(0):
        quit()
    elif x==str(1):
        main()
    else:
        print("Tolong masukkan dengan benar, 0 untuk tidak dan 1 untuk iya.")
        ulang_program()
        
def permutasi(xlist,r):
    ylist = tuple(xlist)
    n = len(ylist)
    indeks = list(range(n))
    siklus = list(range(n, n-r, -1))
    yield tuple(ylist[i] for i in indeks[:r])
    while n:
        for i in reversed(range(r)):
            siklus[i] -= 1
            if siklus[i] == 0:
                indeks[i:] = indeks[i+1:] + indeks[i:i+1]
                siklus[i] = n - i
            else:
                j = siklus[i]
                indeks[i], indeks[-j] = indeks[-j], indeks[i]
                yield tuple(ylist[i] for i in indeks[:r])
                break
        else:
            return

def unique_is(xlist): #mengeluarkan unique i pada string di dalam list
    unique = []
    for string in xlist:
        for i in range(len(string)):
            if (string[i] not in unique):
                unique.append(string[i])
    return unique

def jml_list(xlist):
    jml = 0
    i=0
    for i in range(len(xlist)-1):
        jml += int(xlist[i])
    return jml



def main():
    tebakan=[1,0,2,3,4,5,6,7,8,9]
    namafile = str("")
    lines = []
    namafile = loadfile()
    lines = parser(namafile,lines)
    lines = strip(lines) # stripped list
    if not cek_string(lines):
        print('Soal terkait memiliki operand yang melebihi 10 karakter dan tidak akan diproses.\n')
        ulang_program()
    else:
        start_time = time.time()
        tries = 0
        unique = unique_is(lines)
        for perm in permutasi(tebakan,len(unique)):
            kamus = dict(zip(unique,perm))
            operasi = []
            tdknol = True #melakukan pengecualian pada 0 di depan
            for string in lines:
                operand = []
                for i in string:
                    operand.append(str(kamus[i]))
                temp = "".join(operand)
                operasi.append(temp)
            #print(operasi)
            jumlah = jml_list(operasi)
            tries += 1
            if ((jumlah == int(operasi[len(operasi)-1]))): #mengecek apakah ada 0 di depan
                for i in range(len(operasi)):
                    if (int(operasi[i][0]) == 0):
                        tdknol = False
                        break
                if tdknol:
                    for j in range(len(operasi)):
                        if (j == len(operasi)-1):
                            print("------------")
                        print(lines[j]," : ",end="")
                        print(operasi[j])
                    break
        print("Jumlah Kasus yang diuji : ",tries)
        print("Program selesai selama %s detik" % (time.time() - start_time))
        ulang_program()

main()