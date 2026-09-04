# data_ispo/prinsip_4.py
# Data Master ISPO - Prinsip 4 (Sesuai Lampiran Permentan No. 33 Tahun 2025)

PRINSIP_4_DATA = {
    "prinsip_no": 4,
    "prinsip_nama": "TANGGUNG JAWAB KETENAGAKERJAAN",
    "kriteria": [
        {
            "code": "4.1",
            "nama": "Keselamatan dan Kesehatan Kerja",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen sistem manajemen"
                        " K3 sesuai dengan peraturan perundangan yang berlaku."
                        " (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " sistem manajemen K3 meliputi kebijakan tentang"
                                " K3, perencanaan, pelaksanaan, pemantauan"
                                " dan evaluasi serta tinjauan ulang K3 terkini"
                                " dan ditandatangani oleh pimpinan puncak."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia SOP/Petunjuk"
                                " teknis/Instruksi Kerja, bukti sosialisasi dan"
                                " rekaman implementasi."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia"
                                " SOP/Petunjuk teknis/Instruksi Kerja,"
                                " bukti sosialisasi dan rekaman implementasi."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia bukti sosialisasi kepada seluruh"
                                " pekerja serta manajemen dan pekerja"
                                " kontraktor tentang kebijakan K3 serta."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia bukti sosialisasi"
                                " kebijakan K3."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia bukti"
                                " sosialisasi."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman implementasi"
                                " sistem manajemen K3."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman"
                                " implementasi SMK3."
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
                        "Perusahaan Perkebunan memiliki organisasi dan sistem"
                        " tanggap darurat sesuai dengan peraturan perundangan"
                        " yang berlaku. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia struktur organisasi dan SDM yang"
                                " memiliki pemahaman terhadap sistem"
                                " kesiapsiagaan dan tanggap darurat yang"
                                " disahkan manajemen."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen struktur"
                                " organisasi, SDM, dan pemahaman tanggap"
                                " darurat."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " sistem tanggap darurat meliputi penanganan"
                                " keadaan darurat, bencana alam, dan"
                                " kecelakaan kerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP sistem tanggap"
                                " darurat."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki SOP.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman implementasi"
                                " sistem tanggap darurat."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman"
                                " implementasi tanggap darurat."
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
                        "Perusahaan Perkebunan memiliki sarana dan prasarana"
                        " tanggap darurat yang diperiksa berkala dan di"
                        " tempatkan di tempat yang mudah diakses bilamana"
                        " dibutuhkan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia sarana dan prasarana tanggap"
                                " darurat (bencana alam, kebakaran dan"
                                " peledakan) di wilayah konsesi usaha"
                                " Perkebunan yang sesuai dengan peraturan"
                                " perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki sarana dan prasarana"
                                " tanggap darurat yang memadai."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki sarana dan"
                                " prasarana tanggap darurat."
                            ),
                        },
                        {
                            "text": "Tersedia sarana evakuasi.",
                            "doc": False,
                            "interview": False,
                            "obs": True,
                            "pass": "Memenuhi Jika tersedia sarana evakuasi.",
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Jumlah sarana dan prasarana tanggap darurat"
                                " memadai sesuai dengan peraturan yang"
                                " berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Jika jumlah sarpras memadai.",
                            "fail": "Tidak Memenuhi Jika tidak memadai.",
                        },
                        {
                            "text": (
                                "Penempatan sarana dan prasarana tanggap"
                                " darurat yang mudah diakses."
                            ),
                            "doc": False,
                            "interview": False,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika penempatan sarpras mudah"
                                " diakses."
                            ),
                            "fail": "Tidak Memenuhi Jika sulit diakses.",
                        },
                        {
                            "text": (
                                "Tersedia program dan realisasi pemeliharaan"
                                " dan/atau penggantian sarana dan prasarana"
                                " tanggap darurat sesuai dengan peraturan yang"
                                " berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia program dan realisasi"
                                " pemeliharaan/penggantian sarpras."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Perusahaan Perkebunan telah membentuk organisasi"
                        " Panitia Pembina Keselamatan dan Kesehatan Kerja"
                        " (P2K3) dengan jumlah personal yang memadai sesuai"
                        " dengan peraturan perundangan yang berlaku. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SK pengesahan tim P2K3 oleh"
                                " instansi terkait yang sesuai dengan"
                                " personil P2K3."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen SK"
                                " pengesahan tim P2K3 yang termutakhir."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki SK P2K3."
                            ),
                        },
                        {
                            "text": (
                                "Memiliki sekretaris P2K3 yang bersertifikat"
                                " Ahli Keselamatan dan Kesehatan Kerja (AK3)"
                                " mutakhir sesuai dengan persyaratan yang"
                                " berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika sekretaris P2K3 bersertifikat"
                                " AK3 mutakhir."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak bersertifikat"
                                " AK3."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rekaman hasil rapat P2K3 untuk"
                                " memantau implementasi dari K3 beserta bukti"
                                " penyesuaian K3 yang perlu diterapkan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia rekaman hasil rapat"
                                " P2K3."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak tersedia rekaman"
                                " rapat."
                            ),
                        },
                    ],
                },
                {
                    "no": 5,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki hasil identifikasi"
                        " resiko dan rencana pengelolaan resiko yang"
                        " disosialisasikan kepada manajemen dan pekerja. (I, B,"
                        " P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia hasil identifikasi resiko dan"
                                " rencana pengelolaan pada setiap kegiatan"
                                " operasional di lingkungan Perusahaan"
                                " Perkebunan oleh petugas yang berkompeten."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen identifikasi"
                                " dan rencana pengelolaan risiko."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia bukti sosialisasi tentang hasil"
                                " identifikasi resiko dan rencana"
                                " pengelolaan resiko untuk semua tingkatan"
                                " pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki bukti sosialisasi"
                                " risiko."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Semua pekerja memiliki pemahaman yang cukup"
                                " terhadap resiko K3 dibagiannya."
                            ),
                            "doc": False,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika pekerja memahami risiko K3 di"
                                " bagiannya."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memahami.",
                        },
                        {
                            "text": (
                                "Tersedia bukti rekaman pelaksanaan"
                                " pengelolaan resiko."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tersedia bukti rekaman"
                                " pelaksanaan pengelolaan risiko."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak ada rekaman."
                            ),
                        },
                    ],
                },
                {
                    "no": 6,
                    "deskripsi": (
                        "Perusahaan Perkebunan menempatkan petunjuk K3 di"
                        " lokasi yang strategis, berdasarkan potensi resiko"
                        " yang sudah diidentifikasi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia tanda-tanda bahaya di lokasi yang"
                                " teridentifikasi resikonya sesuai dengan"
                                " jenis resikonya."
                            ),
                            "doc": False,
                            "interview": False,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki tanda-tanda bahaya"
                                " di lokasi dan jelas terpelihara."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki"
                                " tanda-tanda bahaya."
                            ),
                        },
                        {
                            "text": (
                                "Pemberian tanda sudah memenuhi peraturan"
                                " yang berlaku tentang pemasangan tanda"
                                " bahaya."
                            ),
                            "doc": False,
                            "interview": False,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika pemasangan tanda bahaya"
                                " sesuai peraturan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak sesuai.",
                        },
                    ],
                },
                {
                    "no": 7,
                    "deskripsi": (
                        "Perusahaan Perkebunan melakukan pemeriksaan"
                        " kesehatan secara berkala untuk seluruh pekerja dan"
                        " pemeriksaan kesehatan khusus untuk pekerja dengan"
                        " resiko tertentu. Hasil pemeriksaan dievaluasi dan"
                        " ditindaklanjuti secara memadai jika ditemukan pekerja"
                        " yang terkena penyakit akibat kerja. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia daftar pekerja yang harus"
                                " dilakukan pemeriksaan kesehatan berkala dan"
                                " pemeriksaan kesehatan khusus untuk pekerja"
                                " dengan resiko tertentu dan termutakhir."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen daftar"
                                " pekerja pemeriksaan kesehatan berkala dan"
                                " khusus."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki daftar.",
                        },
                        {
                            "text": (
                                "Tersedia bukti pelaksanaan pemeriksaan"
                                " kesehatan berkala dan pemeriksaan kesehatan"
                                " khusus untuk pekerja dengan resiko tertentu"
                                " sesuai dengan daftar yang ada."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia bukti pelaksanaan"
                                " pemeriksaan kesehatan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia bukti.",
                        },
                        {
                            "text": (
                                "Tersedia bukti pemeriksaan berkala"
                                " dilakukan oleh petugas khusus sesuai dengan"
                                " peraturan perundangan yang berlaku dan"
                                " tindak lanjut dari hasil pemeriksaan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika pemeriksaan dilakukan petugas"
                                " khusus dan ditindaklanjuti."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak sesuai.",
                        },
                        {
                            "text": (
                                "Tersedia bukti tindak lanjut dari hasil"
                                " pelaksanaan kesehatan berkala dan"
                                " pemeriksaan kesehatan khusus untuk pekerja"
                                " dengan resiko tertentu."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada bukti tindak lanjut hasil"
                                " pemeriksaan kesehatan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 8,
                    "deskripsi": (
                        "Perusahaan Perkebunan memastikan seluruh pekerja"
                        " mendapatkan pelatihan K3 yang memadai. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia program pelatihan K3 secara"
                                " berkala untuk semua tingkatan pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen rencana"
                                " pelatihan K3 secara berkala dan mutakhir."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki rencana"
                                " pelatihan."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia bukti pelatihan K3 untuk semua"
                                " pekerja sesuai dengan program pelatihan"
                                " yang ada."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada bukti pelatihan K3.",
                            "fail": "Tidak Memenuhi Jika tidak ada bukti.",
                        },
                    ],
                },
                {
                    "no": 9,
                    "deskripsi": (
                        "Perusahaan Perkebunan menyediakan Alat Pelindung Diri"
                        " (APD) yang memadai sesuai dengan peruntukannya kepada"
                        " setiap pekerja. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia APD yang memadai untuk setiap"
                                " pekerja sesuai dengan hasil identifikasi"
                                " resiko."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Para pekerja menggunakan APD"
                                " sesuai dengan resiko pekerjaannya."
                            ),
                            "fail": (
                                "Tidak Memenuhi Pekerja tidak menggunakan APD"
                                " sesuai resiko."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia program penggantian APD sesuai"
                                " dengan masa pakai dari produsen APD."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada program penggantian APD"
                                " sesuai masa pakai."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak ada program"
                                " penggantian."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumentasi sebagai bukti"
                                " pemberian APD kepada pekerja sesuai dengan"
                                " resiko pekerjaannya."
                            ),
                            "doc": True,
                            "interview": False,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada dokumentasi penyerahan"
                                " APD."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak ada dokumentasi."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia dokumen inventarisasi APD untuk"
                                " melihat stok APD yang tersedia dalam rangka"
                                " mengantisipasi APD yang rusak."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada inventarisasi stok APD."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada inventaris.",
                        },
                    ],
                },
                {
                    "no": 10,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki laporan penerapan K3"
                        " yang dilaporkan setiap 3 (tiga) bulan ke Dinas"
                        " Tenaga Kerja setempat. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia laporan penerapan program K3 sesuai"
                                " dengan peraturan perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Dokumen Laporan penerapan program K3"
                                " tersedia dengan lengkap sesuai dengan"
                                " rencana."
                            ),
                            "fail": (
                                "Tidak memenuhi Dokumen laporan penerapan"
                                " program K3 tidak lengkap."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia bukti penyerahan laporan penerapan"
                                " K3 setiap 3 (tiga) bulan kepada Dinas"
                                " Tenaga Kerja setempat dan bukti laporan"
                                " sudah diterima."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada bukti serah terima"
                                " laporan K3 triwulanan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada bukti.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "4.2",
            "nama": "Persyaratan Administrasi Terkait Hubungan Kerja",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme rekrutmen"
                        " pekerja dan proses rekrutmen sesuai dengan peraturan"
                        " perundangan yang berlaku. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " rekrutmen pekerja yang didalamnya sudah"
                                " mencantumkan tata cara perekrutan tenaga"
                                " kerja dan persyaratan pekerja yang diterima"
                                " untuk semua tipe pekerjaan, pelarangan"
                                " penggunaan pekerja anak, dan pelarangan"
                                " diskriminasi dalam pekerjaan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP rekrutmen pekerja"
                                " sesuai perundangan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki SOP"
                                " rekrutmen."
                            ),
                        },
                        {
                            "text": (
                                "Perusahaan Perkebunan dan agen tenaga kerja"
                                " (jika menggunakan agen perekrutan) tidak"
                                " melakukan pemungutan biaya kepada tenaga"
                                " kerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tidak ada pungutan biaya"
                                " rekrutmen."
                            ),
                            "fail": "Tidak Memenuhi Jika ada pungutan biaya.",
                        },
                        {
                            "text": (
                                "Perusahaan Perkebunan dan agen tenaga kerja"
                                " (jika menggunakan agen perekrutan) tidak"
                                " melakukan penahanan dokumen asli milik"
                                " tenaga kerja kecuali dengan alasan yang"
                                " dibenarkan oleh peraturan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tidak menahan dokumen asli"
                                " pekerja."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika menahan dokumen tanpa"
                                " alasan sah."
                            ),
                        },
                        {
                            "text": (
                                "Pengumuman perekrutan tenaga kerja dan"
                                " persyaratannya untuk semua tingkatan pekerja"
                                " diinformasikan secara terbuka."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika pengumuman rekrutmen terbuka."
                            ),
                            "fail": "Tidak Memenuhi Jika tertutup.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan perkebunan memiliki data seluruh pekerja"
                        " baik PKWTT (Pekerja Waktu Tidak Tertentu) maupun"
                        " PKWT (Pekerja Waktu Tertentu)."
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia daftar pekerja yang berisi informasi"
                                " tentang: profil pribadi pekerja (nama,"
                                " tempat dan tanggal lahir, alamat resmi"
                                " sesuai KTP, agama, tanggal mulai masuk"
                                " kerja). status tipe hubungan kerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki daftar pekerja.",
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki daftar"
                                " pekerja."
                            ),
                        }
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki kebijakan tertulis"
                        " yang menyatakan bahwa Perusahaan Perkebunan melarang"
                        " adanya segala bentuk kerjapaksa atau perbudakan dalam"
                        " melakukan kegiatan operasional. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen kebijakan tertulis tentang"
                                " pelarangan segala bentuk kerja paksa atau"
                                " perbudakan dalam melakukan kegiatan"
                                " operasional yang ditandatangani oleh pimpinan"
                                " puncak Perusahaan Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen tertulis,"
                                " bukti sosialisasi dan penerapan kebijakan"
                                " pelarangan kerja paksa/perbudakan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " kebijakan."
                            ),
                        },
                        {
                            "text": (
                                "Perusahaan Perkebunan melakukan sosialisasi"
                                " dan komunikasi terkait kebijakan Tentang"
                                " pelarangan segala bentuk kerja paksa atau"
                                " perbudakan kepada seluruh tingkatan pekerja"
                                " Perusahaan Perkebunan, pekerja kontraktor dan"
                                " masyarakat sekitar."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada bukti sosialisasi kerja"
                                " paksa."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada sosialisasi.",
                        },
                        {
                            "text": (
                                "Tidak ada bentuk kerja paksa atau perbudakan"
                                " dalam melakukan kegiatan operasional usaha"
                                " perkebunan."
                            ),
                            "doc": False,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tidak ditemukan indikasi kerja"
                                " paksa."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika ditemukan bentuk kerja"
                                " paksa."
                            ),
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Pekerja mempunyai hak untuk waktu istirahat dan cuti"
                        " sesuai dengan peraturan perundangan yang berlaku. (I,"
                        " B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia aturan secara tertulis yang mengatur"
                                " hak cuti dan jam kerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki aturan tertulis cuti"
                                " dan jam kerja."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen yang menunjukkan realisasi"
                                " atas aturan yang mengatur hak cuti dan jam"
                                " kerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada realisasi cuti.",
                            "fail": "Tidak Memenuhi Jika tidak ada realisasi.",
                        },
                        {
                            "text": (
                                "Terdapat rekaman sosialisasi peraturan"
                                " terkait jam kerja dan hak cuti pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman sosialisasi cuti"
                                " dan jam kerja."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada rekaman.",
                        },
                        {
                            "text": (
                                "Terdapat rekaman penerapan peraturan"
                                " Perusahaan Perkebunan terkait jam kerja dan"
                                " hak cuti pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada rekaman penerapan jam"
                                " kerja dan cuti."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 5,
                    "deskripsi": (
                        "Setiap pekerja memiliki salinan dokumen hubungan"
                        " kerja sesuai dengan peraturan ketenagakerjaan yang"
                        " berlaku dan tercatat di Dinas yang membidangi"
                        " Ketenagakerjaan setempat. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen hubungan kerja yang berisi"
                                " informasi sekurang- kurangnya: nama dan"
                                " alamat perusahaan; nama, jenis kelamin,"
                                " umur dan alamat pekerja; jabatan atau jenis"
                                " pekerjaan; lingkup pekerjaan; besaran upah,"
                                " tunjangan dan cara pembayaran; peraturan"
                                " Perusahaan Perkebunan dan sanksi yang"
                                " berlaku; hak dan kewajiban pekerja dan"
                                " perusahaan; jangka waktu berlakunya"
                                " perjanjian kerja; tanggal perjanjian kerja"
                                " dibuat; tanda tangan kedua belah pihak"
                                " (pekerja dan perusahaan)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen hubungan kerja"
                                " lengkap."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " hubungan kerja."
                            ),
                        },
                        {
                            "text": (
                                "Seluruh pekerja memiliki salinan dokumen"
                                " hubungan kerja yang sudah ditandatangani"
                                " kedua belah pihak."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika seluruh pekerja memegang"
                                " salinan kontrak."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika pekerja tidak memegang"
                                " salinan."
                            ),
                        },
                    ],
                },
                {
                    "no": 6,
                    "deskripsi": (
                        "Perusahaan Perkebunan yang menggunakan tenaga kerja"
                        " asing harus menunjukkan RPTKA (Rencana Penggunaan"
                        " Tenaga Kerja Asing), IMTA (Izin Menggunakan Tenaga"
                        " Kerja Asing), serta mematuhi peraturan terkait"
                        " mengenai penggunaan tenaga kerja asing. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen RPTKA (Rencana Penggunaan"
                                " Tenaga Kerja Asing (jika ada tenaga kerja"
                                " asing)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen RPTKA (jika"
                                " ada TKA)."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki RPTKA."
                            ),
                        },
                        {
                            "text": "Tersedia dokumen IMTA.",
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Jika memiliki IMTA (jika ada TKA).",
                            "fail": "Tidak Memenuhi Jika tidak memiliki IMTA.",
                        },
                    ],
                },
                {
                    "no": 7,
                    "deskripsi": (
                        "Seluruh pekerjaan yang bersifat tetap tidak boleh"
                        " dilakukan oleh Pekerja Waktu Tertentu (PKWT) atau"
                        " Pekerja Harian Lepas (PKHL). Pekerja Harian Lepas"
                        " yang telah bekerja lebih dari 6 (enam) bulan secara"
                        " terus menerus harus diangkat menjadi Pekerja Waktu"
                        " Tidak Tertentu (PKWTT). (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Daftar hadir lengkap pekerja 6 (enam) bulan"
                                " terakhir sesuai dengan tipe hubungan kerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki daftar pekerja.",
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Bukti pengangkatan pekerja harian mencakup"
                                " PKWT dan PKHL berdasarkan peraturan"
                                " perundangan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada bukti pengangkatan sesuai"
                                " aturan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada bukti.",
                        },
                    ],
                },
                {
                    "no": 8,
                    "deskripsi": (
                        "Melaporkan informasi data ketenagakerjaan dan"
                        " perkembangannya kepada Disnaker setempat setiap 1"
                        " (satu) tahun sekali. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Terdapat bukti bahwa Perusahaan Perkebunan"
                                " membuat laporan ketenagakerjaan dan"
                                " perkembangannya secara periodik sesuai"
                                " peraturan perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen Laporan"
                                " ketenagakerjaan secara rutin."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki laporan"
                                " ketenagakerjaan."
                            ),
                        },
                        {
                            "text": (
                                "Bukti penyerahan dan tanda terima laporan"
                                " sesuai dengan ketentuan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada tanda terima laporan.",
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "4.3",
            "nama": "Peningkatan Kesejahteraan dan Kemampuan Pekerja",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki sistem pengupahan"
                        " sesuai peraturan tentang upah minimum dan mempunyai"
                        " struktur dan skala upah. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Kebijakan Perusahaan Perkebunan tentang sistem"
                                " pengupahan sesuai dengan peraturan"
                                " perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki kebijakan pengupahan"
                                " sesuai perundangan."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " tentang pengupahan meliputi upah pokok,"
                                " tunjangan tetap, tunjangan tidak tetap,"
                                " upah lembur, potongan upah yang sah, dan"
                                " fasilitas/imbalan lain di Perusahaan"
                                " Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP pengupahan"
                                " lengkap."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Sosialisasi Kebijakan Perusahaan Perkebunan"
                                " tentang pengupahan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada bukti sosialisasi upah.",
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Implementasi atas upah minimum sesuai dengan"
                                " peraturan perundangan yang berlaku"
                                " dibuktikan dengan salinan slip gaji/upah"
                                " yang diberikan oleh Perusahaan Perkebunan"
                                " kepada pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika upah minimum diimplementasikan"
                                " lewat slip gaji."
                            ),
                            "fail": "Tidak Memenuhi Jika di bawah minimum.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman penerapan tentang sistem"
                                " pengupahan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman penerapan"
                                " pengupahan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada rekaman.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki sarana dan prasarana"
                        " untuk kesejahteraan pekerja. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia sarana dan prasarana (fisik dan non"
                                " fisik) yang dimiliki oleh Perusahaan"
                                " Perkebunan untuk kesejahteraan dan"
                                " kenyamanan pekerja dan keluarga pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki daftar sarana dan"
                                " prasarana kesejahteraan."
                            ),
                            "fail": (
                                "Tidak memenuhi Jika tidak memiliki sarpras."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia Program dan anggaran perawatan"
                                " serta perbaikan sarana dan prasarana untuk"
                                " kesejahteraan pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada program dan anggaran"
                                " perawatan sarpras."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada anggaran.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman tindak lanjut dari keluhan"
                                " pekerja/keluarga pekerja terhadap kerusakan"
                                " sarana dan prasarana."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada rekaman tindak lanjut"
                                " keluhan sarpras."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki kebijakan untuk"
                        " mengikutsertakan pekerja dalam program Sistem"
                        " Jaminan Sosial Nasional (SJSN) Sesuai peraturan"
                        " perundangan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Dokumen Kebijakan tentang program"
                                " Sistem Jaminan Sosial Nasional (SJSN) sesuai"
                                " dengan hukum ketenagakerjaan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika memiliki Dokumen dan bukti"
                                " sosialisasi kebijakan SJSN."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman Sosialisasi program Sistem"
                                " Jaminan Sosial Nasional (SJSN) yang"
                                " ditetapkan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada rekaman sosialisasi SJSN.",
                            "fail": "Tidak Memenuhi Jika tidak ada rekaman.",
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki daftar karyawan yang"
                        " mengikuti program Badan Penyelenggara Jaminan Sosial"
                        " (BPJS) Ketenagakerjaan dan Kesehatan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia daftar termutakhir karyawan yang"
                                " terdaftar dalam program Badan Penyelenggara"
                                " Jaminan Sosial (BPJS) Ketenagakerjaan dan"
                                " Kesehatan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen daftar"
                                " peserta BPJS."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki daftar.",
                        },
                        {
                            "text": (
                                "Tersedia Bukti pembayaran program BPJS"
                                " ketenagakerjaan dan kesehatan untuk pekerja"
                                " tetap (PKWTT) dan pekerja harian lepas"
                                " (PKHL)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada bukti iuran BPJS PKWTT dan"
                                " PKHL."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada bukti iuran.",
                        },
                        {
                            "text": (
                                "Tersedia Bukti koordinasi pelaksanaan BPJS"
                                " Ketenagakerjaan dan Kesehatan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada bukti koordinasi BPJS.",
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 5,
                    "deskripsi": (
                        "Kerja lembur harus atas kesediaan pekerja dan tidak"
                        " melebihi batas waktu yang telah ditentukan sesuai"
                        " dengan peraturan perundangan yang berlaku. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " pengaturan kerja lembur sesuai dengan"
                                " peraturan perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki SOP pengaturan lembur."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman sosialisasi dan"
                                " komunikasi kepada seluruh pekerja dan"
                                " pekerja kontrak tentang pengaturan kerja"
                                " lembur."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman sosialisasi"
                                " lembur."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada rekaman.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen rekaman kerja lembur untuk"
                                " semua tingkatan pekerja yang konsisten."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika rekaman lembur konsisten.",
                            "fail": "Tidak Memenuhi Jika tidak konsisten.",
                        },
                    ],
                },
                {
                    "no": 6,
                    "deskripsi": (
                        "Target kerja yang ditetapkan harus sesuai dengan"
                        " kemampuan pekerja dan sarana pendukung. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen target kerja sesuai dengan"
                                " bidang pekerjaannya."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika memiliki dokumen target kerja.",
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia dokumen sistem jenjang karir dan"
                                " penilaian prestasi kerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada dokumen jenjang karir dan"
                                " penilaian prestasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Para pekerja memahami dan menerima target"
                                " kerja yang ditetapkan termasuk sistem jenjang"
                                " karir dan penilaian prestasi kerja."
                            ),
                            "doc": False,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika pekerja memahami target.",
                            "fail": "Tidak Memenuhi Jika tidak.",
                        },
                        {
                            "text": (
                                "Tersedia sarana dan prasarana untuk"
                                " meningkatkan kinerja dalam rangka mencapai"
                                " target yang ditetapkan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika sarpras penunjang target"
                                " tersedia."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "4.4",
            "nama": "Larangan Pekerja Anak dan Diskriminasi dalam Pekerjaan",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen kebijakan"
                        " pelarangan mempekerjakan anak sesuai dengan"
                        " peraturan perundangan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Dokumen kebijakan terkait"
                                " pelarangan mempekerjakan anak sesuai"
                                " dengan peraturan perundangan yang berlaku."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki Dokumen kebijakan"
                                " pelarangan anak bekerja."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman sosialisasi dokumen"
                                " kebijakan Perusahaan Perkebunan terkait"
                                " pelarangan mempekerjakan anak sesuai dengan"
                                " peraturan perundangan yang berlaku pada"
                                " seluruh tingkatan pekerja dan pekerja"
                                " kontrak."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada rekaman sosialisasi.",
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman daftar karyawan berisi"
                                " informasi tentang nama, pendidikan,"
                                " jabatan, tempat dan tanggal lahir dan lain"
                                " sebagainya."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada daftar karyawan lengkap"
                                " usia pekerja."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada daftar.",
                        },
                        {
                            "text": (
                                "Tersedia tanda larangan anak-anak berada di"
                                " sekitar lokasi kerja yang berbahaya bagi"
                                " anak-anak dan diketahui oleh seluruh pekerja"
                                " dan keluarga pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": "Memenuhi Jika ada tanda larangan anak.",
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan menerapkan Kebijakan tentang"
                        " peluang dan perlakuan yang sama untuk mendapatkan"
                        " kesempatan kerja. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Dokumen Kebijakan terkait tidak"
                                " melakukan Diskriminasi terhadap pekerja"
                                " berdasarkan ras, warna kulit, jenis kelamin,"
                                " agama, umur, dan status sosial, sesuai"
                                " dengan peraturan perundangan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki Dokumen"
                                " non-diskriminasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman Sosialisasi dokumen"
                                " kebijakan terkait tidak melakukan"
                                " diskriminasi terhadap pekerja berdasarkan"
                                " ras, warna kulit, jenis kelamin, agama,"
                                " umur, status sosial."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman sosialisasi"
                                " non-diskriminasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tidak ada bentuk Diskriminasi terhadap"
                                " pekerja."
                            ),
                            "doc": False,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika tidak ditemukan diskriminasi."
                            ),
                            "fail": "Tidak Memenuhi Jika ada diskriminasi.",
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen pengaduan"
                        " dan keluhan pekerja. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia prosedur penerimaan dan penanganan"
                                " atas pengaduan dan keluhan dari pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika tersedia prosedur pengaduan"
                                " pekerja."
                            ),
                            "fail": "Tidak memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman penerimaan dan penanganan"
                                " atas pengaduan dan keluhan dari pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada rekaman penanganan keluhan"
                                " pekerja."
                            ),
                            "fail": "Tidak memenuhi Jika tidak ada rekaman.",
                        },
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Perusahaan Perkebunan harus memastikan pekerja"
                        " terbebas dari segala bentuk pelecehan, ancaman,"
                        " penganiayaan baik secara fisik maupun mental dari"
                        " sesama pekerja ataupun Perusahaan Perkebunan. (I,"
                        " B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen mekanisme pengaduan dan"
                                " keluhan pekerja terkait pelecehan, ancaman,"
                                " penganiayaan baik secara fisik maupun mental"
                                " dan disosialisasikan kepada para pekerja di"
                                " semua tingkatan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen mekanisme"
                                " pengaduan pelecehan."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman penanganan terkait"
                                " pelecehan, ancaman, penganiayaan baik secara"
                                " fisik maupun mental."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada rekaman penanganan"
                                " pelecehan/ancaman."
                            ),
                            "fail": "Tidak memenuhi Jika tidak ada.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "4.5",
            "nama": "Fasilitasi Pembentukan Serikat Pekerja",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen pembentukan"
                        " Serikat Pekerja dan pertemuan baik antara"
                        " Perusahaan Perkebunan dengan Serikat Pekerja. (I, B,"
                        " P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen pembentukan Serikat Pekerja"
                                " yang telah tercatat di Dinas yang"
                                " membidangi ketenagakerjaan setempat."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen pembentukan"
                                " Serikat Pekerja tercatat Disnaker."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman pertemuan antara Perusahaan"
                                " Perkebunan dengan Serikat Pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman pertemuan"
                                " perusahaan dan serikat."
                            ),
                            "fail": "Tidak memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman pertemuan intern Serikat"
                                " Pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman rapat intern"
                                " serikat."
                            ),
                            "fail": "Tidak memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dan menerapkan"
                        " kebijakan terkait dengan Serikat Pekerja. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Kebijakan Perusahaan Perkebunan"
                                " tentang membebaskan pekerjanya dalam"
                                " pembentukan Serikat Pekerja dan memberikan"
                                " fasilitas terhadap pekerja dalam kegiatan"
                                " serikat pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki kebijakan kebebasan"
                                " berserikat dan fasilitas."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia bukti sosialisasi kebijakan untuk"
                                " seluruh tingkatan pekerja dan kontraktor."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika ada bukti sosialisasi.",
                            "fail": "Tidak memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki daftar pekerja yang"
                        " menjadi anggota Serikat Pekerja. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Daftar pekerja yang menjadi anggota"
                                " Serikat Pekerja tersedia dan mutakhir."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki daftar anggota"
                                " serikat pekerja."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        }
                    ],
                },
                {
                    "no": 4,
                    "deskripsi": (
                        "Perusahaan Perkebunan memastikan pekerja berhak"
                        " menyampaikan pendapat serta keluhannya melalui"
                        " mekanisme yang jelas termasuk Serikat Pekerja. (I,"
                        " B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia mekanisme yang terdokumentasi untuk"
                                " menyampaikan pendapat dan keluhan melalui"
                                " Serikat Pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen mekanisme"
                                " keluhan via serikat."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Pekerja mengetahui mekanisme untuk"
                                " menyampaikan pendapat dan keluhan melalui"
                                " Serikat Pekerja."
                            ),
                            "doc": False,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika pekerja mengetahui mekanisme"
                                " tersebut."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak mengetahui.",
                        },
                        {
                            "text": (
                                "Tersedia dokumentasi umpan balik dari"
                                " perusahaan terhadap pendapat dan keluhan"
                                " dari serikat pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada dokumen umpan balik"
                                " perusahaan."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 5,
                    "deskripsi": (
                        "Perusahaan Perkebunan memastikan pekerja mempunyai"
                        " hak untuk membentuk atau bergabung dalam organisasi"
                        " atau serikat buruh. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Kebijakan yang memperbolehkan"
                                " pekerja untuk berkumpul, membentuk atau"
                                " bergabung dalam organisasi atau serikat"
                                " buruh."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki kebijakan hak"
                                " berserikat."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman sosialisasi terkait"
                                " kebijakan yang memperbolehkan pekerja"
                                " untuk berkumpul, membentuk atau bergabung"
                                " dalam organisasi atau serikat buruh."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman sosialisasi hak"
                                " berserikat."
                            ),
                            "fail": "Tidak memenuhi Jika tidak ada rekaman.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "4.6",
            "nama": "Fasilitasi Pembentukan Koperasi Pekerja dan Karyawan",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki kebijakan dalam"
                        " mendukung pembentukan koperasi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia Dokumen kebijakan dalam mendukung"
                                " pembentukan koperasi dan memberikan"
                                " fasilitas pembentukan koperasi."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen dan bukti"
                                " sosialisasi kebijakan dukungan koperasi."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman Sosialisasi kebijakan dan"
                                " kebijakan diketahui oleh seluruh pekerja."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman sosialisasi"
                                " koperasi."
                            ),
                            "fail": "Tidak memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen"
                        " pembentukan koperasi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Koperasi pekerja dan karyawan melakukan"
                                " Rapat Anggota Tahunan (RAT)."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": "Memenuhi Jika koperasi melaksanakan RAT.",
                            "fail": (
                                "Tidak Memenuhi Jika tidak melaksanakan RAT."
                            ),
                        },
                        {
                            "text": (
                                "Koperasi yang telah terbentuk harus memiliki"
                                " akta pendirian, anggaran dasar dan"
                                " anggaran rumah tangga."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika koperasi punya akta, AD, dan"
                                " ART."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak lengkap.",
                        },
                        {
                            "text": (
                                "Perusahaan Perkebunan melakukan pembinaan"
                                " dan dukungan terhadap koperasi pekerja dan"
                                " karyawan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika perusahaan membina koperasi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak membina.",
                        },
                        {
                            "text": (
                                "Koperasi pekerja dan karyawan mempunyai"
                                " aktivitas yang nyata."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika koperasi beraktivitas nyata."
                            ),
                            "fail": "Tidak Memenuhi Jika vakum.",
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki daftar pekerja dan"
                        " karyawan yang menjadi anggota koperasi. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Daftar pekerja yang menjadi anggota koperasi"
                                " yang termutakhir."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki daftar anggota"
                                " koperasi."
                            ),
                            "fail": "Tidak memenuhi Jika tidak memiliki.",
                        }
                    ],
                },
            ],
        },
    ],
}