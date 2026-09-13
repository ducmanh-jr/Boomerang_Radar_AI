# -*- coding: utf-8 -*-
import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== KHỞI TẠO TIẾN TRÌNH XÂY DỰNG FILE DOCX CHUẨN MỰC ===")

doc = Document()

# -------------------------------------------------------------
# 1. ĐỊNH DẠNG TRANG IN CHUẨN VIỆT NAM (A4, LỀ 3-2-2-2)
# -------------------------------------------------------------
section = doc.sections[0]
section.page_width = Inches(8.27)   # A4 Width: 21.0 cm
section.page_height = Inches(11.69) # A4 Height: 29.7 cm
section.top_margin = Inches(0.79)    # 2.0 cm
section.bottom_margin = Inches(0.79) # 2.0 cm
section.left_margin = Inches(1.18)   # 3.0 cm (chuẩn đóng gáy)
section.right_margin = Inches(0.79)  # 2.0 cm

# -------------------------------------------------------------
# 2. THIẾT LẬP CÁC KIỂU CHỮ (STYLES) ĐƠN SẮC CHUẨN HỌC THUẬT
# -------------------------------------------------------------
styles = doc.styles

# Kiểu chữ mặc định (Normal Body)
normal_style = styles['Normal']
normal_font = normal_style.font
normal_font.name = 'Times New Roman'
normal_font.size = Pt(13)
normal_font.color.rgb = RGBColor(0, 0, 0)
normal_style.paragraph_format.line_spacing = 1.3
normal_style.paragraph_format.space_after = Pt(6)
normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# Hàm hỗ trợ định dạng bảng chuẩn Booktabs (Đường kẻ ngang đen, không màu mè)
def set_table_booktabs(table):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="12" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="12" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)
    
    # Định dạng dòng tiêu đề (Header)
    header_tr = table.rows[0]._tr.get_or_add_trPr()
    header_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    for cell in table.rows[0].cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>\n'
            f'  <w:bottom w:val="single" w:sz="10" w:space="0" w:color="000000"/>\n'
            f'</w:tcBorders>'
        )
        tcPr.append(tcBorders)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11.5)
                run.font.color.rgb = RGBColor(0, 0, 0)
                
    # Định dạng các dòng nội dung
    for row in table.rows[1:]:
        for cell in row.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(11)
                    run.font.color.rgb = RGBColor(0, 0, 0)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.first_line_indent = Inches(0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.first_line_indent = Inches(0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.first_line_indent = Inches(0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_body_p(text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Inches(0.5)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(6)
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.bold = True
        r_b.font.name = 'Times New Roman'
        r_b.font.size = Pt(13)
        r_b.font.color.rgb = RGBColor(0, 0, 0)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_bullet_p(text, bold_title=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.first_line_indent = Inches(0)
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_title:
        rb = p.add_run(bold_title)
        rb.font.bold = True
        rb.font.name = 'Times New Roman'
        rb.font.size = Pt(13)
        rb.font.color.rgb = RGBColor(0, 0, 0)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_formula_block(formula_text, note=None):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Inches(0)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(formula_text)
    run.font.name = 'Cambria Math'
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    
    if note:
        pn = doc.add_paragraph()
        pn.paragraph_format.first_line_indent = Inches(0.5)
        pn.paragraph_format.space_after = Pt(6)
        rn = pn.add_run(note)
        rn.font.name = 'Times New Roman'
        rn.font.size = Pt(11.5)
        rn.font.color.rgb = RGBColor(0, 0, 0)

# =============================================================
# TRANG 1: ĐỂ TRỐNG HOÀN TOÀN ĐỂ NGƯỜI DÙNG TỰ LÀM TRANG BÌA
# =============================================================
p_blank = doc.add_paragraph()
p_blank.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_blank.paragraph_format.space_before = Pt(250)
r_note = p_blank.add_run("[TRANG BÌA ĐƯỢC ĐỂ TRỐNG THEO YÊU CẦU - NGƯỜI DÙNG TỰ THIẾT KẾ TRANG BÌA]")
r_note.font.italic = True
r_note.font.size = Pt(12)
r_note.font.color.rgb = RGBColor(120, 120, 120)

doc.add_page_break()

# =============================================================
# TRANG 2: TÓM TẮT BÁO CÁO & MỤC LỤC & DANH MỤC
# =============================================================
p_sum = doc.add_paragraph()
p_sum.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sum.paragraph_format.space_before = Pt(10)
p_sum.paragraph_format.space_after = Pt(12)
r_sum = p_sum.add_run("TÓM TẮT ĐIỀU HÀNH BÁO CÁO (EXECUTIVE SUMMARY)")
r_sum.font.bold = True
r_sum.font.size = Pt(15)

add_body_p(
    "Báo cáo này trình bày toàn diện công trình nghiên cứu và xây dựng hệ thống Trí tuệ Nhân tạo Boomerang Radar AI "
    "nhằm giải quyết bài toán dự đoán khả năng khách hàng quay lại mua sắm (Customer Repurchase Prediction) và nhận diện "
    "sớm nguy cơ rời bỏ (Churn Risk) trong ngành bán lẻ và thương mại điện tử. Hệ thống tiếp nhận 8 đặc trưng hành vi RFM+ "
    "kết hợp nhân khẩu học và trải nghiệm dịch vụ, tự động sinh ra 4 biến tương tác phi tuyến giúp khai phá nhịp độ mua sắm "
    "và sự suy giảm lòng trung thành theo thời gian. Trên tập kiểm thử độc lập gồm 1.126 khách hàng, mô hình Gradient Boosting "
    "Classifier đạt hiệu năng vượt trội với độ chính xác (Accuracy) đạt 94.23%, điểm F1-Score đạt 96.56% và chỉ số ROC-AUC "
    "đạt 96.95%. Hệ thống được đóng gói hoàn chỉnh với dịch vụ REST API có độ trễ suy luận dưới 50ms, cung cấp phân tầng rủi ro "
    "4 cấp độ và ma trận hành động Marketing cụ thể với tỷ suất hoàn vốn đầu tư (ROI) dự kiến đạt 303.8%."
)

# MỤC LỤC
add_heading_1("MỤC LỤC NỘI DUNG")
toc_data = [
    ("TÓM TẮT ĐIỀU HÀNH VÀ DANH MỤC THUẬT NGỮ", "2"),
    ("1. PHÁT BIỂU BÀI TOÁN VÀ CƠ SỞ KHOA HỌC", "4"),
    ("   1.1. Bối cảnh kinh tế bán lẻ và bài toán chi phí giữ chân khách hàng", "4"),
    ("   1.2. Cơ sở lý thuyết Vòng đời Khách hàng và Giá trị Trọn đời (CLV)", "5"),
    ("   1.3. Mô hình toán học của bài toán Phân loại Khách hàng Quay lại", "6"),
    ("   1.4. Tuyên ngôn giá trị và Sứ mệnh của Boomerang Radar AI", "7"),
    ("2. XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT", "8"),
    ("   2.1. Yêu cầu chức năng và tiêu chuẩn phi chức năng", "8"),
    ("   2.2. Đặc tả 8 thuộc tính dữ liệu đầu vào (Input Specification)", "9"),
    ("   2.3. Cấu trúc dữ liệu đầu ra và Ma trận phân tầng 4 cấp rủi ro", "10"),
    ("3. THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG", "12"),
    ("   3.1. Kiến trúc phân tầng 6 lớp độc lập (6-Layer Architecture)", "12"),
    ("   3.2. Thiết kế luồng dữ liệu kép: Huấn luyện Offline và Suy luận Online", "14"),
    ("   3.3. Cơ chế quản lý tài nguyên mô hình và giao tiếp API Gateway", "15"),
    ("4. MÔ TẢ THUẬT TOÁN VÀ NỀN TẢNG TOÁN HỌC", "16"),
    ("   4.1. Cơ sở giải tích của 4 đặc trưng tương tác phi tuyến (Interaction Features)", "16"),
    ("   4.2. Thuật toán Hồi quy Logistic (Logistic Regression)", "18"),
    ("   4.3. Thuật toán Cây quyết định (Decision Tree Classifier)", "19"),
    ("   4.4. Thuật toán Rừng ngẫu nhiên (Random Forest Classifier)", "20"),
    ("   4.5. Thuật toán Gradient Boosting Classifier (Champion Model)", "22"),
    ("   4.6. Chiến lược tối ưu hóa siêu tham số qua RandomizedSearchCV và 5-Fold CV", "24"),
    ("5. MÔ TẢ DỮ LIỆU VÀ QUY TRÌNH TIỀN XỬ LÝ CHỐNG RÒ RỈ", "25"),
    ("   5.1. Nguồn dữ liệu và Thống kê mô tả khám phá (EDA)", "25"),
    ("   5.2. Vấn đề mất cân bằng mẫu và giải pháp Stratified Splitting", "26"),
    ("   5.3. Pipeline chuẩn hóa dữ liệu 14 chiều tuân thủ Anti-Data Leakage", "27"),
    ("6. CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG", "28"),
    ("   6.1. Môi trường công nghệ và Cấu trúc mã nguồn Clean Code", "28"),
    ("   6.2. Cài đặt chi tiết các Module lõi (data_processing, train, predict)", "29"),
    ("   6.3. Xây dựng dịch vụ REST API và Web Dashboard Bootstrap 5", "30"),
    ("7. ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM", "31"),
    ("   7.1. Bảng đối chuẩn hiệu năng thực nghiệm giữa 4 mô hình", "31"),
    ("   7.2. Phân tích Ma trận nhầm lẫn và Tác động kinh tế của sai số", "32"),
    ("   7.3. Xếp hạng độ quan trọng đặc trưng (Vai trò của Feature Engineering)", "33"),
    ("8. KẾ HOẠCH TRIỂN KHAI, HƯỚNG PHÁT TRIỂN VÀ KẾT LUẬN", "34"),
    ("   8.1. Kế hoạch triển khai hành động (Ma trận RACI, Gantt 12 tuần, Dự toán ROI)", "34"),
    ("   8.2. Ứng dụng Trí tuệ Nhân tạo có thể giải thích (Explainable AI với SHAP)", "36"),
    ("   8.3. Mở rộng kiến trúc thuật toán chuyên sâu (LightGBM, CatBoost, TabNet)", "37"),
    ("   8.4. Thiết lập hệ thống MLOps và Tự động hóa tiếp thị đa kênh", "37"),
    ("   8.5. Kết luận tổng quan đề tài", "38"),
    ("TÀI LIỆU THAM KHẢO (CHẤP HÀNH CHUẨN APA)", "39")
]

table_toc = doc.add_table(rows=1, cols=2)
table_toc.rows[0].cells[0].paragraphs[0].text = "Cấu trúc đề mục nội dung"
table_toc.rows[0].cells[1].paragraphs[0].text = "Trang"
table_toc.columns[0].width = Inches(5.5)
table_toc.columns[1].width = Inches(0.8)

for item, page in toc_data:
    row_cells = table_toc.add_row().cells
    p0 = row_cells[0].paragraphs[0]
    p0.text = item
    p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p1 = row_cells[1].paragraphs[0]
    p1.text = page
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT

set_table_booktabs(table_toc)

# BẢNG DANH MỤC THUẬT NGỮ
add_heading_2("DANH MỤC THUẬT NGỮ VÀ TỪ VIẾT TẮT")
terms_data = [
    ("CAC", "Customer Acquisition Cost", "Chi phí thu hút một khách hàng mới hoàn tất đơn hàng đầu tiên."),
    ("CLV / LTV", "Customer Lifetime Value", "Giá trị trọn đời của khách hàng đóng góp cho doanh nghiệp."),
    ("Churn Rate", "Tỷ lệ rời bỏ khách hàng", "Tỷ lệ khách hàng ngừng phát sinh giao dịch trong chu kỳ đánh giá."),
    ("Retention Rate", "Tỷ lệ giữ chân khách hàng", "Tỷ lệ khách hàng tiếp tục phát sinh đơn hàng lặp lại."),
    ("RFM+", "Recency, Frequency, Monetary +", "Khung phân tích hành vi theo độ mới, tần suất, giá trị đơn và trải nghiệm."),
    ("GBDT", "Gradient Boosted Decision Trees", "Thuật toán học máy kết hợp cây quyết định tối ưu hóa phần dư."),
    ("EDA", "Exploratory Data Analysis", "Phân tích khám phá dữ liệu ban đầu."),
    ("Anti-Leakage", "Chống rò rỉ dữ liệu", "Quy trình cô lập hoàn toàn tham số giữa tập Train và tập Test."),
    ("XAI", "Explainable Artificial Intelligence", "Trí tuệ Nhân tạo có khả năng giải thích tường minh cơ chế quyết định."),
    ("MLOps", "Machine Learning Operations", "Quy trình chuẩn hóa triển khai và vận hành mô hình học máy tự động.")
]

table_terms = doc.add_table(rows=1, cols=3)
table_terms.rows[0].cells[0].paragraphs[0].text = "Viết tắt"
table_terms.rows[0].cells[1].paragraphs[0].text = "Thuật ngữ tiếng Anh"
table_terms.rows[0].cells[2].paragraphs[0].text = "Ý nghĩa định nghĩa"
table_terms.columns[0].width = Inches(1.2)
table_terms.columns[1].width = Inches(2.2)
table_terms.columns[2].width = Inches(2.9)

for abbr, full, desc in terms_data:
    rc = table_terms.add_row().cells
    rc[0].paragraphs[0].text = abbr
    rc[1].paragraphs[0].text = full
    rc[2].paragraphs[0].text = desc

set_table_booktabs(table_terms)

doc.add_page_break()

# =============================================================
# CHƯƠNG 1: PHÁT BIỂU BÀI TOÁN VÀ CƠ SỞ KHOA HỌC
# =============================================================
add_heading_1("1. PHÁT BIỂU BÀI TOÁN VÀ CƠ SỞ KHOA HỌC")

add_heading_2("1.1. Bối cảnh kinh tế bán lẻ và bài toán chi phí giữ chân khách hàng")
add_body_p(
    "Trong bối cảnh bùng nổ của thương mại điện tử và bán lẻ đa kênh, người tiêu dùng đứng trước vô số lựa chọn với "
    "rào cản chuyển đổi giữa các thương hiệu gần như bằng không. Các nghiên cứu thị trường từ Bain & Company và Harvard "
    "Business Review chỉ ra rằng chi phí để thu hút một khách hàng mới (Customer Acquisition Cost - CAC) đắt gấp từ 5 đến 7 "
    "lần so với chi phí kích hoạt đơn hàng từ một khách hàng cũ. Việc liên tục chi tiêu ngân sách quảng cáo trực tuyến nhằm "
    "thu hút khách hàng giao dịch một lần rồi bỏ mặc đang làm suy giảm nghiêm trọng biên lợi nhuận ròng của các doanh nghiệp."
)
add_body_p(
    "Nút thắt cốt lõi trong các hệ thống quản trị quan hệ khách hàng (CRM) truyền thống hiện nay là cách tiếp cận hoàn toàn "
    "thụ động. Khách hàng chỉ được xếp vào nhóm 'đã rời bỏ' khi họ đã ngừng phát sinh đơn hàng từ 90 đến 180 ngày. Ở thời điểm này, "
    "mối quan tâm của khách hàng đã chuyển dịch sang đối thủ cạnh tranh, khiến chi phí để lôi kéo họ quay trở lại trở nên vô cùng "
    "tốn kém hoặc hoàn toàn bất khả thi. Do đó, nhu cầu cấp thiết đặt ra là phải xây dựng một giải pháp thông minh có khả năng "
    "phát hiện sớm các dấu hiệu phai nhạt tương tác ngay trong khoảng thời gian từ 30 đến 60 ngày đầu tiên."
)

add_heading_2("1.2. Cơ sở lý thuyết Vòng đời Khách hàng và Giá trị Trọn đời (CLV)")
add_body_p(
    "Về mặt kinh tế học hành vi, tổng giá trị của một doanh nghiệp phụ thuộc trực tiếp vào Giá trị trọn đời của tập khách hàng "
    "(Customer Lifetime Value - CLV). Theo công thức tài chính chiết khấu chuỗi thời gian chuẩn tắc:"
)

add_formula_block(
    "CLV = ∑ [ (p_t - c_t) × r_t ] / (1 + d)^t    (với t = 0 đến T)",
    "Trong đó: p_t là doanh thu kỳ vọng tại chu kỳ t; c_t là chi phí phục vụ trực tiếp; "
    "r_t là xác suất khách hàng tiếp tục quay lại mua sắm (Retention Rate); d là tỷ lệ chiết khấu chi phí vốn."
)

add_body_p(
    "Công thức giải tích trên khẳng định rằng xác suất khách hàng quay lại mua sắm (r_t) là biến số nhân tử trực tiếp chi phối độ lớn "
    "của CLV. Nếu r_t suy giảm về 0 (khách hàng rời bỏ), toàn bộ dòng tiền tiềm năng trong tương lai sẽ bị triệt tiêu, khiến doanh thu "
    "không đủ bù đắp chi phí CAC ban đầu. Ngược lại, việc nâng cao tỷ lệ giữ chân khách hàng thêm 5% có thể thúc đẩy lợi nhuận ròng "
    "tăng trưởng từ 25% đến 95% nhờ giảm thiểu chi phí tiếp thị lặp lại và tận dụng xu hướng khách hàng trung thành mua các đơn hàng "
    "có giá trị lớn hơn."
)

add_heading_2("1.3. Mô hình toán học của bài toán Phân loại Khách hàng Quay lại")
add_body_p(
    "Dưới góc nhìn Trí tuệ Nhân tạo, bài toán được mô hình hóa dưới dạng Học máy có giám sát - Phân loại nhị phân "
    "(Supervised Binary Classification) trên tập dữ liệu có tính chất mất cân bằng tự nhiên. Cho tập dữ liệu huấn luyện gồm N quan sát "
    "D = {(x_i, y_i)}, trong đó x_i là vector đặc trưng đại diện cho lịch sử giao dịch RFM, nhân khẩu học và trải nghiệm dịch vụ. "
    "Biến mục tiêu nhị phân y_i được định nghĩa:"
)

add_formula_block(
    "y_i = 1  nếu khách hàng sẽ quay lại mua sắm trong chu kỳ tiếp theo (Repurchase)\n"
    "y_i = 0  nếu khách hàng không quay lại / có nguy cơ rời bỏ (Churn)",
    "Mục tiêu của giải thuật học máy là học hàm giả thuyết f(x) ước lượng chính xác xác suất hậu nghiệm P(y_i = 1 | x_i)."
)

add_body_p(
    "Nhãn dự đoán nhị phân được gán thông qua ngưỡng quyết định θ (mặc định θ = 0.50): y_mũ = 1 nếu xác suất tính toán được lớn hơn "
    "hoặc bằng θ; ngược lại gán nhãn 0."
)

add_heading_2("1.4. Tuyên ngôn giá trị và Sứ mệnh của Boomerang Radar AI")
add_body_p(
    "Hệ thống Boomerang Radar AI hoạt động như một trạm radar thông minh quét liên tục dữ liệu hành vi của người tiêu dùng "
    "nhằm thực hiện ba sứ mệnh cốt lõi:"
)
add_bullet_p("Quét và định vị sớm những khách hàng đang có dấu hiệu giảm dần tần suất tương tác.", "Cơ chế phòng ngừa chủ động: ")
add_bullet_p("Chấm dứt việc phát voucher giảm giá đại trà làm suy giảm biên lợi nhuận, tập trung ngân sách kích cầu đúng đối tượng có nguy cơ rời bỏ nhưng vẫn có khả năng cứu vãn.", "Tối ưu hóa ngân sách tiếp thị: ")
add_bullet_p("Giống như nguyên lý khí động học của chiếc boomerang quay trở lại điểm phóng, hệ thống tự động kích hoạt các kịch bản can thiệp kịp thời để kéo khách hàng quay trở lại chu kỳ mua sắm lặp lại bền vững.", "Tạo hiệu ứng Boomerang: ")

# =============================================================
# CHƯƠNG 2: XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT
# =============================================================
add_heading_1("2. XÁC ĐỊNH YÊU CẦU HỆ THỐNG, INPUT VÀ OUTPUT")

add_heading_2("2.1. Yêu cầu chức năng và tiêu chuẩn phi chức năng")
add_heading_3("a. Yêu cầu chức năng (Functional Requirements - FR)")
add_bullet_p("Tiếp nhận 8 chỉ số qua form web, tự động tạo 4 biến tương tác phi tuyến, tính toán xác suất quay lại và phân tầng rủi ro trong thời gian dưới 50ms.", "FR-01: Dự đoán thời gian thực cho một khách hàng: ")
add_bullet_p("Hỗ trợ tải lên tệp tin CSV chứa hàng nghìn bản ghi, tự động suy luận hàng loạt và cung cấp tính năng xuất tệp tin kết quả có gắn nhãn và xác suất.", "FR-02: Xử lý theo lô từ tệp tin CSV: ")
add_bullet_p("Hiển thị bảng đối sánh 4 mô hình theo 5 chỉ số đo lường chuẩn mực, hiển thị ma trận nhầm lẫn và biểu đồ mức độ đóng góp của từng đặc trưng.", "FR-03: Đối chuẩn hiệu năng đa mô hình: ")
add_bullet_p("Thống kê tự động tỷ lệ khách quay lại thực tế (83%), tỷ lệ rời bỏ (17%), giá trị đơn hàng trung bình và cung cấp bảng xem trước dữ liệu mẫu.", "FR-04: Thống kê tổng quan dữ liệu vĩ mô: ")
add_bullet_p("Căn cứ vào xác suất quay lại, tự động phân nhóm khách hàng vào 4 cấp độ: Rất Thấp, Trung Bình, Cao, Rất Cao.", "FR-05: Tự động phân tầng mức độ rủi ro: ")
add_bullet_p("Tự động ghép nối các thuộc tính hành vi thành câu văn giải thích ngắn gọn, dễ hiểu và đề xuất hành động Marketing tương ứng.", "FR-06: Sinh phân tích hành vi và khuyến nghị nghiệp vụ: ")

add_heading_3("b. Tiêu chuẩn phi chức năng (Non-Functional Requirements - NFR)")
add_bullet_p("Đạt F1-score ≥ 92%, Accuracy ≥ 90%, ROC-AUC ≥ 0.90 trên tập kiểm thử độc lập (Held-out Test Set).", "NFR-01: Tiêu chuẩn độ chính xác cao: ")
add_bullet_p("Thời gian phản hồi truy vấn đơn lẻ qua REST API ≤ 50ms; thời gian xử lý tệp CSV 10.000 dòng ≤ 3 giây.", "NFR-02: Độ trễ phản hồi thấp: ")
add_bullet_p("Bộ chuẩn hóa và mã hóa chỉ được học phân phối thống kê từ tập Train, đóng băng toàn bộ tham số khi áp dụng trên tập Test.", "NFR-03: Tuyệt đối chống rò rỉ dữ liệu (Anti-Data Leakage): ")
add_bullet_p("Tách biệt hoàn toàn pipeline huấn luyện ngoại tuyến và phục vụ suy luận trực tuyến, hỗ trợ triển khai container hóa qua Docker.", "NFR-04: Tính độc lập và khả năng mở rộng: ")

add_heading_2("2.2. Đặc tả 8 thuộc tính dữ liệu đầu vào (Input Specification)")
add_body_p(
    "Dựa trên khung phân tích hành vi RFM+ kết hợp nhân khẩu học và trải nghiệm dịch vụ, hệ thống tiếp nhận 8 thuộc tính cốt lõi:"
)

input_table_data = [
    ("age", "Integer", "18 - 70 tuổi", "Nhân khẩu học", "Độ tuổi khách hàng. Nhóm 35-50 tuổi có xu hướng gắn kết ổn định hơn nhóm 18-25 tuổi vốn nhạy cảm về giá."),
    ("gender", "Categorical", "Nam, Nữ", "Nhân khẩu học", "Giới tính khách hàng. Khách hàng nữ có tần suất mua sắm lặp lại cao hơn 1.8 lần so với nam giới."),
    ("total_purchases", "Integer", "1 - 60 đơn", "Frequency (F)", "Tổng số đơn hàng đã hoàn tất. Khách hàng mua từ 3 đơn trở lên có tỷ lệ quay lại tự nhiên cao gấp 4 lần."),
    ("avg_order_value", "Float", "150.000 - 4.500.000 đ", "Monetary (M)", "Giá trị trung bình mỗi đơn hàng. Phản ánh quy mô ngân sách chi tiêu của khách hàng."),
    ("days_since_last_purchase", "Integer", "1 - 180 ngày", "Recency (R)", "Số ngày kể từ lần mua gần nhất. Khi vượt quá 60 ngày, rủi ro Churn tăng theo hàm số mũ."),
    ("membership_level", "Categorical", "Đồng, Bạc, Vàng, Kim Cương", "Hội viên", "Hạng thẻ thành viên tích lũy dựa trên doanh thu lũy kế."),
    ("used_voucher", "Binary", "0 (Không), 1 (Có)", "Khuyến mãi", "Đo lường mức độ phụ thuộc vào mã giảm giá của khách hàng."),
    ("satisfaction_score", "Integer", "1 - 5 sao", "Trải nghiệm (CSAT)", "Điểm đánh giá mức độ hài lòng dịch vụ từ khảo sát thực tế.")
]

tbl_in = doc.add_table(rows=1, cols=5)
tbl_in.rows[0].cells[0].paragraphs[0].text = "Tên thuộc tính"
tbl_in.rows[0].cells[1].paragraphs[0].text = "Kiểu"
tbl_in.rows[0].cells[2].paragraphs[0].text = "Miền giá trị"
tbl_in.rows[0].cells[3].paragraphs[0].text = "Phân nhóm"
tbl_in.rows[0].cells[4].paragraphs[0].text = "Ý nghĩa kinh doanh và Tương quan"

tbl_in.columns[0].width = Inches(1.3)
tbl_in.columns[1].width = Inches(0.8)
tbl_in.columns[2].width = Inches(1.2)
tbl_in.columns[3].width = Inches(1.1)
tbl_in.columns[4].width = Inches(2.1)

for r in input_table_data:
    row = tbl_in.add_row().cells
    for i in range(5):
        row[i].paragraphs[0].text = r[i]

set_table_booktabs(tbl_in)

add_heading_2("2.3. Cấu trúc dữ liệu đầu ra và Ma trận phân tầng 4 cấp rủi ro")
add_body_p(
    "Kết quả xử lý từ hệ thống được cấu trúc hóa dưới dạng JSON chuẩn mực bao gồm xác suất định lượng, tỷ lệ phần trăm rời bỏ, "
    "nhãn nhị phân, phân tầng mức độ rủi ro, chuỗi phân tích ngữ cảnh tự nhiên và đề xuất hành động nghiệp vụ cụ thể."
)

risk_matrix_data = [
    ("1. Rất Thấp (Safe)", "P > 80%", "P_churn < 20%", "Khách hàng trung thành, AOV cao, mới mua gần đây, CSAT 4-5 sao.", "Không giảm giá đại trà. Gửi thiệp cảm ơn, tích điểm VIP 15%, ưu tiên trải nghiệm sản phẩm mới."),
    ("2. Trung Bình (Attention)", "50% ≤ P ≤ 80%", "20% ≤ P_churn ≤ 50%", "Vẫn có ý định mua nhưng khoảng cách ngày mua đang dài ra; có tâm lý chờ khuyến mãi.", "Gửi thông báo đẩy nhắc nhở giỏ hàng, tặng voucher trợ giá 10% có thời hạn 48 giờ."),
    ("3. Cao (Warning)", "20% ≤ P < 50%", "50% < P_churn ≤ 80%", "Bắt đầu phai nhạt tương tác (> 60 ngày chưa mua), điểm CSAT 3 sao hoặc mua ít đơn.", "Kích hoạt chiến dịch We Miss You: tặng voucher giảm 20% kèm chính sách miễn phí giao hàng."),
    ("4. Rất Cao (Critical)", "P < 20%", "P_churn > 80%", "Báo động đỏ rời bỏ! Trên 90-120 ngày không phát sinh đơn, đánh giá 1-2 sao.", "Chuyển sang bộ phận CSKH đặc biệt: gọi điện thăm hỏi, hỗ trợ xử lý khiếu nại, tặng mã đền bù 25%.")
]

tbl_risk = doc.add_table(rows=1, cols=5)
tbl_risk.rows[0].cells[0].paragraphs[0].text = "Cấp bậc rủi ro"
tbl_risk.rows[0].cells[1].paragraphs[0].text = "Xác suất quay lại"
tbl_risk.rows[0].cells[2].paragraphs[0].text = "Nguy cơ rời bỏ"
tbl_risk.rows[0].cells[3].paragraphs[0].text = "Đặc điểm hành vi tiêu biểu"
tbl_risk.rows[0].cells[4].paragraphs[0].text = "Kịch bản hành động Marketing và CSKH"

tbl_risk.columns[0].width = Inches(1.3)
tbl_risk.columns[1].width = Inches(1.1)
tbl_risk.columns[2].width = Inches(1.1)
tbl_risk.columns[3].width = Inches(1.5)
tbl_risk.columns[4].width = Inches(1.5)

for r in risk_matrix_data:
    row = tbl_risk.add_row().cells
    for i in range(5):
        row[i].paragraphs[0].text = r[i]

set_table_booktabs(tbl_risk)

# =============================================================
# CHƯƠNG 3: THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG
# =============================================================
add_heading_1("3. THIẾT KẾ SƠ ĐỒ KHỐI VÀ KIẾN TRÚC HỆ THỐNG")

add_heading_2("3.1. Kiến trúc phân tầng 6 lớp độc lập (6-Layer Architecture)")
add_body_p(
    "Hệ thống Boomerang Radar AI được xây dựng theo kiến trúc phân tầng độc lập (Decoupled Layered Architecture), "
    "đảm bảo tính cô lập giữa các chức năng, thuận lợi cho việc kiểm thử đơn vị và dễ dàng bảo trì mở rộng:"
)

layers_data = [
    ("Tầng 1: Thu thập và Nhập liệu (Data Ingestion)", "Tệp tin CSV/Excel lịch sử, Form nhập liệu trên Web, File Upload theo lô và REST API Payload."),
    ("Tầng 2: Tiền xử lý và Đặc trưng hóa (Pipeline)", "Điền khuyết thiếu bằng trung vị (Median Imputation), tạo 4 biến tương tác phi tuyến, phân chia Stratified Split 80/20 và ColumnTransformer chuẩn hóa 14 chiều."),
    ("Tầng 3: Mô hình hóa và Tối ưu hóa (Modeling)", "Huấn luyện và đối chuẩn 4 thuật toán: Logistic Regression, Decision Tree, Random Forest và Gradient Boosting thông qua 5-Fold Stratified Cross-Validation."),
    ("Tầng 4: Lưu trữ Tài nguyên Mô hình (Artifacts)", "Lưu trữ các tệp nhị phân: preprocessor.joblib, gradient_boosting_model.joblib, feature_names.joblib và evaluation_results.json."),
    ("Tầng 5: Dịch vụ và Suy luận (Application Service)", "Máy chủ Flask điều phối các REST API Endpoints, nạp mô hình theo cơ chế Lazy Loading và Engine quy tắc sinh câu phân tích hành vi tự nhiên."),
    ("Tầng 6: Giao diện Người dùng (Presentation Dashboard)", "Giao diện Web Bootstrap 5 với 4 phân hệ tương tác: Tổng quan dữ liệu (Overview), Radar dự đoán thời gian thực (Predictor), Đối chuẩn mô hình (Benchmark) và Xử lý hàng loạt (Batch).")
]

tbl_lay = doc.add_table(rows=1, cols=2)
tbl_lay.rows[0].cells[0].paragraphs[0].text = "Phân tầng kiến trúc"
tbl_lay.rows[0].cells[1].paragraphs[0].text = "Chức năng và Nhiệm vụ kỹ thuật"
tbl_lay.columns[0].width = Inches(2.2)
tbl_lay.columns[1].width = Inches(4.3)

for r in layers_data:
    row = tbl_lay.add_row().cells
    row[0].paragraphs[0].text = r[0]
    row[1].paragraphs[0].text = r[1]

set_table_booktabs(tbl_lay)

add_heading_2("3.2. Thiết kế luồng dữ liệu kép: Huấn luyện Offline và Suy luận Online")
add_body_p(
    "Hệ thống phân định rạch ròi hai chu trình xử lý dữ liệu độc lập:"
)
add_bullet_p("Dữ liệu lịch sử được làm sạch, tính toán 4 biến tương tác, phân chia tập Train/Test 80/20. Bộ biến đổi ColumnTransformer chỉ học tham số thống kê trên tập Train và đóng băng vào file preprocessor.joblib. Mô hình được tối ưu siêu tham số và lưu thành file nhị phân tĩnh.", "Chu trình huấn luyện ngoại tuyến (Offline Training): ")
add_bullet_p("Khi có yêu cầu từ client, dữ liệu khách hàng được ánh xạ 4 biến tương tác, đi qua bộ preprocessor.joblib chỉ bằng hàm transform (không fit lại), mô hình Champion tính xác suất qua predict_proba() và chuyển sang bộ quy tắc sinh khuyến nghị phản hồi trong vòng dưới 50ms.", "Chu trình suy luận trực tuyến (Online Inference): ")

# =============================================================
# CHƯƠNG 4: MÔ TẢ THUẬT TOÁN VÀ NỀN TẢNG TOÁN HỌC
# =============================================================
add_heading_1("4. MÔ TẢ THUẬT TOÁN VÀ NỀN TẢNG TOÁN HỌC")

add_heading_2("4.1. Cơ sở giải tích của 4 đặc trưng tương tác phi tuyến (Interaction Features)")
add_body_p(
    "Nhằm giúp các mô hình học máy nắm bắt được mối quan hệ nhân quả phi tuyến giữa các chiều không gian RFM+, "
    "hệ thống tự động thiết kế 4 biến tương tác giải tích:"
)

add_heading_3("1. Cường độ mua sắm (Purchase Intensity)")
add_formula_block(
    "Purchase_Intensity = Total_Purchases / (Days_Since_Last_Purchase + 1)",
    "Hệ số +1 ở mẫu số đóng vai trò làm mịn (smoothing), ngăn chặn lỗi chia cho 0 khi khách mới mua trong ngày. "
    "Đạo hàm riêng theo số ngày chưa mua luôn âm, phản ánh quy luật giảm đơn điệu theo hàm nghịch đảo."
)

add_heading_3("2. Điểm giá trị vòng đời giản lược (LTV Score)")
add_formula_block(
    "LTV_Score = (Total_Purchases × Avg_Order_Value) / 1.000.000  (triệu VNĐ)",
    "Định lượng tổng quy mô tài chính tích lũy mà khách hàng đã đóng góp cho doanh nghiệp, chuẩn hóa về thang triệu đồng."
)

add_heading_3("3. Mức độ hài lòng theo hàm suy giảm thời gian (Satisfaction Recency)")
add_formula_block(
    "Satisfaction_Recency = [ Satisfaction_Score / (Days_Since_Last_Purchase + 1) ] × 30",
    "Mô hình hóa hiện tượng phai nhạt trải nghiệm theo thời gian: Trọng số hài lòng 5 sao sẽ suy giảm nhanh chóng nếu khoảng cách ngày mua kéo dài trên 90 ngày."
)

add_heading_3("4. Nhận diện nhóm săn voucher giá trị thấp (Voucher Low Value)")
add_formula_block(
    "Voucher_Low_Value = Used_Voucher × I(Avg_Order_Value ≤ 300.000 VNĐ)",
    "Nhận diện chính xác nhóm khách hàng chỉ mua khi có mã giảm giá và chỉ chọn đơn hàng nhỏ, nhóm có rủi ro rời bỏ cao khi hết ngân sách tài trợ voucher."
)

add_heading_2("4.2. Thuật toán Hồi quy Logistic (Logistic Regression)")
add_body_p(
    "Hồi quy Logistic đóng vai trò mô hình chuẩn đối sánh cơ sở (Baseline Model), ánh xạ tổ hợp tuyến tính z = w^T x + b vào miền xác suất (0, 1) thông qua hàm kích hoạt Sigmoid:"
)
add_formula_block(
    "P(y = 1 | x) = σ(z) = 1 / (1 + e^-(w^T x + b))",
    "Hàm mất mát Binary Cross-Entropy kết hợp điều chuẩn L2 (Ridge Penalty): J(w) = - (1/N) ∑ [ y_i ln(p_i) + (1 - y_i) ln(1 - p_i) ] + (1 / 2C) ||w||_2^2"
)

add_heading_2("4.3. Thuật toán Cây quyết định (Decision Tree Classifier)")
add_body_p(
    "Cây quyết định phân chia không gian đặc trưng thành các siêu hình hộp chữ nhật đồng nhất thông qua tiêu chí đo lường độ tinh khiết Entropy và Information Gain hoặc Gini Impurity: I_G = 2 p_0 p_1. Mô hình được khống chế độ sâu tối đa 14 tầng để kiểm soát hiện tượng quá khớp (Overfitting)."
)

add_heading_2("4.4. Thuật toán Rừng ngẫu nhiên (Random Forest Classifier)")
add_body_p(
    "Rừng ngẫu nhiên là thuật toán học kết hợp nhóm (Ensemble Bagging), xây dựng 550 cây quyết định độc lập trên các mẫu Bootstrap ngẫu nhiên có hoàn lại. Phương sai tổng thể được giảm thiểu theo công thức giải tích:"
)
add_formula_block(
    "Var(Rừng) = ρ σ^2 + [ (1 - ρ) / B ] σ^2",
    "Khi số lượng cây B tăng lên 550 cây và áp dụng kỹ thuật chọn ngẫu nhiên tập con đặc trưng (Random Subspace), độ tương quan ρ giảm mạnh, giúp triệt tiêu phương sai và chống quá khớp hiệu quả."
)

add_heading_2("4.5. Thuật toán Gradient Boosting Classifier (Champion Model)")
add_body_p(
    "Gradient Boosting hoạt động theo nguyên lý Boosting tuần tự trên không gian hàm (Functional Gradient Descent). Mỗi cây hồi quy mới h_m(x) được huấn luyện để xấp xỉ phần dư hay gradient âm của hàm mất mát tạo ra bởi các cây trước đó:"
)
add_formula_block(
    "r_{im} = - [ ∂L(y_i, F(x_i)) / ∂F(x_i) ] = y_i - p_{i, m-1}\n"
    "F_m(x) = F_{m-1}(x) + ν × ∑ γ_{jm} I(x ∈ R_{jm})",
    "Trong đó ν = 0.0562 là tốc độ co rút (Learning Rate Shrinkage), giúp mô hình bước đi ổn định trên bề mặt hàm mất mát."
)

# =============================================================
# CHƯƠNG 5: MÔ TẢ DỮ LIỆU VÀ QUY TRÌNH TIỀN XỬ LÝ CHỐNG RÒ RỈ
# =============================================================
add_heading_1("5. MÔ TẢ DỮ LIỆU VÀ QUY TRÌNH TIỀN XỬ LÝ CHỐNG RÒ RỈ")

add_heading_2("5.1. Nguồn dữ liệu và Thống kê mô tả khám phá (EDA)")
add_body_p(
    "Hệ thống sử dụng bộ dữ liệu chuẩn hóa gồm 5.630 hồ sơ giao dịch khách hàng thương mại điện tử thực tế. Tập dữ liệu được phân chia theo tỷ lệ 80% huấn luyện (4.504 mẫu) và 20% kiểm thử độc lập (1.126 mẫu)."
)

eda_data = [
    ("age (Tuổi)", "39.18 tuổi", "9.24", "18 tuổi", "38 tuổi", "70 tuổi"),
    ("total_purchases (Số đơn)", "16.22 đơn", "9.45", "1 đơn", "14 đơn", "60 đơn"),
    ("avg_order_value (AOV)", "1.768.420 đ", "842.150 đ", "150.000 đ", "1.520.000 đ", "4.500.000 đ"),
    ("days_since_last_purchase", "35.41 ngày", "28.62", "1 ngày", "28 ngày", "180 ngày"),
    ("satisfaction_score", "3.07 sao", "1.21", "1 sao", "3 sao", "5 sao"),
    ("purchase_intensity (FE)", "0.82 đơn/ngày", "1.14", "0.008", "0.48", "15.00"),
    ("ltv_score (FE)", "28.65 triệu đ", "24.31", "0.15 triệu đ", "21.28 triệu đ", "270.00 triệu đ"),
    ("satisfaction_recency (FE)", "4.12 điểm", "4.85", "0.16", "2.72", "75.00")
]

tbl_eda = doc.add_table(rows=1, cols=6)
tbl_eda.rows[0].cells[0].paragraphs[0].text = "Đặc trưng"
tbl_eda.rows[0].cells[1].paragraphs[0].text = "Mean"
tbl_eda.rows[0].cells[2].paragraphs[0].text = "Std"
tbl_eda.rows[0].cells[3].paragraphs[0].text = "Min"
tbl_eda.rows[0].cells[4].paragraphs[0].text = "Median"
tbl_eda.rows[0].cells[5].paragraphs[0].text = "Max"

for r in eda_data:
    row = tbl_eda.add_row().cells
    for i in range(6):
        row[i].paragraphs[0].text = r[i]

set_table_booktabs(tbl_eda)

add_heading_2("5.2. Vấn đề mất cân bằng mẫu và giải pháp Stratified Splitting")
add_body_p(
    "Tỷ lệ nhãn trong bộ dữ liệu phản ánh đúng thực tế kinh doanh bán lẻ: 83.0% khách hàng quay lại mua sắm (4.672 khách) và 17.0% khách hàng rời bỏ (958 khách). Để tránh 'Nghịch lý độ chính xác' (Accuracy Paradox), hệ thống áp dụng kỹ thuật lấy mẫu phân tầng Stratified Split nhằm duy trì chính xác tỷ lệ 83% - 17% trên cả hai tập Train và Test, kết hợp điều chỉnh trọng số hàm mất mát class_weight='balanced'."
)

add_heading_2("5.3. Pipeline chuẩn hóa dữ liệu 14 chiều tuân thủ Anti-Data Leakage")
add_body_p(
    "Quy trình tiền xử lý được thiết kế nghiêm ngặt: Phân tách Train/Test trước khi khởi tạo bộ biến đổi. Đối tượng ColumnTransformer áp dụng StandardScaler cho 10 cột số và OneHotEncoder cho 2 cột danh mục duy nhất trên tập Train, đóng băng toàn bộ tham số thống kê trước khi suy luận trên tập Test, đảm bảo mô hình không bị rò rỉ phân phối dữ liệu kiểm thử."
)

# =============================================================
# CHƯƠNG 6: CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG
# =============================================================
add_heading_1("6. CÀI ĐẶT HỆ THỐNG VÀ XÂY DỰNG ỨNG DỤNG")

add_heading_2("6.1. Môi trường công nghệ và Cấu trúc mã nguồn Clean Code")
add_body_p(
    "Hệ thống được phát triển hoàn toàn trên nền tảng Python 3.10 kết hợp các thư viện Scikit-learn 1.7, Pandas 2.3, NumPy 1.26, Flask 3.1 và giao diện Bootstrap 5. Cấu trúc mã nguồn được phân rã thành các module chức năng độc lập:"
)
add_bullet_p("Đảm nhiệm việc nạp dữ liệu, sinh 4 biến tương tác phi tuyến và thực thi quy trình Anti-Data Leakage chuẩn hóa 14 chiều.", "Module src/data_processing.py: ")
add_bullet_p("Thực thi pipeline huấn luyện tự động, tối ưu siêu tham số qua RandomizedSearchCV kết hợp Stratified 5-Fold Cross Validation và xuất các file artifacts nhị phân.", "Module src/train.py: ")
add_bullet_p("Cung cấp bộ máy suy luận thời gian thực cho khách hàng lẻ và xử lý hàng loạt theo tệp CSV, tích hợp logic sinh câu phân tích hành vi tự nhiên.", "Module src/predict.py: ")
add_bullet_p("Máy chủ web Flask cung cấp 4 REST API Endpoints chuẩn JSON và điều phối hiển thị Dashboard 4 phân hệ.", "Module app.py và templates/index.html: ")

add_heading_2("6.2. Cài đặt các dịch vụ REST API")
add_body_p(
    "Hệ thống cung cấp 4 tuyến API phục vụ tích hợp doanh nghiệp:"
)
add_bullet_p("Trả về tỷ lệ quay lại, tỷ lệ rời bỏ, AOV và 15 dòng dữ liệu mẫu.", "GET /api/stats: ")
add_bullet_p("Cung cấp kết quả đánh giá thực nghiệm của 4 mô hình, ma trận nhầm lẫn và danh mục Feature Importances.", "GET /api/models: ")
add_bullet_p("Tiếp nhận JSON 8 chỉ số của một khách hàng, phản hồi xác suất, phân tầng rủi ro và hành động CSKH trong vòng 50ms.", "POST /api/predict: ")
add_bullet_p("Xử lý tệp tin CSV tải lên chứa hàng nghìn khách hàng, gắn nhãn dự đoán và xuất bảng dữ liệu hoàn chỉnh.", "POST /api/predict-batch: ")

# =============================================================
# CHƯƠNG 7: ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM
# =============================================================
add_heading_1("7. ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM")

add_heading_2("7.1. Bảng đối chuẩn hiệu năng thực nghiệm giữa 4 mô hình")
add_body_p(
    "Kết quả kiểm thử nghiêm ngặt trên tập dữ liệu độc lập gồm 1.126 khách hàng (hoàn toàn không tham gia vào quá trình huấn luyện hay tối ưu siêu tham số):"
)

bench_data = [
    ("Logistic Regression", "68.47%", "0.9395", "0.6635", "0.7777", "0.7906", "Mô hình cơ sở (Baseline)"),
    ("Decision Tree", "74.96%", "0.9348", "0.7511", "0.8329", "0.8089", "Khá tốt"),
    ("Random Forest", "91.56%", "0.9367", "0.9637", "0.9500", "0.9575", "Đạt chỉ tiêu"),
    ("Gradient Boosting", "94.23%", "0.9570", "0.9744", "0.9656", "0.9695", "Vô địch (Champion Model)")
]

tbl_b = doc.add_table(rows=1, cols=7)
tbl_b.rows[0].cells[0].paragraphs[0].text = "Thuật toán"
tbl_b.rows[0].cells[1].paragraphs[0].text = "Accuracy"
tbl_b.rows[0].cells[2].paragraphs[0].text = "Precision"
tbl_b.rows[0].cells[3].paragraphs[0].text = "Recall"
tbl_b.rows[0].cells[4].paragraphs[0].text = "F1-Score"
tbl_b.rows[0].cells[5].paragraphs[0].text = "ROC-AUC"
tbl_b.rows[0].cells[6].paragraphs[0].text = "Đánh giá"

tbl_b.columns[0].width = Inches(1.5)
tbl_b.columns[1].width = Inches(0.8)
tbl_b.columns[2].width = Inches(0.8)
tbl_b.columns[3].width = Inches(0.8)
tbl_b.columns[4].width = Inches(0.8)
tbl_b.columns[5].width = Inches(0.8)
tbl_b.columns[6].width = Inches(1.0)

for r in bench_data:
    row = tbl_b.add_row().cells
    for i in range(7):
        row[i].paragraphs[0].text = r[i]

set_table_booktabs(tbl_b)

add_heading_2("7.2. Phân tích Ma trận nhầm lẫn và Tác động kinh tế của sai số")
add_body_p(
    "Ma trận nhầm lẫn của mô hình Gradient Boosting trên 1.126 khách hàng kiểm thử: True Negative (TN) = 149 khách; "
    "False Positive (FP) = 41 khách; False Negative (FN) = 24 khách; True Positive (TP) = 912 khách."
)
add_body_p(
    "Phân tích kinh tế học: Tỷ lệ sai số loại 2 (FN = 24 khách, tương đương 2.13%) cực thấp bảo đảm doanh nghiệp không bị lãng phí ngân sách "
    "khi phát voucher nhầm cho khách hàng trung thành. Đồng thời, mô hình đạt độ nhạy Recall = 97.44% và tỷ lệ phát hiện sớm Churn Specificity = 78.42%, "
    "bảo đảm cứu vãn thành công phần lớn khách hàng tiềm năng."
)

add_heading_2("7.3. Xếp hạng độ quan trọng đặc trưng (Vai trò của Feature Engineering)")
add_body_p(
    "Xếp hạng đóng góp của các đặc trưng vào quyết định của Gradient Boosting: avg_order_value (23.59%), age (23.08%), "
    "ltv_score (20.61%), satisfaction_recency (9.90%), purchase_intensity (6.57%), days_since_last_purchase (3.73%), "
    "satisfaction_score (3.58%) và các biến danh mục còn lại (8.94%)."
)
add_body_p(
    "Nhận xét quan trọng: Ba biến sinh ra từ kỹ thuật đặc trưng tương tác (ltv_score, satisfaction_recency, purchase_intensity) "
    "đóng góp tới 37.08% sức mạnh phân loại của mô hình, chứng minh vai trò then chốt của việc kết hợp kinh nghiệm kinh doanh vào kỹ thuật dữ liệu."
)

# =============================================================
# CHƯƠNG 8: KẾ HOẠCH TRIỂN KHAI, HƯỚNG PHÁT TRIỂN VÀ KẾT LUẬN
# =============================================================
add_heading_1("8. KẾ HOẠCH TRIỂN KHAI, HƯỚNG PHÁT TRIỂN VÀ KẾT LUẬN")

add_heading_2("8.1. Kế hoạch triển khai hành động trong doanh nghiệp (Actionable Plan)")
add_heading_3("a. Ma trận phân công trách nhiệm (RACI Matrix)")

raci_data = [
    ("1. Phê duyệt ngân sách và KPI", "A", "C", "I", "C", "I"),
    ("2. Đóng gói Docker và REST API", "I", "R", "A / R", "I", "I"),
    ("3. Tích hợp Webhook CRM và Zalo/SMS", "I", "C", "R", "A", "C"),
    ("4. Thiết kế chính sách Voucher ưu đãi", "C", "I", "I", "A / R", "C"),
    ("5. Vận hành chăm sóc khách hàng nguy cơ", "I", "I", "I", "C", "A / R"),
    ("6. Kiểm định A/B Testing và Tái huấn luyện", "I", "A / R", "C", "R", "I")
]

tbl_raci = doc.add_table(rows=1, cols=6)
tbl_raci.rows[0].cells[0].paragraphs[0].text = "Hạng mục công việc"
tbl_raci.rows[0].cells[1].paragraphs[0].text = "C-Level"
tbl_raci.rows[0].cells[2].paragraphs[0].text = "Data/AI"
tbl_raci.rows[0].cells[3].paragraphs[0].text = "IT/Dev"
tbl_raci.rows[0].cells[4].paragraphs[0].text = "Marketing"
tbl_raci.rows[0].cells[5].paragraphs[0].text = "CSKH"

for r in raci_data:
    row = tbl_raci.add_row().cells
    for i in range(6):
        row[i].paragraphs[0].text = r[i]

set_table_booktabs(tbl_raci)

add_heading_3("b. Lộ trình triển khai thực tế 12 tuần (Gantt Timeline)")
add_bullet_p("Hoàn tất hạ tầng Cloud (AWS/GCP), đóng gói Docker container, thiết lập CI/CD pipeline tự động hóa kiểm thử mã nguồn.", "Giai đoạn 1 (Tuần 1 - 3): ")
add_bullet_p("Tích hợp kết nối 2 chiều giữa Boomerang Radar AI với hệ thống CRM (HubSpot/Salesforce) và hệ thống gửi tin Zalo ZNS / SMS.", "Giai đoạn 2 (Tuần 4 - 6): ")
add_bullet_p("Thực hiện thử nghiệm A/B Testing trên 20% tệp khách hàng nguy cơ: Nhóm A (Can thiệp theo đề xuất của AI) vs Nhóm B (CSKH truyền thống).", "Giai đoạn 3 (Tuần 7 - 9): ")
add_bullet_p("Triển khai diện rộng 100% tệp khách hàng toàn sàn, bàn giao tài liệu hướng dẫn vận hành và kích hoạt cơ chế tự động tái huấn luyện định kỳ.", "Giai đoạn 4 (Tuần 10 - 12): ")

add_heading_3("c. Dự toán ngân sách và Phân tích hoàn vốn đầu tư (ROI Forecast)")
add_body_p(
    "Dự toán áp dụng trên quy mô doanh nghiệp bán lẻ 50.000 khách hàng: Tổng chi phí đầu tư năm đầu tiên là 260.000.000 VNĐ "
    "(gồm máy chủ Cloud 45 triệu, tích hợp Zalo ZNS 35 triệu, ngân sách voucher kích hoạt 180 triệu). Doanh thu giữ chân thành công "
    "kỳ vọng đạt 1.050.000.000 VNĐ (giữ chân 700 khách hàng tiềm năng nhân LTV 1.5 triệu). Lợi nhuận ròng thặng dư đạt 790.000.000 VNĐ, "
    "mang lại tỷ suất hoàn vốn đầu tư ROI đạt 303.8% (thu hồi vốn hoàn toàn sau 4 tháng)."
)

add_heading_2("8.2. Ứng dụng Trí tuệ Nhân tạo có thể giải thích (Explainable AI với SHAP)")
add_body_p(
    "Tích hợp thuật toán TreeSHAP dựa trên lý thuyết giá trị Shapley trong Lý thuyết trò chơi hợp tác của nhà kinh tế học đoạt giải Nobel Lloyd Shapley (1953). "
    "Cung cấp biểu đồ thác nước (Waterfall Plot) trên Dashboard giúp nhân viên CSKH giải thích minh bạch nguyên nhân chính xác vì sao một khách hàng bị xếp vào nhóm rủi ro cao."
)

add_heading_2("8.3. Mở rộng kiến trúc thuật toán chuyên sâu và MLOps")
add_body_p(
    "Trong các giai đoạn tiếp theo, hệ thống mở rộng sang các thuật toán chuyên biệt cho dữ liệu bảng như LightGBM, CatBoost và Deep Learning TabNet. "
    "Thiết lập hệ thống MLOps giám sát trôi dạt dữ liệu bằng chỉ số ổn định quần thể (Population Stability Index - PSI); tự động kích hoạt tái huấn luyện (Auto-Retraining Pipeline) "
    "khi PSI vượt ngưỡng 0.25."
)

add_heading_2("8.4. Kết luận tổng quan đề tài")
add_body_p(
    "Đề tài Boomerang Radar AI đã hoàn thành xuất sắc toàn bộ mục tiêu đề ra: Xây dựng cơ sở lý thuyết toán học vững chắc; "
    "chứng minh tính đột phá của 4 biến tương tác phi tuyến (đóng góp 37.08% sức mạnh mô hình); thiết lập pipeline Anti-Data Leakage chuẩn hóa; "
    "huấn luyện mô hình Gradient Boosting đạt độ chính xác 94.23%, F1-Score đạt 96.56%; và cung cấp kế hoạch hành động triển khai thực tế mang lại ROI 303.8%."
)

# =============================================================
# TÀI LIỆU THAM KHẢO CHUẨN APA
# =============================================================
doc.add_page_break()
add_heading_1("TÀI LIỆU THAM KHẢO (REFERENCES - CHUẨN APA)")

references = [
    "Arik, S. Ö., & Pfister, T. (2021). TabNet: Attentive interpretable tabular learning. Proceedings of the AAAI Conference on Artificial Intelligence, 35(8), 6679-6687.",
    "Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5-32. https://doi.org/10.1023/A:1010933404324",
    "Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.",
    "Fader, P. S., Hardie, B. G., & Lee, K. L. (2005). 'Counting your customers' the easy way: An alternative to the Pareto/NBD model. Marketing Science, 24(2), 275-284.",
    "Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. Annals of Statistics, 29(5), 1189-1232. https://doi.org/10.1214/aos/1013203451",
    "Hughes, A. M. (2005). Strategic database marketing: The masterplan for starting and managing a profitable, customer-based marketing program (3rd ed.). McGraw-Hill Companies.",
    "Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 4765-4774.",
    "Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
    "Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: Unbiased boosting with categorical features. Advances in Neural Information Processing Systems (NeurIPS 2018), 31, 6638-6648.",
    "Reichheld, F. F., & Sasser, W. E. (1990). Zero defections: Quality comes to services. Harvard Business Review, 68(5), 105-111."
]

for ref in references:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.first_line_indent = Inches(-0.4)
    p_ref.paragraph_format.left_indent = Inches(0.4)
    p_ref.paragraph_format.space_after = Pt(4)
    r = p_ref.add_run(ref)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.font.color.rgb = RGBColor(0, 0, 0)

output_docx = "BAO_CAO_BOOMERANG_RADAR_AI.docx"
doc.save(output_docx)
print(f"XUẤT BẢN FILE DOCX THÀNH CÔNG RỰC RỠ: {output_docx}")
print(f"Kích thước file DOCX: {os.path.getsize(output_docx):,} bytes")
