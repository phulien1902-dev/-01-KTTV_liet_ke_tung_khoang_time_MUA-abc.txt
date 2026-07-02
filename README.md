🌧️ Liệt kê thời gian mưa từ nhiều file TXT

Công cụ Python giúp đọc nhiều file dữ liệu TXT của các trạm khí tượng, tự động trích xuất thời gian xuất hiện mưa và xuất kết quả ra file Excel (.xlsx).

Đây là công cụ hữu ích cho việc tổng hợp dữ liệu khí tượng, kiểm tra chất lượng dữ liệu và thống kê hiện tượng mưa.

✨ Chức năng
Đọc đồng thời nhiều file .txt.
Tự động tìm vùng dữ liệu giữa:
DAILY_DATA
RAW_HOURLY_GRAPH_DATA
Trích xuất:
Mã trạm
Năm
Tháng
Ngày
Chuỗi thời gian mưa (mt, mr)
Loại bỏ các thông tin không liên quan như .dg, .sh, .sk,...
Xuất toàn bộ kết quả ra một file Excel.
📋 Định dạng dữ liệu đầu ra
STT	Mã trạm	Năm	Tháng	Ngày	Thời gian mưa
1	48001	2025	6	12	mt06-08.mr14-15
2	48002	2025	6	13	mr03-05
🖥️ Giao diện

Chương trình sử dụng giao diện Tkinter, rất đơn giản:

Nhấn Chọn nhiều file TXT và xuất Excel
Chọn các file cần xử lý
Chọn vị trí lưu file Excel
Chương trình tự động tổng hợp dữ liệu
📦 Thư viện sử dụng
tkinter
pandas
openpyxl
re

Cài đặt:

pip install pandas openpyxl
▶️ Cách chạy
python get_thoi_gian_MUA_tu_nhieu_file_TXT_OK.py
⚙️ Nguyên lý hoạt động

Chương trình thực hiện các bước:

Chọn nhiều file TXT.
Đọc từng file.
Xác định vùng dữ liệu DAILY_DATA.
Lấy cột hiện tượng thời tiết.
Trích xuất các chuỗi bắt đầu bằng:
mt
mr
Tổng hợp toàn bộ dữ liệu.
Xuất sang Excel.
📁 Kết quả

File Excel đầu ra gồm các cột:

STT
Mã trạm
Năm
Tháng
Ngày
Thời gian mưa
💡 Ứng dụng
Tổng hợp thời gian mưa của nhiều trạm.
Kiểm tra dữ liệu khí tượng.
Phân tích số liệu thủy văn.
Hỗ trợ nghiên cứu và thống kê thời tiết.
Làm dữ liệu đầu vào cho các phần mềm GIS hoặc phân tích dữ liệu.
