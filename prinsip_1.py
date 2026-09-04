# data_ispo/prinsip_1.py
# Data Master ISPO - Prinsip 1 (Sesuai teks referensi mutlak)

PRINSIP_1_DATA = {
    "prinsip_no": 1,
    "prinsip_nama": "KEPATUHAN TERHADAP PERATURAN PERUNDANG-UNDANGAN",
    "kriteria": [
        {
            "code": "1.1",
            "nama": "Izin Lokasi atau Kesesuaian Kegiatan Pemanfaatan Ruang",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan memiliki dokumen Izin Lokasi atau KKPR yang dikeluarkan oleh Gubernur/Bupati/Wali kota/OSS/PTSP/Pejabat yang berwenang dengan dilengkapi peta skala minimal 1:50.000. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia dokumen Izin Lokasi (awal dan/atau perpanjangan) dan/atau dokumen KKPR. Dokumen KKPR dimaksud berlaku bagi perolehan kebun sejak tahun 2021.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen yang sah",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen yang sah",
                        },
                        {
                            "text": "Tersedia dokumen izin lokasi untuk perolehan kebun tahun 1993-2020 dengan dilengkapi peta skala minimal 1:50.000.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen yang sah",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen yang sah",
                        },
                        {
                            "text": "Tersedia peta izin lokasi dan/atau dokumen KKPR dengan skala minimal 1:50.000.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen yang sah",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen yang sah",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": "Pemegang dokumen Izin Lokasi atau KKPR wajib membebaskan tanah dari hak dan kepentingan pihak lain sesuai peraturan perundang-undangan. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia dokumen pembebasan lahan pada masa Izin Lokasi atau KKPR yang masih berlaku.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen yang masih berlaku",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen yang masih berlaku",
                        }
                    ],
                },
            ],
        },
        {
            "code": "1.2",
            "nama": "Perolehan Lahan",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan yang lahan perkebunannya berasal dari kawasan hutan produksi tetap/kawasan hutan produksi terbatas/kawasan hutan yang dapat dikonversi wajib mempunyai dokumen Keputusan Penetapan Batas Areal Pelepasan Kawasan Hutan. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia dokumen Keputusan Penetapan Batas Areal yang diterbitkan oleh instansi berwenang.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen Keputusan Penetapan Batas Areal",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen Keputusan Penetapan Batas Areal",
                        }
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": "Lahan usaha perkebunan yang berasal dari tanah hak ulayat masyarakat hukum adat wajib diperoleh berdasarkan musyawarah dan mufakat tanpa paksaan serta persetujuan dari masyarakat hukum adat pemegang hak ulayat dengan informasi yang lengkap mengenai penyerahan tanah dan ganti rugi sesuai dengan ketentuan yang berlaku. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia kesepakatan melalui Padiatapa/ Persetujuan Atas dasar Informasi Awal Tanpa Paksaan/Free, Prior, and Informed Consent (FPIC) yang prosesnya diawasi oleh pemerintah desa/kecamatan/kabupaten/kota.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen Padiatapa/FPIC",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen Padiatapa/FPIC",
                        },
                        {
                            "text": "Tersedia dokumen yang menunjukkan bahwa lahan perkebunan tidak berasal dari tanah hak ulayat dan diakui oleh ketentuan yang berlaku.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen yang menunjukan bahwa lahan tidak berasal dari tanah hak ulayat",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen yang menunjukan bahwa lahan tidak berasal dari tanah hak ulayat",
                        },
                    ],
                },
            ],
        },
        {
            "code": "1.3",
            "nama": "Hak Atas Tanah",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan memiliki bukti kepemilikan Hak atas Tanah (HGU dan/atau Hak Pakai) yang sah dengan luasan sesuai dengan peraturan perundangan di bidang pertanahan. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia Sertifikat Hak atas tanah (HGU, HP) yang sesuai: a) nama pemegang Hak Atas Tanah sesuai dengan nama Perusahaan Perkebunan; b) jenis penggunaan dan/atau pemanfaatan tanah sesuai keputusan pemberian haknya; c) kesesuaian lokasi dan luasan operasional berada di dalam areal HGU; d) kesesuaian masa berlaku HGU pada saat sertifikasi ISPO.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen Hak atas tanah yang sah",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen Hak atas tanah yang sah",
                        },
                        {
                            "text": "SK Pemberian HGU wajib didaftarkan pada kantor pertanahan Kabupaten/Kota/Provinsi setempat yang dibuktikan dengan tanda terima.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika SK HGU didaftarkan dengan tanda terima",
                            "fail": "Tidak memenuhi Jika belum didaftarkan",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": "Perusahaan Perkebunan wajib memelihara batas-batas HGU. (I, B)",
                    "params": [
                        {
                            "text": "Tersedia Peta Bidang Tanah (Kadasteral) yang ditetapkan oleh pejabat yang berwenang sesuai dengan Hak Atas Tanah (HGU dan/atau HP).",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki peta bidang tanah",
                            "fail": "Tidak memenuhi Jika tidak memiliki peta bidang tanah",
                        },
                        {
                            "text": "Tersedia dokumen/rekaman jumlah dan keberadaan pilar batas/patok Hak Atas Tanah (HGU dan/atau HP) yang sesuai dengan Peta Bidang Tanah (Kadasteral).",
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika memiliki rekaman pilar batas",
                            "fail": "Tidak memenuhi Jika tidak memiliki rekaman pilar batas",
                        },
                        {
                            "text": "Tersedia SOP/Petunjuk Teknis/Instruksi Kerja untuk pemeliharaan pilar batas/patok Hak Atas Tanah (HGU dan/atau HP).",
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika memiliki SOP pemeliharaan",
                            "fail": "Tidak memenuhi Jika tidak memiliki SOP",
                        },
                        {
                            "text": "Tersedia dokumen rekaman/monitoring pemeliharaan pilar batas/patok Hak Atas Tanah (HGU dan/atau HP).",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen monitoring pemeliharaan batas",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen monitoring",
                        },
                    ],
                },
            ],
        },
        {
            "code": "1.4",
            "nama": "Sengketa Lahan dan Sengketa Lainnya terkait dengan Usaha Perkebunan",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan wajib menyelesaikan sengketa lahan dan sengketa lainnya terkait dengan usaha perkebunan yang ada di dalam arealnya sesuai peraturan yang berlaku dan telah disepakati penyelesaiannya. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia hasil identifikasi areal sengketa dan peta lahan yang menjadi sengketa pada seluruh area operasionalnya yang berada di dalam HGU.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki hasil identifikasi areal sengketa dan peta",
                            "fail": "Tidak memenuhi Jika tidak memiliki hasil identifikasi sengketa",
                        },
                        {
                            "text": "Tersedia dokumen proses penyelesaian sengketa lahan dan sengketa lainnya terkait dengan usaha perkebunan melalui musyawarah, apabila tidak dapat diselesaikan maka ditempuh melalui jalur hukum, dibuktikan dengan tanda terima pengaduan.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen proses penyelesaian sengketa",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen penyelesaian sengketa",
                        },
                        {
                            "text": "Tersedia laporan penyelesaian sengketa lahan dan sengketa lainnya terkait dengan usaha perkebunan yang telah dilaporkan ke instansi terkait dibuktikan dengan tanda terima.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen tanda terima pelaporan kepada instansi terkait",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen tanda terima pelaporan",
                        },
                    ],
                }
            ],
        },
        {
            "code": "1.5",
            "nama": "Tanah Terlantar",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan wajib memastikan pemanfaatan lahan HGU dan/atau Hak Pakai sesuai peruntukannya. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia dokumen pelaporan penggunaan dan pemanfaatan tanah sesuai dengan keputusan pemberian hak atas tanah yang disampaikan kepada instansi terkait.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen pelaporan penggunaan dan pemanfaatan tanah ke instansi terkait",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen pelaporan",
                        },
                        {
                            "text": "Tersedia hasil identifikasi pemanfaatan tanah yang belum sesuai peruntukannya.",
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Jika memiliki dokumen identifikasi pemanfaatan tanah yang belum sesuai",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen identifikasi",
                        },
                    ],
                }
            ],
        },
        {
            "code": "1.6",
            "nama": "Tumpang Tindih Lahan dengan Usaha Lainnya",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan memiliki kesepakatan tertulis atas tumpang tindih lahan dengan usaha lainnya sesuai peraturan perundang-undangan. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia hasil identifikasi lahan yang tumpang tindih dengan izin lain dan melaporkannya kepada pemberi izin.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki identifikasi areal yang tumpang tindih",
                            "fail": "Tidak memenuhi Jika tidak memiliki identifikasi",
                        },
                        {
                            "text": "Tersedia dokumen kesepakatan yang memuat: lokasi, luasan, periode, khususnya bagi izin usaha lainnya yang dikeluarkan setelah izin lokasi perkebunan.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen penyelesaian tumpang tindih lahan",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen penyelesaian",
                        },
                    ],
                }
            ],
        },
        {
            "code": "1.7",
            "nama": "Bentuk Badan Hukum",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan memiliki akta pendirian badan usaha yang disahkan oleh Kementerian yang membidangi Hukum. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia dokumen Akta pendirian yang disahkan oleh Kementerian yang membidangi Hukum dan sesuai dengan: a) nama Perusahaan Perkebunan, b) bidang usaha dan c) tipe kepemilikan Perusahaan Perkebunan (PMA atau PMDN).",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen akta pendirian berbadan Hukum",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen akta",
                        },
                        {
                            "text": "Jika terjadi perubahan, maka harus tersedia Akta perubahan terakhir yang disahkan oleh Kementerian yang membidangi hukum.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika tersedia akta perubahan",
                            "fail": "Tidak memenuhi Jika tidak tersedia",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": "Perusahaan Perkebunan memiliki Nomor Induk Berusaha (NIB) dan Nomor Pokok Wajib Pajak (NPWP). (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia Nomor Induk Berusaha (NIB) dan Nomor Pokok Wajib Pajak (NPWP) yang sesuai nama perusahaan yang mengajukan sertifikasi ISPO.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen NPWP, NIB",
                            "fail": "Tidak memenuhi Jika tidak memiliki NIB/NPWP",
                        }
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": "Semua bangunan dengan kategori permanen, wajib memiliki Izin Mendirikan Bangunan (IMB) dan/atau Persetujuan Bangunan Gedung (PBG) yang sesuai dengan peraturan yang berlaku. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia Izin Mendirikan Bangunan (IMB) dan/atau Persetujuan Bangunan Gedung (PBG) untuk bangunan (rumah permanen, pabrik, kantor, gudang, bengkel, dll) yang diperoleh dari instansi yang berwenang.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki IMB dan/atau Persetujuan Bangunan Gedung (PBG)",
                            "fail": "Tidak memenuhi Jika tidak memiliki",
                        }
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": "Bangunan PKS dan Fasilitasnya, yang berada di luar HGU mempunyai Sertifikat Hak Guna Bangunan yang dikeluarkan oleh instansi terkait yang berwenang. (I, P)",
                    "params": [
                        {
                            "text": "Tersedia SK atau Sertifikat Hak Guna Bangunan (HGB) yang sesuai dengan: a) nama perusahaan yang mengajukan sertifikasi ISPO, b) jenis penggunaan dan/atau pemanfaatan, c) lokasi bangunan, d) luas bangunan, dan e) masa berlaku.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki SK atau HGB",
                            "fail": "Tidak memenuhi Jika tidak Memiliki SK atau HGB",
                        }
                    ],
                },
                {
                    "no": 5,
                    "deskripsi": "Perusahaan Perkebunan wajib membayar Pajak Bumi dan Bangunan (PBB) setiap tahun, PPH dan PPN sesuai dengan ketentuan yang berlaku, dan melaporkan SPT pajak sesuai peraturan yang berlaku. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia bukti pembayaran/setoran Pajak Bumi dan Bangunan (PBB) 1 (satu) tahun terakhir.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki PBB",
                            "fail": "Tidak memenuhi Jika tidak memiliki PBB",
                        },
                        {
                            "text": "Tersedia bukti pembayaran/setoran Pajak Penghasilan (PPh) 3 (tiga) bulan terakhir dan Pajak Pertambahan Nilai (PPN) 1 (satu) tahun terakhir.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki PPh dan PPN",
                            "fail": "Tidak memenuhi Jika tidak memiliki PPh/PPN",
                        },
                        {
                            "text": "Tersedia bukti lapor Surat Pemberitahuan Tahunan (SPT) kepada instansi terkait.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki bukti lapor SPT",
                            "fail": "Tidak memenuhi Jika tidak memiliki bukti lapor SPT",
                        },
                    ],
                },
            ],
        },
        {
            "code": "1.8",
            "nama": "Izin Lingkungan atau Persetujuan Lingkungan",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan memiliki Izin Lingkungan atau Persetujuan Lingkungan yang dikeluarkan oleh pejabat yang berwenang sesuai peraturan perundangan. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia Izin atau Persetujuan Lingkungan yang sesuai dengan: a) nama perusahaan yang mengajukan sertifikasi ISPO, b) ruang lingkup usaha, dan c) lokasi usaha.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki Izin atau Persetujuan Lingkungan sesuai ketentuan yang berlaku",
                            "fail": "Tidak Memenuhi Jika tidak memiliki Izin atau Persetujuan Lingkungan",
                        }
                    ],
                }
            ],
        },
        {
            "code": "1.9",
            "nama": "Fasilitasi Pembangunan Kebun Masyarakat",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan memiliki dokumen kerja sama dengan masyarakat sekitar kebun tentang fasilitasi pembangunan kebun masyarakat. Fasilitasi dapat dilakukan melalui: a) pola kredit, b) pola bagi hasil, c) bentuk pendanaan lain yang disepakati para pihak, d) bentuk kemitraan lainnya. (I, B)",
                    "params": [
                        {
                            "text": "Tersedia dokumen kesepakatan bersama atau perjanjian kerja sama antara Perusahaan Perkebunan dengan masyarakat sekitar sesuai ketentuan perundangan yang berlaku dan diketahui oleh dinas yang membidangi perkebunan.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen kerja sama Perusahaan Perkebunan dengan masyarakat sekitar",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen kerja sama",
                        },
                        {
                            "text": "Tersedia dokumen perencanaan pemenuhan kewajiban fasilitasi masyarakat sesuai dengan kesepakatan atau perjanjian kerja sama.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen perencanaan",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen perencanaan",
                        },
                        {
                            "text": "Tersedia dokumen realisasi kerja sama pembangunan kebun masyarakat minimal 20% dari luas Izin Usaha Perkebunan (IUP/IUP-B) yang dimiliki sesuai dengan ketentuan perudangan yang berlaku dan dilaporkan ke instansi berwenang.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika realisasi kemitraan min. 20% tersedia",
                            "fail": "Tidak memenuhi Jika realisasi belum terpenuhi",
                        },
                    ],
                }
            ],
        },
        {
            "code": "1.10",
            "nama": "Izin Usaha Perkebunan atau Perizinan Berusaha",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": "Perusahaan Perkebunan memiliki Izin Usaha Perkebunan/ Perizinan Berusaha sesuai peraturan yang berlaku. (I, B, P)",
                    "params": [
                        {
                            "text": "Tersedia dokumen Izin Usaha Perkebunan/ Perizinan Berusaha yang diterbitkan oleh Bupati/Wali kota/ Gubernur/BKPM atas nama Menteri Pertanian, sesuai dengan kewenangan.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen Izin Usaha Perkebunan/ Perizinan Berusaha dan memenuhi persyaratan",
                            "fail": "Tidak memenuhi Jika tidak memiliki dokumen Izin Usaha Perkebunan/ Perizinan Berusaha atau tidak memenuhi persyaratan",
                        },
                        {
                            "text": "Izin Usaha Perkebunan/Perizinan diterbitkan oleh instansi pemerintah yang berwenang sesuai dengan peraturan perundangan.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika diterbitkan instansi sah",
                            "fail": "Tidak memenuhi",
                        },
                        {
                            "text": "Luas Usaha Perkebunan/Perizinan harus lebih besar atau sama dengan luas HGU/HGB.",
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika luas izin >= luas HGU/HGB",
                            "fail": "Tidak memenuhi",
                        },
                        {
                            "text": "Areal usaha perkebunan yang disertifikasi ISPO harus dapat dipastikan berada di dalam areal Izin Perkebunan.",
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika areal berada di dalam izin",
                            "fail": "Tidak memenuhi",
                        },
                        {
                            "text": "Jumlah unit dan kapasitas terpasang atau volume produksi produk dari Pabrik Kelapa Sawit (PKS) sesuai dengan kapasitas yang tertera didalam Izin Usaha Perkebunan/Perizinan.",
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika kapasitas PKS sesuai izin",
                            "fail": "Tidak memenuhi",
                        },
                        {
                            "text": "Komoditi yang tertera dalam dokumen Izin Usaha Perkebunan/Perizinan sesuai dengan komoditi yang diusahakan.",
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika komoditi sesuai",
                            "fail": "Tidak memenuhi",
                        },
                        {
                            "text": "Untuk IUP-P, ditunjukkan dengan ketersediaan bahan baku TBS yang diolah di PKS paling rendah 20% dari kebun sendiri ditunjukkan dengan adanya perjanjian kerja sama pasokan bahan baku TBS antara PKS dengan perkebun minimal 10 (sepuluh) tahun.",
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika pasokan TBS >= 20%",
                            "fail": "Tidak memenuhi",
                        },
                        {
                            "text": "Pemenuhan bahan baku minimal 20% dari kebun yang diusahakan sendiri, dibuktikan dengan: (a) Dokumen Perjanjian kerja sama secara tertulis dengan pekebun minimal 15 (lima belas) tahun, jika pemenuhan bahan baku berasal dari hak atas tanah pekebun; atau (b) Dokumen HGU atas nama perusahaan yang mengajukan sertifikasi ISPO, jika pemenuhan bahan baku berasal dari HGU milik perusahaan; atau (c) Dokumen Perjanjian Hak Pakai, jika pemenuhan bahan baku berasal dari lahan yang disewa dari Hak Pakai.",
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika dokumen pembuktian bahan baku 20% lengkap",
                            "fail": "Tidak memenuhi",
                        },
                    ],
                }
            ],
        },
    ],
}