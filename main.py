import io
import json
import os
import re
import sqlite3
import pandas as pd
import streamlit as st
from docx import Document

# Import modul data ISPO lengkap dari Prinsip 1 sampai 7
from data_ispo.prinsip_1 import PRINSIP_1_DATA
from data_ispo.prinsip_2 import PRINSIP_2_DATA
from data_ispo.prinsip_3 import PRINSIP_3_DATA
from data_ispo.prinsip_4 import PRINSIP_4_DATA
from data_ispo.prinsip_5 import PRINSIP_5_DATA
from data_ispo.prinsip_6 import PRINSIP_6_DATA
from data_ispo.prinsip_7 import PRINSIP_7_DATA

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Smart Audit ISPO - Permentan 33/2025",
    page_icon="🌴",
    layout="wide",
)

DB_PATH = "smart_audit_ispo.db"
UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
  os.makedirs(UPLOAD_DIR)

# List data gabungan seluruh 7 Prinsip ISPO
ISPO_PRINCIPIES_DATA = [
    PRINSIP_1_DATA,
    PRINSIP_2_DATA,
    PRINSIP_3_DATA,
    PRINSIP_4_DATA,
    PRINSIP_5_DATA,
    PRINSIP_6_DATA,
    PRINSIP_7_DATA,
]


# ==========================================
# INISIALISASI & MIGRASI DATABASE (RBAC & PASSWORD)
# ==========================================
def init_db():
  conn = sqlite3.connect(DB_PATH, check_same_thread=False)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()

  cursor.execute("""CREATE TABLE IF NOT EXISTS prinsip (
        id INTEGER PRIMARY KEY AUTOINCREMENT, prinsip_no INTEGER UNIQUE, nama TEXT NOT NULL
    );""")
  cursor.execute("""CREATE TABLE IF NOT EXISTS kriteria (
        id INTEGER PRIMARY KEY AUTOINCREMENT, prinsip_id INTEGER, code TEXT NOT NULL, nama TEXT NOT NULL,
        FOREIGN KEY (prinsip_id) REFERENCES prinsip (id)
    );""")
  cursor.execute("""CREATE TABLE IF NOT EXISTS indikator (
        id INTEGER PRIMARY KEY AUTOINCREMENT, kriteria_id INTEGER, indikator_no INTEGER, deskripsi TEXT NOT NULL,
        FOREIGN KEY (kriteria_id) REFERENCES kriteria (id)
    );""")
  cursor.execute("""CREATE TABLE IF NOT EXISTS parameter (
        id INTEGER PRIMARY KEY AUTOINCREMENT, indikator_id INTEGER, parameter_text TEXT NOT NULL,
        verifikasi_dokumen BOOLEAN, verifikasi_wawancara BOOLEAN, verifikasi_observasi BOOLEAN,
        norma_memenuhi TEXT, norma_tidak_memenuhi TEXT,
        FOREIGN KEY (indikator_id) REFERENCES indikator (id)
    );""")
  
  # Tabel Sesi Audit / Perusahaan
  cursor.execute("""CREATE TABLE IF NOT EXISTS audit_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_perusahaan TEXT NOT NULL,
        jenis_entitas TEXT,
        lead_auditor TEXT,
        tanggal_audit TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );""")

  # Tabel Hasil Audit (CASCADE Hapus jika sesi dihapus)
  cursor.execute("""CREATE TABLE IF NOT EXISTS audit_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        parameter_id INTEGER,
        status TEXT,
        catatan TEXT,
        file_paths TEXT,
        tindakan_perbaikan TEXT,
        target_tanggal TEXT,
        penanggung_jawab TEXT,
        UNIQUE(session_id, parameter_id),
        FOREIGN KEY (session_id) REFERENCES audit_sessions (id) ON DELETE CASCADE,
        FOREIGN KEY (parameter_id) REFERENCES parameter (id)
    );""")

  # Tabel User dengan Password
  cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        assigned_session_id INTEGER,
        FOREIGN KEY (assigned_session_id) REFERENCES audit_sessions (id) ON DELETE SET NULL
    );""")

  # Migrasi kolom password jika tabel users lama belum memilikinya
  cursor.execute("PRAGMA table_info(users);")
  user_cols = [col["name"] for col in cursor.fetchall()]
  if "password" not in user_cols:
    cursor.execute("ALTER TABLE users ADD COLUMN password TEXT DEFAULT 'admin123';")

  # Seed akun default jika tabel user kosong
  cursor.execute("SELECT COUNT(*) as cnt FROM users;")
  if cursor.fetchone()["cnt"] == 0:
    cursor.execute("INSERT INTO audit_sessions (nama_perusahaan, jenis_entitas, lead_auditor, tanggal_audit) VALUES ('PT. MUSTIKA AGUNG', 'Perusahaan', 'Ahmad Auditor, S.P.', '2026-01-01');")
    conn.commit()
    cursor.execute("SELECT id FROM audit_sessions LIMIT 1;")
    default_sid = cursor.fetchone()["id"]
    
    # Buat akun bawaan dengan password awal
    cursor.executemany("INSERT INTO users (username, password, role, assigned_session_id) VALUES (?, ?, ?, ?);", [
        ("superadmin", "super2026", "super_admin", None),
        ("admin_mustika", "admin123", "admin", default_sid),
        ("viewer_tamu", "tamu123", "user", default_sid)
    ])
    conn.commit()

  # Synchronize Master Data ISPO ke Database
  for p in ISPO_PRINCIPIES_DATA:
    cursor.execute(
        """
            INSERT INTO prinsip (prinsip_no, nama) VALUES (?, ?)
            ON CONFLICT(prinsip_no) DO UPDATE SET nama=excluded.nama
        """,
        (p["prinsip_no"], p["prinsip_nama"]),
    )

    cursor.execute("SELECT id FROM prinsip WHERE prinsip_no = ?", (p["prinsip_no"],))
    prinsip_id = cursor.fetchone()["id"]

    for k in p["kriteria"]:
      cursor.execute("SELECT id FROM kriteria WHERE prinsip_id = ? AND code = ?", (prinsip_id, k["code"]))
      k_row = cursor.fetchone()
      if not k_row:
        cursor.execute("INSERT INTO kriteria (prinsip_id, code, nama) VALUES (?, ?, ?)", (prinsip_id, k["code"], k["nama"]))
        kriteria_id = cursor.lastrowid
      else:
        kriteria_id = k_row["id"]
        cursor.execute("UPDATE kriteria SET nama = ? WHERE id = ?", (k["nama"], kriteria_id))

      for ind in k["indikator"]:
        cursor.execute("SELECT id FROM indikator WHERE kriteria_id = ? AND indikator_no = ?", (kriteria_id, ind["no"]))
        ind_row = cursor.fetchone()
        if not ind_row:
          cursor.execute("INSERT INTO indikator (kriteria_id, indikator_no, deskripsi) VALUES (?, ?, ?)", (kriteria_id, ind["no"], ind["deskripsi"]))
          indikator_id = cursor.lastrowid
        else:
          indikator_id = ind_row["id"]
          cursor.execute("UPDATE indikator SET deskripsi = ? WHERE id = ?", (ind["deskripsi"], indikator_id))

        for param in ind["params"]:
          cursor.execute("SELECT id FROM parameter WHERE indikator_id = ? AND parameter_text = ?", (indikator_id, param["text"]))
          p_row = cursor.fetchone()
          if not p_row:
            cursor.execute(
                """
                            INSERT INTO parameter (
                                indikator_id, parameter_text, verifikasi_dokumen, 
                                verifikasi_wawancara, verifikasi_observasi, norma_memenuhi, norma_tidak_memenuhi
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                (indikator_id, param["text"], param["doc"], param["interview"], param["obs"], param["pass"], param["fail"]),
            )

  conn.commit()
  return conn


conn = init_db()
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON;")


# ==========================================
# SIDEBAR: AUTENTIKASI PASSWORD & LOGIN
# ==========================================
st.sidebar.title("🔐 Login Pengguna")

cursor.execute("SELECT username FROM users")
usernames = [u["username"] for u in cursor.fetchall()]

selected_username = st.sidebar.selectbox("Pilih Akun", options=usernames)
input_password = st.sidebar.text_input("Masukkan Password", type="password")

cursor.execute("SELECT * FROM users WHERE username = ?", (selected_username,))
current_user = cursor.fetchone()

# Validasi Login
is_authenticated = False
if current_user and input_password == current_user["password"]:
  is_authenticated = True
else:
  if input_password != "":
    st.sidebar.error("⚠️ Password salah!")

if not is_authenticated:
  st.sidebar.warning("Silakan masukkan password yang valid untuk mengakses sistem.")
  st.stop()

role_labels = {
    "super_admin": "👑 Super Admin (Akses Penuh Semua)",
    "admin": "🛡️ Admin (Akses 1 Perusahaan)",
    "user": "👁️ Viewer (Hanya Lihat & Download)"
}
st.sidebar.success(f"Login Berhasil sebagai **{selected_username}**")
st.sidebar.info(f"Hak Akses: **{role_labels.get(current_user['role'], 'User')}**")

st.sidebar.markdown("---")
st.sidebar.title("📝 Sesi Audit & Perusahaan")

cursor.execute("SELECT id, nama_perusahaan, lead_auditor FROM audit_sessions ORDER BY id DESC")
sessions = cursor.fetchall()
session_options = {s["id"]: f"{s['nama_perusahaan']} (Lead: {s['lead_auditor']})" for s in sessions}

if current_user["role"] == "super_admin":
  if session_options:
    selected_session_id = st.sidebar.selectbox(
        "Pilih Sesi Perusahaan",
        options=list(session_options.keys()),
        format_func=lambda x: session_options[x],
    )
  else:
    selected_session_id = None

  with st.sidebar.expander("➕ Buat Sesi Audit Baru"):
    with st.form("new_session_form"):
      new_comp = st.text_input("Nama Perusahaan / Koperasi")
      new_ent = st.selectbox("Jenis Entitas", ["Perusahaan", "Koperasi / Pekebun"])
      new_auditor = st.text_input("Nama Lead Auditor", "Tim Auditor")
      submit_new = st.form_submit_button("Buat & Aktifkan Sesi")
      if submit_new and new_comp:
        cursor.execute("""
            INSERT INTO audit_sessions (nama_perusahaan, jenis_entitas, lead_auditor, tanggal_audit) 
            VALUES (?, ?, ?, datetime('now'))
        """, (new_comp, new_ent, new_auditor))
        conn.commit()
        st.success(f"Sesi {new_comp} berhasil dibuat!")
        st.rerun()

  # FITUR HAPUS SESI AUDIT (KHUSUS SUPER ADMIN)
  if session_options:
    with st.sidebar.expander("🗑️ Hapus Sesi Audit"):
      with st.form("del_session_form"):
        del_target_id = st.selectbox(
            "Pilih Sesi yang Akan Dihapus",
            options=list(session_options.keys()),
            format_func=lambda x: session_options[x],
            key="del_sess_select"
        )
        confirm_del = st.form_submit_button("⚠️ Hapus Sesi Ini Secara Permanen")
        if confirm_del:
          cursor.execute("DELETE FROM audit_results WHERE session_id = ?", (del_target_id,))
          cursor.execute("DELETE FROM audit_sessions WHERE id = ?", (del_target_id,))
          conn.commit()
          st.success("Sesi audit berhasil dihapus permanen!")
          st.rerun()

  # ==========================================
  # FITUR MANAJEMEN AKUN, PASSWORD & HAPUS AKUN (SUPER ADMIN)
  # ==========================================
  with st.sidebar.expander("🔑 Kelola Akun & Password"):
    st.markdown("### Tambah Akun Baru")
    with st.form("add_user_form"):
      new_uname = st.text_input("Username Baru")
      new_pass = st.text_input("Password Baru", type="password")
      new_role = st.selectbox("Tingkatan Role", ["admin", "user", "super_admin"])
      
      cursor.execute("SELECT id, nama_perusahaan FROM audit_sessions")
      sess_list = cursor.fetchall()
      sess_map = {s["id"]: s["nama_perusahaan"] for s in sess_list}
      
      assign_sid = None
      if sess_map and new_role != "super_admin":
        assign_sid = st.selectbox("Tugaskan ke Perusahaan", options=list(sess_map.keys()), format_func=lambda x: sess_map[x])
      
      submit_user = st.form_submit_button("Simpan Akun Baru")
      if submit_user and new_uname and new_pass:
        try:
          cursor.execute("INSERT INTO users (username, password, role, assigned_session_id) VALUES (?, ?, ?, ?)", 
                         (new_uname, new_pass, new_role, assign_sid))
          conn.commit()
          st.success(f"Akun `{new_uname}` berhasil dibuat!")
          st.rerun()
        except Exception as e:
          st.error(f"Gagal membuat akun (Username mungkin sudah ada): {e}")

    st.markdown("---")
    st.markdown("### Ubah Password Akun")
    with st.form("change_pass_form"):
      cursor.execute("SELECT username FROM users")
      target_users = [u["username"] for u in cursor.fetchall()]
      target_uname = st.selectbox("Pilih Akun", options=target_users)
      updated_pass = st.text_input("Password Baru", type="password")
      submit_pass = st.form_submit_button("Perbarui Password")
      if submit_pass and updated_pass:
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (updated_pass, target_uname))
        conn.commit()
        st.success(f"Password untuk akun `{target_uname}` berhasil diperbarui!")
        st.rerun()

    st.markdown("---")
    st.markdown("### Hapus Akun Pengguna")
    with st.form("del_user_form"):
      cursor.execute("SELECT id, username FROM users")
      all_usr_list = cursor.fetchall()
      usr_map = {u["id"]: u["username"] for u in all_usr_list}
      
      del_uid = st.selectbox("Pilih Akun yang Dihapus", options=list(usr_map.keys()), format_func=lambda x: usr_map[x])
      submit_del_user = st.form_submit_button("⚠️ Hapus Akun Ini")
      if submit_del_user:
        # Jangan biarkan menghapus diri sendiri jika sedang login sebagai superadmin aktif yang tersisa, atau beri peringatan
        cursor.execute("DELETE FROM users WHERE id = ?", (del_uid,))
        conn.commit()
        st.success("Akun berhasil dihapus permanen!")
        st.rerun()
else:
  selected_session_id = current_user["assigned_session_id"]
  cursor.execute("SELECT nama_perusahaan, lead_auditor FROM audit_sessions WHERE id = ?", (selected_session_id,))
  res_comp = cursor.fetchone()
  c_name = res_comp["nama_perusahaan"] if res_comp else "Perusahaan Ditugaskan"
  c_auditor = res_comp["lead_auditor"] if res_comp else "-"
  st.sidebar.markdown(f"Perusahaan Aktif:\n> **{c_name}**\nLead Auditor:\n> **{c_auditor}**")

if not session_options and current_user["role"] == "super_admin":
  st.warning("Belum ada sesi perusahaan yang tersedia. Silakan buat sesi audit baru melalui sidebar.")
  st.stop()

# Ambil detail sesi aktif
cursor.execute("SELECT * FROM audit_sessions WHERE id = ?", (selected_session_id,))
active_session = cursor.fetchone()
st.session_state["session_id"] = active_session["id"]
st.session_state["nama_perusahaan"] = active_session["nama_perusahaan"]
st.session_state["lead_auditor"] = active_session["lead_auditor"]

st.sidebar.success(f"Sesi Aktif: **{st.session_state['nama_perusahaan']}**")


# ==========================================
# FUNGSI BACKUP & RESTORE DATABASE
# ==========================================
def get_db_backup_bytes():
  with open(DB_PATH, "rb") as f:
    return f.read()


def restore_db_from_uploaded_file(uploaded_file):
  try:
    with open(DB_PATH, "wb") as f:
      f.write(uploaded_file.getbuffer())
    return True
  except Exception as e:
    return False


# ==========================================
# FUNGSI GENERATOR LAPORAN WORD LENGKAP
# ==========================================
def generate_word_report(cursor, session_id, nama_perusahaan, lead_auditor):
  doc = Document()
  doc.add_heading("Laporan Resmi Smart Audit ISPO", level=1)
  doc.add_paragraph(f"Nama Perusahaan / Koperasi: {nama_perusahaan}")
  doc.add_paragraph(f"Lead Auditor: {lead_auditor}")
  doc.add_paragraph("Standar Acuan: Peraturan Menteri Pertanian (Permentan) No. 33 Tahun 2025")
  doc.add_paragraph("---")

  cursor.execute("""
        SELECT 
            COUNT(pa.id) as total_param,
            SUM(CASE WHEN a.status = 'COMPLY' THEN 1 ELSE 0 END) as comply,
            SUM(CASE WHEN a.status = 'N/A' THEN 1 ELSE 0 END) as na_count
        FROM parameter pa
        LEFT JOIN audit_results a ON pa.id = a.parameter_id AND a.session_id = ?
    """, (session_id,))
  stats = cursor.fetchone()
  t_param = stats["total_param"] or 0
  t_na = stats["na_count"] or 0
  t_comply = stats["comply"] or 0
  p_aktif = t_param - t_na
  skor_akhir = (t_comply / p_aktif * 100) if p_aktif > 0 else 0

  cursor.execute("""
        SELECT p.prinsip_no, p.nama AS prinsip_nama, 
               k.code AS kriteria_code, k.nama AS kriteria_nama,
               i.indikator_no, i.deskripsi AS indikator_desc,
               pa.parameter_text, 
               COALESCE(a.status, 'BELUM DINILAI') as status,
               COALESCE(a.catatan, '-') as catatan
        FROM prinsip p
        JOIN kriteria k ON p.id = k.prinsip_id
        JOIN indikator i ON k.id = i.kriteria_id
        JOIN parameter pa ON i.id = pa.indikator_id
        LEFT JOIN audit_results a ON pa.id = a.parameter_id AND a.session_id = ?
        ORDER BY p.prinsip_no, k.code, i.indikator_no
    """, (session_id,))
  rows = cursor.fetchall()

  doc.add_heading("Ringkasan Hasil Evaluasi Parameter", level=2)
  table = doc.add_table(rows=1, cols=5)
  table.style = "Table Grid"
  hdr_cells = table.rows[0].cells
  hdr_cells[0].text = "Prinsip / Kriteria"
  hdr_cells[1].text = "Indikator"
  hdr_cells[2].text = "Parameter"
  hdr_cells[3].text = "Status"
  hdr_cells[4].text = "Catatan / Dokumen"

  for row in rows:
    row_cells = table.add_row().cells
    row_cells[0].text = f"Prinsip {row['prinsip_no']}\nKr. {row['kriteria_code']}"
    row_cells[1].text = f"Indikator #{row['indikator_no']}:\n{row['indikator_desc']}"
    row_cells[2].text = row["parameter_text"]
    row_cells[3].text = row["status"]
    row_cells[4].text = row["catatan"]

  doc.add_paragraph("\n---")
  doc.add_heading("Rekapitulasi Total Skor Kepatuhan", level=2)
  doc.add_paragraph(f"• Total Parameter Keseluruhan: {t_param}")
  doc.add_paragraph(f"• Parameter Dikecualikan (N/A): {t_na}")
  doc.add_paragraph(f"• Parameter Aktif Terpenuhi (Comply): {t_comply}")
  doc.add_paragraph(f"• **Skor Kepatuhan Efektif Keseluruhan: {skor_akhir:.2f}%**")

  buffer = io.BytesIO()
  doc.save(buffer)
  buffer.seek(0)
  return buffer


# ==========================================
# FUNGSI GENERATOR LAPORAN TEMUAN NC & CAPA
# ==========================================
def generate_word_not_comply_report(cursor, session_id, nama_perusahaan, lead_auditor):
  doc = Document()
  doc.add_heading("Laporan Temuan Ketidaksesuaian & Matriks CAPA", level=1)
  doc.add_paragraph(f"Nama Perusahaan / Koperasi: {nama_perusahaan}")
  doc.add_paragraph(f"Lead Auditor: {lead_auditor}")
  doc.add_paragraph("Standar Acuan: Peraturan Menteri Pertanian (Permentan) No. 33 Tahun 2025")
  doc.add_paragraph("Catatan: Dokumen ini memuat temuan audit (NOT COMPLY) beserta Rencana Tindakan Perbaikan (CAPA).")
  doc.add_paragraph("---")

  cursor.execute("""
        SELECT p.prinsip_no, p.nama AS prinsip_nama, 
               k.code AS kriteria_code, k.nama AS kriteria_nama,
               i.indikator_no, i.deskripsi AS indikator_desc,
               pa.parameter_text, pa.norma_tidak_memenuhi,
               COALESCE(a.catatan, '-') as catatan,
               COALESCE(a.tindakan_perbaikan, '-') as tindakan_perbaikan,
               COALESCE(a.target_tanggal, '-') as target_tanggal,
               COALESCE(a.penanggung_jawab, '-') as penanggung_jawab
        FROM prinsip p
        JOIN kriteria k ON p.id = k.prinsip_id
        JOIN indikator i ON k.id = i.kriteria_id
        JOIN parameter pa ON i.id = pa.indikator_id
        JOIN audit_results a ON pa.id = a.parameter_id AND a.session_id = ?
        WHERE a.status = 'NOT COMPLY'
        ORDER BY p.prinsip_no, k.code, i.indikator_no
    """, (session_id,))
  rows = cursor.fetchall()

  if not rows:
    doc.add_paragraph("Tidak ada temuan ketidaksesuaian (NOT COMPLY) yang tercatat.")
  else:
    table = doc.add_table(rows=1, cols=5)
    table.style = "Table Grid"
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Prinsip / Kriteria"
    hdr_cells[1].text = "Parameter & Norma NC"
    hdr_cells[2].text = "Catatan Temuan"
    hdr_cells[3].text = "Tindakan Perbaikan (CAPA)"
    hdr_cells[4].text = "PIC & Target"

    for row in rows:
      row_cells = table.add_row().cells
      row_cells[0].text = f"Prinsip {row['prinsip_no']}\nKr. {row['kriteria_code']}"
      row_cells[1].text = f"Param: {row['parameter_text']}\n\nNorma NC: {row['norma_tidak_memenuhi']}"
      row_cells[2].text = row["catatan"]
      row_cells[3].text = row["tindakan_perbaikan"]
      row_cells[4].text = f"PIC: {row['penanggung_jawab']}\nTarget: {row['target_tanggal']}"

  buffer = io.BytesIO()
  doc.save(buffer)
  buffer.seek(0)
  return buffer


# ==========================================
# FUNGSI GENERATOR LAPORAN EXCEL (.xlsx)
# ==========================================
def generate_excel_report(cursor, session_id, nama_perusahaan):
  cursor.execute("""
        SELECT p.prinsip_no AS Prinsip, 
               k.code AS Kode_Kriteria, k.nama AS Nama_Kriteria,
               i.indikator_no AS No_Indikator, i.deskripsi AS Deskripsi_Indikator,
               pa.parameter_text AS Parameter, 
               COALESCE(a.status, 'BELUM DINILAI') AS Status,
               COALESCE(a.catatan, '-') AS Catatan,
               COALESCE(a.tindakan_perbaikan, '-') AS Tindakan_Perbaikan_CAPA,
               COALESCE(a.target_tanggal, '-') AS Target_CAPA,
               COALESCE(a.penanggung_jawab, '-') AS PIC_CAPA
        FROM prinsip p
        JOIN kriteria k ON p.id = k.prinsip_id
        JOIN indikator i ON k.id = i.kriteria_id
        JOIN parameter pa ON i.id = pa.indikator_id
        LEFT JOIN audit_results a ON pa.id = a.parameter_id AND a.session_id = ?
        ORDER BY p.prinsip_no, k.code, i.indikator_no
    """, (session_id,))
  rows = cursor.fetchall()
  data_list = [dict(row) for row in rows]
  df = pd.DataFrame(data_list)

  excel_buffer = io.BytesIO()
  with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Rekap_Audit_ISPO")

  excel_buffer.seek(0)
  return excel_buffer


# ==========================================
# FUNGSI DASHBOARD RINGKASAN & PROGRES
# ==========================================
def render_dashboard_ringkasan(cursor, session_id):
  st.markdown("## 📊 Dashboard Ringkasan & Progres Audit ISPO")
  st.markdown(f"**Perusahaan Sesi Aktif**: `{st.session_state['nama_perusahaan']}` | **Lead Auditor**: `{st.session_state['lead_auditor']}`")

  cursor.execute("""
        SELECT p.prinsip_no, p.nama, 
               COUNT(pa.id) as total_param,
               SUM(CASE WHEN a.status = 'COMPLY' THEN 1 ELSE 0 END) as comply,
               SUM(CASE WHEN a.status = 'NOT COMPLY' THEN 1 ELSE 0 END) as not_comply,
               SUM(CASE WHEN a.status = 'N/A' THEN 1 ELSE 0 END) as na_count
        FROM prinsip p
        JOIN kriteria k ON p.id = k.prinsip_id
        JOIN indikator i ON k.id = i.kriteria_id
        JOIN parameter pa ON i.id = pa.indikator_id
        LEFT JOIN audit_results a ON pa.id = a.parameter_id AND a.session_id = ?
        GROUP BY p.prinsip_no
    """, (session_id,))
  data_prinsip = cursor.fetchall()

  if not data_prinsip:
    st.info("Belum ada data audit yang tersimpan.")
    return

  total_semua = sum([row["total_param"] for row in data_prinsip])
  total_na = sum([row["na_count"] if row["na_count"] else 0 for row in data_prinsip])
  total_comply = sum([row["comply"] if row["comply"] else 0 for row in data_prinsip])

  parameter_aktif = total_semua - total_na
  skor_keseluruhan = (total_comply / parameter_aktif * 100) if parameter_aktif > 0 else 0

  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.metric("Total Parameter Aktif", parameter_aktif)
  with col2:
    st.metric("Parameter N/A (Dikecualikan)", total_na)
  with col3:
    st.metric("Parameter Comply", total_comply)
  with col4:
    st.metric("Skor Kepatuhan Efektif", f"{skor_keseluruhan:.2f}%")

  st.markdown("---")
  st.subheader("📈 Progres Kepatuhan per Prinsip ISPO")

  for row in data_prinsip:
    p_no = row["prinsip_no"]
    p_nama = row["nama"]
    t_param = row["total_param"]
    comply = row["comply"] if row["comply"] else 0
    na_cnt = row["na_count"] if row["na_count"] else 0

    p_aktif = t_param - na_cnt
    persen = (comply / p_aktif) if p_aktif > 0 else 0

    st.markdown(f"**Prinsip {p_no}: {p_nama}** ({comply}/{p_aktif} Parameter Aktif Comply | {na_cnt} N/A)")
    st.progress(persen)

  st.markdown("---")
  st.subheader("📥 Unduh Laporan Resmi Audit")

  col_dl1, col_dl2, col_dl3 = st.columns(3)

  with col_dl1:
    docx_buffer = generate_word_report(cursor, session_id, st.session_state["nama_perusahaan"], st.session_state["lead_auditor"])
    st.download_button(
        label="📄 Download Laporan Lengkap (.docx)",
        data=docx_buffer,
        file_name=f"Laporan_Audit_Lengkap_{st.session_state['nama_perusahaan'].replace(' ', '_')}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

  with col_dl2:
    docx_nc_buffer = generate_word_not_comply_report(cursor, session_id, st.session_state["nama_perusahaan"], st.session_state["lead_auditor"])
    st.download_button(
        label="📑 Download Laporan Temuan NC & CAPA (.docx)",
        data=docx_nc_buffer,
        file_name=f"Laporan_Temuan_NotComply_CAPA_{st.session_state['nama_perusahaan'].replace(' ', '_')}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

  with col_dl3:
    excel_buffer = generate_excel_report(cursor, session_id, st.session_state["nama_perusahaan"])
    st.download_button(
        label="📊 Download Rekapitulasi Excel (.xlsx)",
        data=excel_buffer,
        file_name=f"Rekap_Audit_ISPO_{st.session_state['nama_perusahaan'].replace(' ', '_')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


# ==========================================
# SIDEBAR: NAVIGASI UTAMA
# ==========================================
st.sidebar.markdown("---")
st.sidebar.title("📌 Navigasi ISPO")

nav_mode = st.sidebar.radio(
    "Pilih Menu Utama",
    ["Dashboard Ringkasan", "Lembar Kerja Audit (Prinsip 1 - 7)"],
)

st.sidebar.markdown("---")

if nav_mode == "Lembar Kerja Audit (Prinsip 1 - 7)":
  cursor.execute("SELECT id, prinsip_no, nama FROM prinsip ORDER BY prinsip_no")
  prinsip_rows = cursor.fetchall()
  prinsip_options = {p["id"]: f"Prinsip {p['prinsip_no']}: {p['nama']}" for p in prinsip_rows}

  selected_prinsip_id = st.sidebar.selectbox(
      "Pilih Prinsip ISPO",
      options=list(prinsip_options.keys()),
      format_func=lambda x: prinsip_options[x],
  )

  cursor.execute("SELECT id, code, nama FROM kriteria WHERE prinsip_id = ?", (selected_prinsip_id,))
  kriteria_rows = cursor.fetchall()

  def extract_sort_key(k_row):
    match = re.search(r"\d+\.(\d+)", k_row["code"])
    return int(match.group(1)) if match else 0

  kriteria_rows_sorted = sorted(kriteria_rows, key=extract_sort_key)
  kriteria_options = {k["id"]: f"Kriteria {k['code']}: {k['nama']}" for k in kriteria_rows_sorted}

  st.sidebar.markdown("**Pilih Kriteria Audit:**")
  selected_kriteria_id = st.sidebar.radio(
      "Daftar Kriteria",
      options=list(kriteria_options.keys()),
      format_func=lambda x: kriteria_options[x],
      label_visibility="collapsed",
  )

# ==========================================
# SIDEBAR: MANAJEMEN DATABASE (Hanya Super Admin)
# ==========================================
if current_user["role"] == "super_admin":
  st.sidebar.markdown("---")
  st.sidebar.title("💾 Manajemen Database")

  db_bytes = get_db_backup_bytes()
  st.sidebar.download_button(
      label="📥 Backup Database (.db)",
      data=db_bytes,
      file_name="smart_audit_ispo_backup.db",
      mime="application/octet-stream",
      help="Unduh file database SQLite untuk cadangan data.",
  )

  uploaded_db = st.sidebar.file_uploader(
      "📤 Restore Database (.db)",
      type=["db"],
      help="Unggah file database .db cadangan untuk memulihkan data.",
  )

  if uploaded_db is not None:
    if st.sidebar.button("🔄 Konfirmasi Pemulihan Database"):
      if restore_db_from_uploaded_file(uploaded_db):
        st.sidebar.success("Database berhasil dipulihkan! Memuat ulang aplikasi...")
        st.rerun()
      else:
        st.sidebar.error("Gagal memulihkan database.")


# ==========================================
# HALAMAN UTAMA (RENDER BERDASARKAN NAV_MODE & ROLE)
# ==========================================
current_session_id = st.session_state["session_id"]
is_viewer = (current_user["role"] == "user")

if nav_mode == "Dashboard Ringkasan":
  render_dashboard_ringkasan(cursor, current_session_id)
else:
  if is_viewer:
    st.info("👁️ **Mode Viewer (Read-Only)**: Anda masuk sebagai User. Anda dapat melihat hasil penilaian, catatan, dan dokumen bukti tanpa izin mengubah atau menghapus data.")

  cursor.execute("""
      SELECT p.prinsip_no, p.nama AS prinsip_nama, k.code, k.nama AS kriteria_nama
      FROM kriteria k JOIN prinsip p ON k.prinsip_id = p.id WHERE k.id = ?
  """, (selected_kriteria_id,))
  curr = cursor.fetchone()

  if curr:
    st.title(f"Prinsip {curr['prinsip_no']}: {curr['prinsip_nama']}")
    st.subheader(f"Kriteria {curr['code']}: {curr['kriteria_nama']}")
    st.markdown(f"**Perusahaan Aktif**: `{st.session_state['nama_perusahaan']}` | **Lead Auditor**: `{st.session_state['lead_auditor']}`")
    st.markdown("---")

    cursor.execute("SELECT id, indikator_no, deskripsi FROM indikator WHERE kriteria_id = ? ORDER BY indikator_no", (selected_kriteria_id,))
    for ind in cursor.fetchall():
      with st.expander(f"📌 Indikator #{ind['indikator_no']}: {ind['deskripsi']}", expanded=True):
        cursor.execute("SELECT * FROM parameter WHERE indikator_id = ?", (ind["id"],))
        for pm in cursor.fetchall():
          param_id = pm["id"]

          cursor.execute("""
              SELECT status, catatan, file_paths, tindakan_perbaikan, target_tanggal, penanggung_jawab 
              FROM audit_results WHERE session_id = ? AND parameter_id = ?
          """, (current_session_id, param_id))
          existing_res = cursor.fetchone()

          saved_status = existing_res["status"] if existing_res else "COMPLY"
          saved_catatan = existing_res["catatan"] if existing_res else ""

          saved_capa = existing_res["tindakan_perbaikan"] if existing_res and "tindakan_perbaikan" in existing_res.keys() and existing_res["tindakan_perbaikan"] else ""
          saved_target = existing_res["target_tanggal"] if existing_res and "target_tanggal" in existing_res.keys() and existing_res["target_tanggal"] else ""
          saved_pic = existing_res["penanggung_jawab"] if existing_res and "penanggung_jawab" in existing_res.keys() and existing_res["penanggung_jawab"] else ""

          saved_files = []
          if existing_res and existing_res["file_paths"]:
            try:
              saved_files = json.loads(existing_res["file_paths"])
            except Exception:
              saved_files = []

          st.markdown(f"**Parameter Evaluation:**\n{pm['parameter_text']}")

          metode_list = []
          if pm["verifikasi_dokumen"]: metode_list.append("📄 Tinjauan Dokumen")
          if pm["verifikasi_wawancara"]: metode_list.append("🗣️ Wawancara")
          if pm["verifikasi_observasi"]: metode_list.append("🔍 Observasi")
          st.caption("Metode Verifikasi: " + " | ".join(metode_list))

          col_n1, col_n2 = st.columns(2)
          col_n1.info(f"✅ **Norma Memenuhi:**\n{pm['norma_memenuhi']}")
          col_n2.warning(f"❌ **Norma Tidak Memenuhi:**\n{pm['norma_tidak_memenuhi']}")

          c1, c2 = st.columns([1, 2])
          
          status_val = c1.selectbox(
              "Status Penilaian",
              ["COMPLY", "NOT COMPLY", "N/A"],
              index=["COMPLY", "NOT COMPLY", "N/A"].index(saved_status) if saved_status in ["COMPLY", "NOT COMPLY", "N/A"] else 0,
              key=f"status_{current_session_id}_{param_id}",
              disabled=is_viewer
          )
          catatan_val = c2.text_input(
              "Catatan / No Dokumen",
              value=saved_catatan,
              key=f"catatan_{current_session_id}_{param_id}",
              disabled=is_viewer
          )

          capa_val, target_val, pic_val = "", "", ""
          if status_val == "NOT COMPLY":
            st.markdown("📝 **Matriks Corrective Action Plan (CAPA) - Temuan Ketidaksesuaian**")
            capa_val = st.text_area(
                "Rencana Tindakan Perbaikan",
                value=saved_capa,
                key=f"capa_{current_session_id}_{param_id}",
                placeholder="Jelaskan langkah perbaikan untuk menutup temuan ini...",
                disabled=is_viewer
            )
            col_capa1, col_capa2 = st.columns(2)
            target_val = col_capa1.text_input(
                "Target Tanggal Penyelesaian",
                value=saved_target,
                key=f"target_{current_session_id}_{param_id}",
                placeholder="Contoh: 30 November 2026",
                disabled=is_viewer
            )
            pic_val = col_capa2.text_input(
                "Penanggung Jawab (PIC / Departemen)",
                value=saved_pic,
                key=f"pic_{current_session_id}_{param_id}",
                placeholder="Contoh: Manager Operasional / HRD",
                disabled=is_viewer
            )

          if not is_viewer:
            uploaded_files = st.file_uploader(
                "Upload Dokumen Bukti (Bisa Pilih Banyak File Sekaligus)",
                type=["pdf", "png", "jpg", "jpeg"],
                accept_multiple_files=True,
                key=f"up_{current_session_id}_{param_id}",
            )

            if uploaded_files:
              has_new_files = False
              for u_file in uploaded_files:
                file_path = os.path.join(UPLOAD_DIR, f"sesi_{current_session_id}_param_{param_id}_{u_file.name}").replace("\\", "/")

                if not os.path.exists(file_path):
                  with open(file_path, "wb") as f:
                    f.write(u_file.getbuffer())

                if file_path not in saved_files:
                  saved_files.append(file_path)
                  has_new_files = True

              if has_new_files:
                json_files = json.dumps(saved_files)
                cursor.execute("""
                    INSERT INTO audit_results (session_id, parameter_id, status, catatan, file_paths)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(session_id, parameter_id) DO UPDATE SET file_paths=excluded.file_paths
                """, (current_session_id, param_id, status_val, catatan_val, json_files))
                conn.commit()
                st.toast("File berhasil diunggah!", icon="📤")
                st.rerun()

          if saved_files:
            st.markdown("**📂 Dokumen Bukti Terlampir:**")
            for idx, fpath in enumerate(saved_files):
              col_f1, col_f2 = st.columns([4, 1])
              fname = os.path.basename(fpath)
              col_f1.caption(f"📄 `{fname}`")

              if not is_viewer:
                if col_f2.button("🗑️ Hapus", key=f"del_{current_session_id}_{param_id}_{idx}"):
                  if os.path.exists(fpath):
                    os.remove(fpath)
                  saved_files.pop(idx)
                  json_files_updated = json.dumps(saved_files)
                  cursor.execute("""
                      INSERT INTO audit_results (session_id, parameter_id, status, catatan, file_paths)
                      VALUES (?, ?, ?, ?, ?)
                      ON CONFLICT(session_id, parameter_id) DO UPDATE SET file_paths=excluded.file_paths
                  """, (current_session_id, param_id, status_val, catatan_val, json_files_updated))
                  conn.commit()
                  st.toast(f"File {fname} berhasil dihapus permanen!", icon="🗑️")
                  st.rerun()

          if not is_viewer:
            if st.button("💾 Simpan Penilaian", key=f"btn_{current_session_id}_{param_id}"):
              json_files = json.dumps(saved_files)
              cursor.execute("""
                  INSERT INTO audit_results (
                      session_id, parameter_id, status, catatan, file_paths, 
                      tindakan_perbaikan, target_tanggal, penanggung_jawab
                  )
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                  ON CONFLICT(session_id, parameter_id) DO UPDATE SET
                      status=excluded.status,
                      catatan=excluded.catatan,
                      file_paths=excluded.file_paths,
                      tindakan_perbaikan=excluded.tindakan_perbaikan,
                      target_tanggal=excluded.target_tanggal,
                      penanggung_jawab=excluded.penanggung_jawab
              """, (current_session_id, param_id, status_val, catatan_val, json_files, capa_val, target_val, pic_val))
              conn.commit()
              st.success(f"Berhasil! Penilaian & Matriks CAPA Parameter #{param_id} untuk sesi ini telah disimpan.")

          st.divider()