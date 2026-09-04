# data_ispo/prinsip_7.py
# Data Master ISPO - Prinsip 7 (Sesuai Lampiran Permentan No. 33 Tahun 2025)

PRINSIP_7_DATA = {
    "prinsip_no": 7,
    "prinsip_nama": "Peningkatan Usaha Secara Berkelanjutan",
    "kriteria": [
        {
            "code": "7.1",
            "nama": "Pemantauan dan Pembaruan Masa Berlaku Dokumen",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki mekanisme untuk"
                        " memantau dan memperbarui dokumen legalitas Perusahaan"
                        " Perkebunan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia SOP/Petunjuk teknis/Instruksi Kerja"
                                " untuk memantau dan memperbarui dokumen"
                                " legalitas Perusahaan Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki mekanisme untuk"
                                " memantau dan memperbarui dokumen legalitas"
                                " Perusahaan Perkebunan dan personil yang"
                                " bertanggung jawab."
                            ),
                            "fail": (
                                "Tidak memenuhi Jika tidak memiliki"
                                " mekanisme pemantauan dokumen legalitas."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia daftar seluruh dokumen legal yang"
                                " dimiliki oleh Perusahaan Perkebunan yang"
                                " berisi informasi paling sedikit: nama"
                                " dokumen; tanggal terbit; tanggal habis masa"
                                " berlaku;"
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada daftar dokumen legal"
                                " lengkap dengan masa berlaku."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak tersedia.",
                        },
                        {
                            "text": (
                                "Tersedia personil yang bertanggung jawab"
                                " terhadap seluruh dokumen yang diperlukan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada personil penanggung"
                                " jawab dokumen."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki inventarisasi dokumen"
                        " legalitas yang masih dalam proses pengajuan awal"
                        " maupun sedang dalam proses perpanjangan/ pembaruan."
                        " (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia inventarisasi dokumen legalitas yang"
                                " sedang berproses meliputi rencana dan"
                                " target penyelesaian."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki inventarisasi"
                                " dokumen legalitas yang sedang berproses"
                                " legal masih berlaku dan personil yang"
                                " bertanggung jawab."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak ada inventarisasi"
                                " dokumen berproses."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia personil yang bertanggung jawab"
                                " terhadap seluruh dokumen legalitas"
                                " Perusahaan Perkebunan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada personil penanggung"
                                " jawab legalitas."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
            ],
        },
        {
            "code": "7.2",
            "nama": "Program Peningkatan Usaha Perkebunan Berkelanjutan",
            "indikator": [
                {
                    "no": 1,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki dokumen tinjauan"
                        " manajemen terhadap seluruh kegiatan operasional"
                        " berdasarkan prinsip usaha berkelanjutan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia dokumen tinjauan manajemen yang"
                                " disahkan dan mencakup seluruh kegiatan"
                                " operasional Perusahaan Perkebunan atas"
                                " prinsip usaha berkelanjutan yang secara"
                                " rutin dilakukan minimal 1 (satu) tahun sekali."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki dokumen tinjauan"
                                " manajemen rutin tahunan."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki dokumen"
                                " tinjauan manajemen."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rekaman hasil audit internal ISPO"
                                " yang dilakukan oleh personil yang telah"
                                " mengikuti pelatihan ISPO."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman audit internal"
                                " oleh personil terlatih ISPO."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 2,
                    "deskripsi": (
                        "Perusahaan Perkebunan mengimplementasikan perbaikan"
                        " kegiatan operasional berdasarkan prinsip usaha"
                        " berkelanjutan. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia rekaman tindakan perbaikan dan"
                                " pencegahan dari hasil internal audit ISPO."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki seluruh dokumen"
                                " rekaman perbaikan audit internal."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki rekaman"
                                " perbaikan."
                            ),
                        },
                        {
                            "text": (
                                "Tersedia rekaman tindak lanjut terhadap"
                                " hasil pemeriksaan instansi terkait."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman tindak lanjut"
                                " pemeriksaan instansi."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia rekaman perbaikan dan peningkatan"
                                " sebagai tindak lanjut keputusan- keputusan"
                                " dari tinjauan manajemen."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika ada rekaman perbaikan tinjauan"
                                " manajemen."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                        {
                            "text": (
                                "Tersedia hasil evaluasi dari setiap"
                                " kegiatan perbaikan internal audit ISPO,"
                                " tinjauan manajemen."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": True,
                            "pass": (
                                "Memenuhi Jika ada hasil evaluasi perbaikan"
                                " dan tinjauan manajemen."
                            ),
                            "fail": "Tidak Memenuhi Jika tidak ada.",
                        },
                    ],
                },
                {
                    "no": 3,
                    "deskripsi": (
                        "Perusahaan Perkebunan memiliki Program Peningkatan"
                        " Operasional Usaha. (I, B, P)"
                    ),
                    "params": [
                        {
                            "text": (
                                "Tersedia rencana operasional usaha jangka"
                                " pendek, menengah dan panjang dalam rangka"
                                " peningkatan: produksi/produktivitas; skala"
                                " usaha; penjualan; penyerapan tenaga kerja;"
                                " atau bentuk upaya peningkatan lainnya yang"
                                " relevan."
                            ),
                            "doc": True,
                            "interview": True,
                            "obs": False,
                            "pass": (
                                "Memenuhi Jika memiliki Program Peningkatan"
                                " Operasional Usaha."
                            ),
                            "fail": (
                                "Tidak Memenuhi Jika tidak memiliki Program"
                                " Peningkatan Operasional Usaha."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
}