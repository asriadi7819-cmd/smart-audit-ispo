# data_ispo/prinsip_3.py
# Data Master ISPO - Prinsip 3 (Sesuai Lampiran Permentan No. 33 Tahun 2025)

PRINSIP_3_DATA = {
    "prinsip_no": 3,
    "prinsip_nama": (
        "PENGELOLAAN LINGKUNGAN HIDUP, SUMBER DAYA ALAM, DAN KEANEKARAGAMAN"
        " HAYATI"
    ),
    "kriteria": [
        {
            "code": "3.1",
            "nama": "Pelaksanaan Izin Lingkungan atau Persetujuan Lingkungan",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen terkait hasil"
                        " pengelolaan dan pemantauan lingkungan, termasuk"
                        " pelaporannya kepada instansi yang berwenang. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen lingkungan (AMDAL, UKL-UPL,"
                                " dan sejenisnya) yang telah disahkan oleh"
                                " instansi terkait, mencakup seluruh"
                                " aktivitas operasional Perusahaan"
                                " Perkebunan, antara lain: (a) luas area; (b)"
                                " rencana kapasitas olah pabrik; (c) pengelolaan"
                                " limbah."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen lingkungan yang"
                                " telah disahkan dan memiliki laporan"
                                " pelaksanaan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " lingkungan yang telah disahkan dan memiliki"
                                " laporan pelaksanaan."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia laporan pelaksanaan dari dokumen"
                                " lingkungan yang telah dilaporkan ke instansi"
                                " terkait dibuktikan dengan tanda terima."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia laporan pelaksanaan"
                                " dengan tanda terima."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia laporan"
                                " pelaksanaan."
                            ),
                        },
                    ],
                }
            ],
        },
        {
            "code": "3.2",
            "nama": "Pengelolaan Limbah",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki Izin/Persetujuan"
                        " teknis/SLO (Surat Laik Operasional) mengenai"
                        " pengelolaan limbah (padat, cair dan emisi udara)"
                        " yang dikeluarkan oleh instansi berwenang. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen izin Persetujuan"
                                " teknis/SLO (Surat Laik Operasional) yang"
                                " dikeluarkan oleh instansi berwenang untuk"
                                " pemanfaatan/pembuangan ke badan"
                                " air/pembuangan ke laut, mencakup: (a) masa"
                                " berlaku; dan (b) kesesuaian lokasi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen izin"
                                " Persetujuan teknis/SLO (Surat Laik"
                                " Operasional)."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen izin"
                                " Persetujuan teknis/SLO (Surat Laik"
                                " Operasional)."
                            ),
                        }
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme pengelolaan"
                        " limbah (padat, cair dan emisi udara). (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " sesuai dengan peraturan perundangan yang"
                                " berlaku meliputi: (a) pengelolaan limbah"
                                " padat, (b) pengelolaan limbah cair (IPAL),"
                                " dan (c) pengelolaan emisi udara."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen"
                                " SOP/Petunjuk teknis/Instruksi Kerja"
                                " pengelolaan limbah padat, cair (IPAL), dan"
                                " emisi udara; rekaman pelaksanaan; laporan"
                                " pengelolaan limbah; dan dokumen hasil"
                                " pengujian."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " SOP/Petunjuk teknis/Instruksi Kerja"
                                " pengelolaan limbah."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman pelaksanaan"
                                " pengelolaan limbah dan pelaporan"
                                " pengelolaan, pemantauan limbah yang telah"
                                " dilaporkan secara berkala kepada instansi"
                                " yang berwenang sesuai dengan peraturan yang"
                                " berlaku (padat, cair dan emisi udara)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman pelaksanaan"
                                " dan pelaporan pengelolaan limbah."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman"
                                " atau pelaporan."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen hasil pengujian dari"
                                " laboratorium yang terakreditasi dan"
                                " menunjukkan seluruh parameter uji telah"
                                " sesuai dengan baku mutu yang ditetapkan untuk"
                                " pembuangan dan/atau pemanfaatan limbah cair"
                                " pabrik kelapa sawit sesuai peraturan yang"
                                " berlaku."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika hasil uji laboratorium sesuai"
                                " baku mutu limbah cair."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak sesuai baku mutu."
                            ),
                        },
                    ],
                },
            ],
        },
        {
            "code": "3.3",
            "nama": "Gangguan dari Sumber yang Tidak Bergerak",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme untuk"
                        " menangani gangguan sumber tidak bergerak sesuai"
                        " dengan pedoman yang diterbitkan oleh Kementerian yang"
                        " menyelenggarakan urusan pemerintahan di bidang"
                        " lingkungan hidup. (I, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " yang menginformasikan tata cara pengelolaan"
                                " gangguan sumber tidak bergerak (emisi dan"
                                " ambient) sesuai dengan peraturan yang"
                                " berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen"
                                " SOP/Petunjuk teknis/Instruksi Kerja"
                                " gangguan sumber tidak bergerak (emisi dan"
                                " ambient); rekaman pelaksanaan; laporan"
                                " pengelolaan kepada instansi yang"
                                " berwenang; dan dokumen hasil pengujian."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " SOP/Petunjuk gangguan sumber tidak bergerak."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman pengelolaan"
                                " gangguan sumber tidak bergerak (emisi dan"
                                " ambient) yang telah dilaporkan kepada"
                                " instansi yang berwenang."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman pengelolaan"
                                " dan laporan ke instansi berwenang."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman"
                                " laporan."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman hasil pengujian dari"
                                " laboratorium yang terakreditasi dan"
                                " menunjukkan seluruh parameter uji telah"
                                " sesuai dengan baku mutu yang ditetapkan untuk"
                                " gangguan dari sumber yang tidak bergerak"
                                " yang sesuai dengan peraturan yang berlaku."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika hasil uji laboratorium"
                                " terakreditasi sesuai baku mutu."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak sesuai baku mutu."
                            ),
                        },
                    ],
                }
            ],
        },
        {
            "code": "3.4",
            "nama": "Pemanfaatan Limbah",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme pemanfaatan"
                        " limbah (padat, cair dan gas/udara). (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " yang menginformasikan: (a) pemanfaatan"
                                " limbah padat berupa serat, cangkang dan"
                                " janjang kosong untuk pengganti bahan bakar"
                                " fosil; (b) pemanfaatan tandan/janjang kosong"
                                " untuk pupuk organik; (c) pemanfaatan limbah"
                                " cair berupa Land Application (LA) untuk"
                                " pemupukan; (d) pemanfaatan limbah gas untuk"
                                " mengurangi emisi karbon."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen"
                                " SOP/Petunjuk teknis/Instruksi Kerja"
                                " pemanfaatan limbah (padat, cair dan"
                                " gas/udara); rekaman pelaksanaan kepada"
                                " instansi yang berwenang."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " SOP pemanfaatan limbah."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman pelaksanaan"
                                " pemanfaatan limbah padat, cair dan gas/udara"
                                " yang telah dilaporkan kepada instansi yang"
                                " berwenang."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman pelaksanaan"
                                " dan laporan pemanfaatan limbah."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                    ],
                }
            ],
        },
        {
            "code": "3.5",
            "nama": "Pengelolaan Bahan Berbahaya dan Beracun (B3) Serta Limbah B3",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme"
                        " pengelolaan Bahan Berbahaya dan Beracun (B3) serta"
                        " Limbah B3. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " tentang pengelolaan Bahan Berbahaya dan"
                                " Beracun (B3) serta Limbah B3."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen"
                                " SOP/Petunjuk teknis/Instruksi Kerja"
                                " pengelolaan Bahan Berbahaya dan Beracun (B3)"
                                " serta Limbah B3; rekaman pelaksanaan kepada"
                                " instansi yang berwenang."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " SOP pengelolaan B3 dan Limbah B3."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman pelaksanaan"
                                " pengelolaan Bahan Berbahaya dan Beracun (B3)"
                                " serta Limbah B3 yang telah dilaporkan kepada"
                                " instansi yang berwenang."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman pelaksanaan"
                                " pengelolaan B3 dan Limbah B3."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki Legalitas Tempat"
                        " Penyimpanan Sementara Limbah B3 yang dikeluarkan"
                        " oleh Instansi yang berwenang. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Legalitas Tempat Penyimpanan"
                                " Sementara Limbah B3 (Tempat Penyimpanan"
                                " Sementara LB3) berupa izin yang masih"
                                " berlaku/ rincian teknis penyimpanan limbah B3"
                                " yang terintegrasi dengan persetujuan"
                                " lingkungan dan sesuai dengan nama pelaku"
                                " usaha dan/atau kegiatan Perkebunan."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen legalitas TPS"
                                " LB3 yang masih berlaku."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki dokumen.",
                        },
                        {
                            "text": (
                                "Kesesuaian jenis Limbah B3 yang tercantum di"
                                " dalam legalitas Tempat Penyimpanan Sementara"
                                " LB3 dengan Limbah B3 yang dihasilkan dan"
                                " disimpan di Tempat Penyimpanan Sementara"
                                " LB3."
                            ),
                            "doc": False,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Jika jenis Limbah B3 sesuai.",
                            "fail": "Tidak Memenuhi Jika tidak sesuai.",
                        },
                        {
                            "text": (
                                "Tempat Penyimpanan sementara limbah B3, harus"
                                " memenuhi syarat sebagai berikut: Persyaratan"
                                " Lokasi Penyimpanan Limbah B3 Bebas banjir;"
                                " tidak rawan bencana, atau telah direkayasa"
                                " dengan teknologi untuk perlindungan dan"
                                " pengelolaan lingkungan hidup fasilitas"
                                " Penyimpanan Limbah B3, berupa: bangunan;"
                                " tangki dan/atau kontainer; silo; dilengkapi"
                                " dengan peralatan penanggulangan keadaan"
                                " darurat."
                            ),
                            "doc": False,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika TPS LB3 memenuhi syarat"
                                " lokasi dan fasilitas."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memenuhi.",
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen perjanjian"
                        " kerja sama dengan pihak ketiga yang memiliki izin"
                        " dari instansi terkait untuk menangani limbah B3. (I,"
                        " B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen perjanjian kerja sama dengan"
                                " pihak ketiga Pengelola Limbah B3"
                                " (Pengangkut/ Pengumpul/ Pemanfaat/Pengolah"
                                " dan/atau Penimbun) yang masih berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen kerja sama"
                                " pihak ketiga pengelola limbah B3."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Jika Perusahaan Perkebunan bekerja sama dengan"
                                " Pengumpul Limbah B3, maka Penghasil Limbah"
                                " B3 atau pelaku usaha dan/atau kegiatan"
                                " Perkebunan harus memiliki Salinan Kontrak"
                                " Kerja sama antara Pihak pengumpul dengan"
                                " Pengelola Akhir (Pemanfaatan/ Pengolahan"
                                " dan/atau Penimbunan) Limbah B3."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki salinan kontrak kerja"
                                " sama pengumpul dengan pengelola akhir."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Pihak Pengelola Limbah B3 harus memiliki"
                                " legalitas Pengelolaan Limbah B3 yang masih"
                                " berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika legalitas pengelola limbah B3"
                                " masih berlaku."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak berlaku.",
                        },
                        {
                            "text": (
                                "Tersedia Dokumen Neraca (Catatan keluar"
                                " masuk) Limbah B3 yang dihasilkan, dikelola"
                                " lanjut dan yang tersimpan di Tempat"
                                " Penampungan Sementara (TPS) Limbah B3."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia dokumen neraca"
                                " limbah B3."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia laporan manifes Elektronik"
                                " pengiriman Limbah B3 untuk jenis Limbah B3"
                                " yang telah diangkut dari TPS Limbah B3 secara"
                                " berkala setiap 3 (tiga) bulan kepada"
                                " instansi terkait."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia laporan manifes"
                                " elektronik berkala 3 bulan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Kesesuaian penerima Limbah B3 dalam manifes"
                                " dengan dokumen kerja sama."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika penerima dalam manifes sesuai"
                                " dokumen kerja sama."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak sesuai.",
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Penggunaan bahan kimia yang dilarang atau dibatasi"
                        " sesuai dengan peraturan perundangan yang berlaku."
                        " (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Dokumen yang menjelaskan penggunaan Bahan Kimia"
                                " sesuai dengan peraturan perundangan yang"
                                " berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen.",
                            "fail": "Tidak Memenuhi Jika tidak memiliki dokumen.",
                        }
                    ],
                },
            ],
        },
        {
            "code": "3.6",
            "nama": "Pengendalian Kebakaran Lahan dan Bencana Alam",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme"
                        " pencegahan, pemantauan dan penanggulangan kebakaran"
                        " lahan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " tentang pencegahan, pemantauan dan"
                                " penanggulangan kebakaran di areal izin Usaha"
                                " Perkebunan sesuai peraturan Perundangan"
                                " yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja, rekaman sosialisasi,"
                                " dan komitmen tertulis terkait pencegahan"
                                " dan penanggulangan kebakaran."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " terkait."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman pelaksanaan"
                                " pencegahan, pemantauan dan penanggulangan"
                                " kebakaran, yang dilaporkan per 1 (satu)"
                                " tahun sekali ke instansi terkait."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman pelaksanaan"
                                " dan pelaporan 1 tahun sekali."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rekaman sosialisasi penanggulangan"
                                " kebakaran kepada seluruh jajaran pelaku"
                                " usaha Perkebunan, pekerja, publik dan tim"
                                " Pemadam kebakaran kebun."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman sosialisasi"
                                " kebakaran."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia komitmen tertulis dari seluruh"
                                " jajaran pelaku usaha Perkebunan, pekerja,"
                                " publik dan tim pemadam kebakaran kebun yang"
                                " menyatakan bahwa tidak boleh ada kegiatan"
                                " pembakaran di dalam areal izin usaha"
                                " Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia komitmen tertulis"
                                " larangan bakar."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia komitmen."
                            ),
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki Sumber Daya Manusia"
                        " (SDM) yang mampu mencegah dan menanggulangi"
                        " kebakaran lahan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia tim/unit penanggulangan kebakaran"
                                " yang telah mendapatkan pelatihan"
                                " pencegahan dan penanggulangan kebakaran dari"
                                " instansi berwenang."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki tim/unit"
                                " penanggulangan kebakaran dan dokumen"
                                " pelatihan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki tim"
                                " terlatih."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen pelatihan pencegahan dan"
                                " penanggulangan kebakaran secara periodik."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia dokumen pelatihan"
                                " periodik."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia dokumen."
                            ),
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki sarana dan prasarana"
                        " pengendalian kebakaran sesuai peraturan perundangan."
                        " (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk Teknis/Instruksi Kerja"
                                " untuk pemeliharaan sarana dan prasarana"
                                " pengendalian kebakaran sesuai peraturan"
                                " perundangan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen.",
                            "fail": "Tidak Memenuhi Jika tidak memiliki dokumen.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman pemeliharaan sarana"
                                " dan prasarana pengendalian kebakaran."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman pemeliharaan"
                                " sarpras."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia daftar inventarisasi sarana dan"
                                " prasarana pengendalian kebakaran."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia daftar inventarisasi"
                                " sarpras."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia daftar."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen pembaharuan dan pengecekan"
                                " secara berkala untuk sarana dan prasarana"
                                " pengendalian/ penanggulangan kebakaran."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia dokumen pengecekan"
                                " berkala sarpras."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia dokumen."
                            ),
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Perusahaan Perkebunan menyediakan anggaran untuk"
                        " pencegahan dan penanggulangan kebakaran lahan. (I,"
                        " B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia anggaran untuk pencegahan dan"
                                " penanggulangan kebakaran."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki anggaran.",
                            "fail": "Tidak Memenuhi Jika tidak memiliki anggaran.",
                        }
                    ],
                },
            ],
        },
        {
            "code": "3.7",
            "nama": "Kawasan Lindung dan Areal Bernilai Konservasi Tinggi",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki hasil identifikasi"
                        " kawasan lindung dan areal bernilai konservasi"
                        " tinggi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen hasil Identifikasi kawasaan"
                                " lindung dan areal bernilai konservasi tinggi"
                                " di areal konsesi perusahaan sesuai dengan"
                                " peraturan perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Jika memiliki dokumen.",
                            "fail": "Tidak Memenuhi Jika tidak memiliki dokumen.",
                        }
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme"
                        " pemeliharaan kawasan lindung dan areal bernilai"
                        " konservasi tinggi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " tentang pemeliharaan, pengelolaan dan"
                                " pemantauan kawasan lindung dan areal bernilai"
                                " konservasi tinggi serta telah"
                                " disosialisasikan kepada seluruh pekerja dan"
                                " masyarakat sekitar sesuai dengan peraturan"
                                " perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja dan dokumen rekaman"
                                " implementasi dan bukti sosialisasi."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki SOP"
                                " pemeliharaan kawasan lindung."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen Rekaman implementasi"
                                " pemeliharaan, pengelolaan dan pemantauan"
                                " kawasan lindung dan areal bernilai"
                                " konservasi tinggi, serta bukti sosialisasi"
                                " kepada seluruh pekerja dan masyarakat."
                                " Dilakukan minimum setahun sekali dan"
                                " dilaporkan kepada instansi yang berwenang."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman implementasi"
                                " dan laporan tahunan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki peta lokasi dan"
                        " Rencana Pengelolaan NKT dan kawasan lindung lainnya"
                        " yang sudah teridentifikasi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia peta lokasi NKT dan kawasan lindung"
                                " yang sesuai dengan dokumen hasil"
                                " Identifikasi kawasan lindung dan NKT serta"
                                " mendapat persetujuan manajemen Perusahaan"
                                " Perkebunan dengan skala minimal 1:50.000."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki peta, rencana"
                                " pengelolaan dan bukti sosialisasi rencana"
                                " pengelolaan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki peta"
                                " skala 1:50.000."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rencana pengelolaan seluruh NKT dan"
                                " kawasan lindung yang telah disosialisasikan"
                                " kepada pekerja dan masyarakat sekitar."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika rencana pengelolaan"
                                " disosialisasikan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak disosialisasikan."
                            ),
                        },
                    ],
                },
            ],
        },
        {
            "code": "3.8",
            "nama": "Konservasi Keanekaragaman Hayati (Biodiversity)",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki daftar jenis tumbuhan"
                        " dan satwa yang dilindungi di areal konsesi (dari"
                        " dokumen lingkungan). (I, B)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia daftar jenis tumbuhan dan satwa yang"
                                " dilindungi di areal konsesi, sebelum dan"
                                " sesudah kegiatan usaha perkebunan dilakukan."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen daftar jenis"
                                " tumbuhan dan satwa yang dilindungi, rencana"
                                " pemantauan dan pemutakhiran."
                            ),
                            "fail": (
                                "Tidak Memiliki dokumen daftar jenis tumbuhan"
                                " dan satwa yang dilindungi, rencana"
                                " pemantauan dan pemutakhiran."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rencana pemantauan tumbuhan dan"
                                " satwa yang dilindungi di areal konsesi."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rencana pemantauan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Dilakukan pemutakhiran dokumen tentang daftar"
                                " jenis tumbuhan dan satwa yang dilindungi di"
                                " areal konsesi berdasarkan hasil pemantauan"
                                " yang disampaikan kepada institusi yang"
                                " menangani konservasi dan perlindungan"
                                " tumbuhan dan satwa yang dilindungi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika dokumen dimutakhirkan dan"
                                " dilaporkan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak dimutakhirkan."
                            ),
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme pelestarian"
                        " keanekaragaman hayati (Biodiversity). (I, B)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " tentang pelestarian keanekaragaman hayati"
                                " (Biodiversity)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja, dokumen rekaman"
                                " pelestarian, rencana dan bukti rekaman"
                                " sosialisasi."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki SOP"
                                " pelestarian keanekaragaman hayati."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman pelestarian"
                                " keanekaragaman hayati (Biodiversity)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman pelestarian"
                                " keanekaragaman hayati."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rencana dan bukti rekaman Sosialisasi"
                                " kepada masyarakat sekitar mengenai"
                                " keberadaan tumbuhan dan satwa yang"
                                " dilindungi dan SOP/Petunjuk"
                                " teknis/Instruksi Kerja tentang pelestarian"
                                " keanekaragaman hayati (Biodiversity)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rencana dan bukti"
                                " rekaman sosialisasi."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia bukti"
                                " sosialisasi."
                            ),
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki upaya penanganan"
                        " apabila ditemukan insiden dengan tumbuhan dan"
                        " satwa yang dilindungi. (I, B)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia rekaman penanganan apabila"
                                " ditemukan insiden dengan tumbuhan dan"
                                " satwa yang dilindungi, serta telah"
                                " dilaporkan kepada BKSDA setempat."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki rekaman penanganan.",
                            "fail": (
                                "Tidak Memiliki rekaman penanganan insiden."
                            ),
                        }
                    ],
                },
            ],
        },
        {
            "code": "3.9",
            "nama": "Konservasi terhadap Sumber dan Kualitas Air",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme"
                        " identifikasi, pemantauan, pengelolaan dan"
                        " pemeliharaan sumber dan kualitas air serta tersedia"
                        " peta badan air. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " yang mengatur tata cara melakukan"
                                " identifikasi, pemantauan, pengelolaan dan"
                                " pemeliharaan sumber dan kualitas air sesuai"
                                " peraturan perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja, hasil identifikasi,"
                                " peta badan air, program pemantauan,"
                                " pengelolaan dan pemeliharaan, serta dokumen"
                                " rekaman."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki SOP"
                                " pengelolaan air."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia hasil identifikasi sumber air yang"
                                " dilengkapi dengan peta yang"
                                " menginformasikan lokasi badan air."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia hasil identifikasi"
                                " dan peta badan air."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia peta.",
                        },
                        {
                            "text": (
                                "Tersedia program rencana pemantauan,"
                                " pengelolaan dan pemeliharaan kualitas air"
                                " permukaan secara periodik."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia program rencana"
                                " pemantauan kualitas air."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia program."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rekaman/bukti terdokumentasi"
                                " penerapan pengelolaan air, pemeliharaan"
                                " sumber air dan pengukuran kualitas air"
                                " melalui hasil pengujian mutu air di"
                                " laboratorium terakreditasi secara berkala."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia bukti rekaman"
                                " penerapan pengelolaan dan hasil uji lab"
                                " mutu air."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia bukti"
                                " rekaman."
                            ),
                        },
                    ],
                }
            ],
        },
        {
            "code": "3.10",
            "nama": "Konservasi Kawasan dengan Potensi Erosi Tinggi",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme konservasi"
                        " kawasan dengan potensi erosi tinggi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " yang mengatur tata cara melakukan"
                                " identifikasi kawasan dengan potensi erosi"
                                " tinggi dan rencana konservasinya sesuai"
                                " peraturan yang berlaku."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja dan dokumen rekaman"
                                " pelaksanaan kegiatan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki SOP"
                                " potensi erosi tinggi."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen program dan rekaman"
                                " pelaksanaan kegiatan konservasi kawasan"
                                " dengan potensi erosi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia dokumen program dan"
                                " rekaman konservasi erosi."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki peta topografi dan"
                        " lokasi penyebaran sungai. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia peta topografi areal perkebunan"
                                " yang termutakhir."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki peta.",
                            "fail": "Tidak Memenuhi Jika tidak memiliki peta.",
                        },
                        {
                            "text": (
                                "Tersedia Peta lokasi areal dengan potensi"
                                " erosi tinggi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika tersedia peta erosi tinggi.",
                            "fail": "Tidak Memenuhi Jika tidak tersedia peta.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "3.11",
            "nama": (
                "Inventarisasi dan Mitigasi Emisi Gas Rumah Kaca"
            ),
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki laporan Inventarisasi"
                        " GRK. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": "Tersedianya Laporan Inventarisasi GRK.",
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Tersedia laporan inventarisasi GRK"
                                " dan analisis perubahan lahan."
                            ),
                            "fail": (
                                "Tidak memenuhi Tidak memiliki laporan"
                                " inventarisasi GRK dan analisis perubahan"
                                " lahan."
                            ),
                        }
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen riwayat lahan."
                        " (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen analisis perubahan lahan"
                                " mulai dari tahun sebagaimana tercantum dalam"
                                " kalkulator GRK ISPO yang termutakhir."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia dokumen analisis"
                                " perubahan lahan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia dokumen."
                            ),
                        }
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme dan Laporan"
                        " Mitigasi Emisi Gas Rumah Kaca (GRK). (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " dan Laporan mitigasi emisi gas rumah kaca"
                                " (GRK)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Memiliki SOP/Petunjuk"
                                " teknis/Instruksi Kerja dan Laporan"
                                " mitigasi serta data pendukung"
                                " terdokumentasi."
                            ),
                            "fail": (
                                "Tidak memenuhi Tidak memiliki SOP dan"
                                " Laporan mitigasi."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia data pendukung terdokumentasi untuk"
                                " perhitungan GRK."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia data pendukung"
                                " perhitungan GRK."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia data.",
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki hasil perhitungan GRK."
                        " (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen hasil perhitungan GRK yang"
                                " benar sesuai dengan sumber data dan acuan"
                                " yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Memiliki dokumen hasil perhitungan"
                                " GRK serta program dan rekaman program"
                                " pengurangan GRK."
                            ),
                            "fail": (
                                "Tidak memenuhi Tidak Memiliki dokumen hasil"
                                " perhitungan GRK."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia program pengurangan GRK yang"
                                " termutakhir."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": "Memenuhi Jika tersedia program pengurangan GRK.",
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman kegiatan program"
                                " pengurangan GRK."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman kegiatan"
                                " pengurangan GRK."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "3.12",
            "nama": "Perlindungan terhadap Hutan Alam dan Gambut",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen yang"
                        " menunjukkan pembangunan kebun baru tidak membuka"
                        " hutan alam dan lahan gambut, sesuai peraturan"
                        " perundangan yang berlaku. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia peta padu serasi areal operasional"
                                " kebun dengan hutan alam."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Memiliki dokumen.",
                            "fail": "Tidak Memenuhi Tidak memiliki dokumen.",
                        },
                        {
                            "text": (
                                "Peta padu serasi areal perkebunan/ pabrik"
                                " dengan Peta Indikatif Penundaan Pemberian"
                                " Izin Baru (PIPPIB) revisi terbaru."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Jika peta padu serasi PIPPIB tersedia.",
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman bahwa Perusahaan Perkebunan"
                                " tidak membuka areal hutan dan gambut."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman bebas buka"
                                " hutan dan gambut."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme"
                        " perlindungan hutan dan lahan gambut. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen kebijakan Perusahaan"
                                " Perkebunan terkait perlindungan kawasan hutan"
                                " dan kawasan gambut yang terdapat dalam"
                                " ketentuan PIPPIB terbaru, dan ditandatangani"
                                " oleh pimpinan puncak."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen.",
                            "fail": "Tidak Memenuhi Jika tidak memiliki dokumen.",
                        },
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " terdokumentasi tentang tata cara pengelolaan"
                                " dan perlindungan kawasan gambut."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia SOP perlindungan"
                                " kawasan gambut."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia SOP.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman penerapan SOP/Petunjuk"
                                " teknis/Instruksi Kerja tentang tata cara"
                                " pengelolaan dan perlindungan kawasan"
                                " gambut."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman penerapan"
                                " SOP perlindungan gambut."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman."
                            ),
                        },
                    ],
                },
            ],
        },
    ],
}