# data_ispo/prinsip_6.py
# Data Master ISPO - Prinsip 6 (Sesuai Lampiran Permentan No. 33 Tahun 2025)

PRINSIP_6_DATA = {
    "prinsip_no": 6,
    "prinsip_nama": "PENERAPAN TRANSPARANSI",
    "kriteria": [
        {
            "code": "6.1",
            "nama": "Ketertelusuran Sumber Pemasok TBS",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki daftar sumber pemasok"
                        " TBS. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia daftar sumber pemasok TBS yang"
                                " termutakhir yang memuat informasi paling"
                                " sedikit berupa: nama pemasok; alamat dan"
                                " lokasi kebun; status sertifikasi ISPO; data"
                                " produksi dan produktivitas pemasok; data"
                                " pembelian dari pemasok."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen informasi"
                                " pemasok TBS yang termutakhir."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " informasi pemasok TBS."
                            ),
                        }
                    ],
                }
            ],
        },
        {
            "code": "6.2",
            "nama": (
                "Perhitungan Indeks K dan Data Dukung yang Transparan"
            ),
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memilki mekanisme perhitungan"
                        " indeks K sesuai peraturan perundangan yang berlaku."
                        " (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " terkait perhitungan indeks K Perusahaan"
                                " Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja terkait"
                                " perhitungan indeks K dan rekaman komponen"
                                " indeks."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki SOP/IK"
                                " perhitungan indeks K."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia Rekaman komponen Indeks dalam"
                                " jangka waktu 3 (tiga) bulan terakhir."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman komponen"
                                " indeks 3 bulan terakhir."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                }
            ],
        },
        {
            "code": "6.3",
            "nama": (
                "Penerapan Penetapan Harga TBS yang Adil dan Transparan"
            ),
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan secara periodik memberikan"
                        " informasi terkini harga TBS terhadap pemasok TBS. (I,"
                        " B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " penetapan harga apabila harga yang"
                                " digunakan untuk pekebun non mitra."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja penetapan harga,"
                                " rekaman surat penetapan harga TBS,"
                                " perhitungan harga TBS, dan bukti pembayaran."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki SOP.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman surat penetapan harga TBS"
                                " bulanan (untuk periode 1 (satu) tahun ke"
                                " belakang), dari Dinas yang membidangi"
                                " Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia surat penetapan"
                                " harga bulanan 1 tahun ke belakang."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman perhitungan harga TBS"
                                " sesuai SOP/Petunjuk teknis/Instruksi Kerja"
                                " yang ditetapkan untuk pekebun non mitra."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman perhitungan harga"
                                " non-mitra."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia bukti pembayaran TBS dari pihak"
                                " luar sesuai dengan perjanjian yang disepakati."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada bukti pembayaran TBS"
                                " sesuai perjanjian."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                }
            ],
        },
        {
            "code": "6.4",
            "nama": (
                "Keterbukaan terhadap Informasi yang Tidak Bersifat Rahasia dan"
                " Penanganan Keluhan"
            ),
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memilki mekanisme untuk"
                        " menyediakan informasi publik, selain informasi yang"
                        " dikecualikan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " penyediaan Informasi publik yang akurat,"
                                " benar dan tidak menyesatkan sesuai peraturan"
                                " perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja penyediaan Informasi"
                                " publik, media elektronik/non elektronik, dan"
                                " rekaman informasi publik."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki SOP.",
                        },
                        {
                            "text": (
                                "Tersedia sarana/media elektronik dan/atau"
                                " non eletronik dalam rangka penyediaan"
                                " informasi publik yang dapat diakses dengan"
                                " mudah dan efisien."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia media informasi"
                                " publik yang mudah diakses."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman informasi publik"
                                " yang publikasikan dan waktu publikasinya"
                                " dalam jangka waktu 2 (dua) tahun terakhir."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman publikasi"
                                " informasi 2 tahun terakhir."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memilki mekanisme"
                        " tanggapan/pelayanan terhadap permintaan informasi"
                        " dari pemangku kepentingan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " tanggapan/pelayanan terhadap permintaan"
                                " informasi dari pemangku kepentingan sesuai"
                                " peraturan perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja dan rekaman"
                                " tanggapan/pelayanan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki SOP.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman"
                                " tanggapan/pelayanan terhadap permintaan"
                                " informasi meliputi: Jumlah permintaan"
                                " informasi yang diterima; waktu yang"
                                " diperlukan dalam memenuhi setiap permintaan"
                                " informasi jumlah pemberian dan penolakan"
                                " permintaan informasi; dan/atau alasan"
                                " penolakan permintaan informasi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman layanan"
                                " permintaan informasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme penanganan"
                        " keluhan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " penanganan keluhan dari pihak internal dan"
                                " eksternal, termasuk keluhan terkait produk"
                                " dalam sistem rantai pasok."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja penanganan keluhan,"
                                " dan rekaman penyelesaian penanganan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki SOP.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman penyelesaian"
                                " penanganan keluhan dalam jangka waktu 2"
                                " (dua) tahun terakhir."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman penyelesaian"
                                " keluhan 2 tahun terakhir."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen Beneficial"
                        " Ownership (BO). (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen informasi berupa pemilik"
                                " manfaat dari perusahaan perkebunan yang"
                                " disampaikan melalui Sistem Informasi"
                                " Perkebunan (SIPERIBUN)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen informasi BO"
                                " di SIPERIBUN."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        }
                    ],
                },
            ],
        },
        {
            "code": "6.5",
            "nama": (
                "Komitmen Untuk Tidak Melakukan Tindakan yang Dapat"
                " Diindikasikan Suap"
            ),
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dan mendeklarasikan"
                        " Kode Etik Usaha yang jujur dan bebas korupsi yang"
                        " telah disosialisasikan kepada publik. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " terkait kode etik pelaksanaan bisnis,"
                                " pencegahan dan pemberatasan tindak"
                                " pencucian uang, pemberantasan tindak pidana"
                                " korupsi dan pencegahan dan pemberatasan"
                                " korupsi yang disahkan oleh manajemen"
                                " Perusahaan Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja terkait kode etik"
                                " dan bukti deklarasi dan/atau sosialisasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki SOP.",
                        },
                        {
                            "text": (
                                "Tersedia bukti deklarasi dan/ atau"
                                " sosialisasi mekanisme terkait kode etik"
                                " kepada seluruh tingkatan pekerja dan pihak"
                                " ketiga."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada bukti deklarasi/sosialisasi"
                                " kode etik."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                }
            ],
        },
        {
            "code": "6.6",
            "nama": (
                "Penerapan Sistem Rantai Pasok yang Mampu Telusur (traceability)"
            ),
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan menetapkan dan menerapkan model"
                        " dan sistem rantai pasok. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia kajian/analisis penetapan model dan"
                                " sistem rantai pasok berdasarkan data sumber"
                                " pemasok TBS."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen penetapan"
                                " model dan prosedur, dokumen komitmen, dan"
                                " dokumen penanganan ketidaksesuaian terkait"
                                " sistem rantai pasok."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia komitmen tentang penetapan model"
                                " dan sistem rantai pasok yang diterapkan"
                                " oleh Perusahaan Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada komitmen rantai pasok."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " untuk menjamin konsistensi penerapan model"
                                " dan sistem rantai pasok yang telah"
                                " ditetapkan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada SOP konsistensi rantai"
                                " pasok."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman implementasi"
                                " penerapan model dan sistem rantai pasok."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman implementasi"
                                " rantai pasok."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen penanganan"
                                " ketidaksesuaian terhadap klaim model rantai"
                                " pasok dan penyimpangan lain pada produk"
                                " bersertifikat ISPO dan/atau dokumen"
                                " terkait."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada dokumen penanganan"
                                " ketidaksesuaian klaim."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki informasi yang lengkap"
                        " pada dokumen transaksi pembelian dan penjualan"
                        " (perjanjian, nota/tiket timbang, surat pengantar"
                        " muat, catatan pengiriman barang termasuk surat"
                        " pengiriman barang). (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen transaksi pembelian dan"
                                " penjualan yang sekurang- kurangnya mencakup"
                                " informasi berikut: nama dan alamat penjual;"
                                " nama dan alamat pembeli; tujuan"
                                " pengiriman; identifikasi produk di antaranya"
                                " CPO, cangkang, dan produk samping olahan"
                                " TBS lainnya, termasuk kesesuaian model"
                                " rantai pasok yang diterapkan; jumlah produk"
                                " yang dikirim; jumlah produk yang diterima"
                                " atau dikirim; tanggal muat dan pengiriman;"
                                " dokumentasi pengiriman/ transportasi; nomor"
                                " sertifikat ISPO; masa berlaku sertifikat"
                                " ISPO; logo ISPO; nomor pengenal unik."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen transaksi"
                                " pembelian dan penjualan lengkap."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak lengkap.",
                        }
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Penerapan sistem rantai pasok segregasi/"
                        " segregation. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia fasilitas yang mendukung"
                                " pemisahan secara fisik produk bersertifikat"
                                " dan produk tidak bersertifikat ISPO pada"
                                " setiap tahapan produksi, pemrosesan,"
                                " penyimpanan dan transportasi pengiriman"
                                " di seluruh rantai pasok."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki fasilitas pemisahan"
                                " produk."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki fasilitas"
                                " pemisahan."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rekaman pembilasan fasilitas pada"
                                " saat perubahan model rantai pasok dan"
                                " rekaman pemisahan produk tidak"
                                " bersertifikat ISPO."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada rekaman pembilasan dan"
                                " pemisahan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " tindak lanjut penangananan produk yang"
                                " terkontaminasi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada SOP penanganan produk"
                                " terkontaminasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen yang membuktikan pemisahan"
                                " secara fisik pada fasilitas penyimpanan,"
                                " proses dan transportasi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada bukti dokumen pemisahan"
                                " fisik."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Penerapan sistem rantai pasok mass balance. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia data termutakhir terkait data"
                                " pemasok TBS bersertifikat ISPO yang"
                                " diverifikasi memenuhi 30% telah"
                                " bersertifikasi ISPO."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia data pemasok TBS"
                                " bersertifikat ISPO (min 30%); data penjualan;"
                                " dan laporan rekonsiliasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia data penjualan produk hasil olahan"
                                " TBS, mencakup Informasi: data produksi;"
                                " data stok penyimpanan /gudang; data"
                                " pengiriman; d) daftar Pembeli."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia data penjualan"
                                " lengkap."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak lengkap.",
                        },
                        {
                            "text": (
                                "Apabila menggunakan sistem pencatatan"
                                " transaksi harian (continous accounting"
                                " system), tersedia laporan rekonsiliasi"
                                " periodik dengan ketentuan: monitoring"
                                " secara harian (realtime); jumlah produk"
                                " bersertifikat ISPO yang dikirim kepada"
                                " pelanggan dari Pabrik tidak melebihi jumlah"
                                " yang diproduksi dalam basis pencatatan"
                                " harian; c) Produk yang diproduksi selama"
                                " masa pembekuan, tidak dapat berstatus sebagai"
                                " Produk Bersertifikat ISPO."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika rekonsiliasi harian mass"
                                " balance sesuai ketentuan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak sesuai.",
                        },
                        {
                            "text": (
                                "Apabila menggunakan sistem pencatatan"
                                " transaksi berkala (fix inventory period),"
                                " tersedia laporan rekonsiliasi maksimal"
                                " periodik 3 (tiga) bulanan dengan ketentuan:"
                                " Jumlah volume/berat dari produk"
                                " bersertifikat ISPO masuk dan keluar"
                                " seimbang; Pada akhir periode rekonsiliasi"
                                " tidak terdapat stok negatif untuk produk"
                                " bersertifikat ISPO; c) Jika terjadi"
                                " pendataan berlebih pada akhir periode"
                                " rekonsiliasi. Kredit yang tidak digunakan"
                                " dapat dialihkan dan dicatat untuk periode"
                                " rekonsiliasi berikutnya selama sertifikat"
                                " ISPO berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika rekonsiliasi 3 bulanan mass"
                                " balance sesuai ketentuan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak sesuai.",
                        },
                    ],
                },
                {
                    "no": 5,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme pengendalian"
                        " kegiatan yang dialihdayakan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " pengendalian kegiatan yang dialihdayakan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia SOP pengendalian"
                                " kegiatan alih daya."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia SOP.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen kesepakatan / kontrak yang"
                                " melingkupi kegiatan yang dialihdayakan"
                                " dengan semua kontraktor yang melakukan"
                                " penanganan fisik produk bersertifikat ISPO,"
                                " status kepemilikan material."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia bukti"
                                " kesepakatan/kontrak kontraktor."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen sosialisasi sistem rantai"
                                " pasok ISPO kepada kontraktor."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika tersedia bukti sosialisasi.",
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
                {
                    "no": 6,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme"
                        " pengendalian rekaman sistem rantai pasok yang"
                        " diimplementasikan dan tetap tersedia sampai"
                        " setidaknya dalam kurun waktu 5 (lima) tahun. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " Pengendalian catatan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia SOP Pengendalian"
                                " catatan rantai pasok."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia SOP.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman rantai pasok yang disimpan"
                                " paling sedikit 5 (lima) tahun."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman rantai pasok"
                                " tersimpan min 5 tahun."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
                {
                    "no": 7,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki personel yang"
                        " kompeten dalam penerapan dan pemeliharaan sistem"
                        " rantai pasok. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia kriteria persyaratan kompetensi"
                                " yang terlibat dalam sistem rantai pasok ISPO."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia kriteria persyaratan"
                                " kompetensi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia rencana kebutuhan pelatihan"
                                " personil."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rencana kebutuhan"
                                " pelatihan personil."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia realisasi pelatihan personil dan"
                                " hasil evaluasi pelatihan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia realisasi pelatihan"
                                " personil dan hasil evaluasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
                {
                    "no": 8,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki infrastruktur yang"
                        " memadai dalam penerapan dan pemeliharaan sistem"
                        " rantai pasok. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Layout kapasitas penyimpanan produk"
                                " bersertifikat ISPO yang sesuai dengan"
                                " kapasitas produksi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia dokumen layout"
                                " penyimpanan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia infrastruktur timbangan yang telah"
                                " dikalibrasi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia infrastruktur dan data"
                                " tera/kalibrasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia sistem manajemen informasi yang"
                                " mendukung sistem rantai pasok dan"
                                " terimplementasi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia sistem manajemen"
                                " informasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
                {
                    "no": 9,
                    "deskripsi": (
                        "Perusahaan Perkebunan melakukan registrasi jumlah"
                        " produksi dan penjualan dari produk bersertifikat"
                        " ISPO. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia rekaman transaksi produk"
                                " bersertifikat ISPO. Saat tersedia sistem IT"
                                " ISPO maka registrasi dan pelaporan transaksi"
                                " harus dilakukan pada sistem IT tersebut"
                                " sebelum dilakukan pengiriman."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki rekaman transaksi"
                                " produk bersertifikat ISPO."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        }
                    ],
                },
            ],
        },
    ],
}