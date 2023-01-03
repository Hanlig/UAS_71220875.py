from os import system
d_nama_kegiatan = ("HMTI 2022")
d_tanggl_kegiatan = ("tahun 2022-2023")
d_pilahan_kategori_kegiatan = ()

def judul(presentasi):
    print("organisasi")
    print("kepanitiaan")
    print("rekogmisi")

    menupilih = (input('oRgAnIsAsI'))

    if menupilih == '1':
        dosen()
    elif menupilih == '2':
        mahasiswa()
    elif menupilih == '3' :
        exit()
    else:
        system('cls')
        menu()

def kegiatan(menampilkan_jumlah_poin):
    print(1):
    print('\n')
    kode = input('Masuk : iaa 2022')
    if kode == 'admin' or kode == 'ADMIN':
        menu_dosen()
    else:
        salah = input('Kode salah')
        dosen()

    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        ubah()
    elif pilih2 == '4':
        hapus()
    elif pilih2 == '5':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        system('cls')
        menu_dosen()

def tambah():
    system('cls')
    judul()
    print('Tambah Data'.center(40))
    print('=====================================')
    jurusan = input ('Prodi [TI/SI] : ')
    if jurusan == 'TI' or jurusan == 'ti':
        j = 'Teknik Infomatika'
        d_jurusan.append(j)
    elif jurusan == 'SI' or jurusan == 'si':
        j = 'Sistem Informasi'
        d_jurusan.append(j)
    else:
        kembali = input('Pilihan Tidak Ada')
        tambah()
    nama = input('Nama  : ')
    d_nama.append(nama)
    nim = input('Nim   : ')
    d_nim.append(nim)
    kelas = input('Kelas :')
    d_kelas.append(kelas)

    system('cls')
    judul()
    print('Tambah Data'.center(40))
    print('=====================================')
    hadir = float(input('Jumlah Hadir : '))
    j_hadir = ((hadir/16)*20/100)*100
    d_hadir.append(j_hadir)

    tugas = float(input('Nilai Tugas  :'))
    j_tugas = tugas*(25/100)
    d_tugas.append(j_tugas)

    uts = float(input('Nilai UTS  :'))
    j_uts = uts*(25/100)
    d_uts.append(j_uts)

    uas = float(input('Nilai UAS  : '))
    j_uas = uas*(30/100)
    d_uas.append(j_uas)

    total = j_hadir+j_tugas+j_uts+j_uas
    d_akhir.append(total)
    print ('Data Tersimpan'.center(40))
    kembali = input('Kembali [enter]')
    menu_dosen()

def lihat():
    system('cls')
    judul()

    for i in range (len(d_nim)):

        print('%d. Nama        : %s'%(i+0, d_nama[i]))
        print('    Nim         : %s'%d_nim[i])
        print('    Kelas       : %s'%d_kelas[i])
        print('    Prodi       : %s'%d_jurusan[i])
        print('    Kehadiran   : %.2f'%d_hadir[i])
        print('    Tugas       : %.2f'%d_tugas[i])
        print('    UTS         : %.2f'%d_uts[i])
        print('    UAS         : %.2f'%d_uas[i])
        print('    Nilai Akhir : %.2f'%d_akhir[i])
        print('---------------------------')
    kembali = input('Kembali Tekan [enter]')
    menu_dosen()

def ubah():
    rubah = input('Ubah Biodata/Nilai [B/N] : ')
    if rubah == 'B' or rubah == 'b' :
        i = int (input('Inputkan ID : '))
        if (i > len(d_nim[i])):
            print('ID Salah')
        else:
            jurusanb = input('Prodi [TI/SI] : ')
            if jurusanb == 'TI' or jurusanb == 'ti':
                jbaru = 'Teknik Informatika'
                d_jurusan[i] = jbaru
            elif jurusanb == 'SI' or jurusanb == 'si':
                jbaru = 'Sistem Informasi'
                d_jurusan[i] = jbaru
            else :
                kembali = input('Pilihan tidak ada')
                ubah()

            namabaru = input('Nama : ')
            d_nama[i] = namabaru

            nimbaru = input('Nim : ')
            d_nim[i] = nimbaru

            kelasbaru = input('Kelas : ')
            d_kelas[i] = kelasbaru

            
    else:
        i = int (input('Inputkan ID : '))
        if (i > len(d_nim[i])):
            print('ID Salah')
        else:
            hadirb = float (input('Jumlah Hadir : '))
            j_hadirb = ((hadirb/16)*20/100)*100
            d_hadir[i] = j_hadirb

            tugasb = float (input('Nilai Tugas : '))
            j_tugasb = tugasb*(25/100)
            d_tugas[i] = j_tugasb

            utsb = float (input('Nilai UTS : '))
            j_utsb = utsb*(25/100)
            d_uts[i] = j_utsb

            uasb = float (input ('Nilai UAS : '))
            j_uasb = uasb*(30/100)
            d_uas[i] = j_uasb

            totalb = j_hadirb+j_tugasb+j_utsb+j_uasb
            d_akhir[i] = totalb
    kembali = input ('Kembali Tekan [enter]')
    menu_dosen()  

def hapus():
    system('cls')
    judul()
    print('Hapus Data'.center(40))
    print('=====================================')
    i = int(input('Masukkan ID : '))
    
    if (i > len(d_nim[i])):
        tidak = input('Nim Tidak Ada')
        hapus()
    
    else:
        d_nim.remove(d_nim[i])
        d_nama.remove(d_nama[i])
        d_kelas.remove(d_kelas[i])
        d_jurusan.remove(d_jurusan[i])
        d_hadir.remove(d_hadir[i])
        d_tugas.remove(d_tugas[i])
        d_uts.remove(d_uts[i])
        d_uas.remove(d_uas[i])
        d_akhir.remove(d_akhir[i])
       
