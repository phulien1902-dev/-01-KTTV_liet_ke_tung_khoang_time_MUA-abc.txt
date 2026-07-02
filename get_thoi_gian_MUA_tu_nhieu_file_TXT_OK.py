import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import re


#=========================================
# Lấy chuỗi mt và mr
#=========================================
def lay_thoi_gian_mua(chuoi):

    if not chuoi:
        return ""

    # bỏ khoảng trắng
    chuoi = chuoi.strip()

    # tìm vị trí bắt đầu của mt hoặc mr
    pattern = r'(mt|mr).*'

    m = re.search(pattern, chuoi)

    if m is None:
        return ""

    s = m.group(0)

    # cắt tại .dg .sh .sk ...
    cat = re.split(r'\.(?!\d)(?!$)', s)

    ket_qua = []

    for x in cat:
        if x.startswith("mt") or x.startswith("mr"):
            ket_qua.append(x)

    return ".".join(ket_qua)


#=========================================
# Đọc một file txt
#=========================================
def doc_file(file_path):

    rows = []

    bat_dau = False

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:

        for line in f:

            line = line.strip().replace('"', '')

            if line == "DAILY_DATA":
                bat_dau = True
                continue

            if line == "RAW_HOURLY_GRAPH_DATA":
                break

            if not bat_dau:
                continue

            cot = line.split(";")

            if len(cot) < 29:
                continue

            try:
                tram = cot[0].strip()
                nam = int(cot[1])
                thang = int(cot[2])
                ngay = int(cot[3])

                hientuong = cot[28].strip()

            except:
                continue

            thoi_gian_mua = lay_thoi_gian_mua(hientuong)

            if thoi_gian_mua != "":

                rows.append([
                    tram,
                    nam,
                    thang,
                    ngay,
                    thoi_gian_mua
                ])

    return rows


#=========================================
# Chọn nhiều file txt
#=========================================
def xu_ly():

    files = filedialog.askopenfilenames(
        title="Chọn các file txt",
        filetypes=[("Text files", "*.txt")]
    )

    if not files:
        return

    tat_ca = []

    stt = 1

    for file in files:

        data = doc_file(file)

        for row in data:

            tat_ca.append([
                stt,
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            ])

            stt += 1

    df = pd.DataFrame(
        tat_ca,
        columns=[
            "Stt",
            "Mã trạm",
            "Năm",
            "Tháng",
            "Ngày",
            "Thời gian mưa"
        ]
    )

    save_file = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel file", "*.xlsx")]
    )

    if save_file:

        with pd.ExcelWriter(save_file, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)

        messagebox.showinfo(
            "Thông báo",
            "Đã xuất Excel thành công!"
        )


#=========================================
# Giao diện
#=========================================
root = tk.Tk()
root.title("Liệt kê thời gian mưa từ nhiều file TXT")
root.geometry("500x180")

lbl = tk.Label(
    root,
    text="LIỆT KÊ THỜI GIAN MƯA",
    font=("Arial", 14, "bold")
)
lbl.pack(pady=20)

btn = tk.Button(
    root,
    text="Chọn nhiều file TXT và xuất Excel",
    width=35,
    height=2,
    command=xu_ly
)
btn.pack()

root.mainloop()