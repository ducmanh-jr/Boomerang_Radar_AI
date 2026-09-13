# -*- coding: utf-8 -*-
import os
import sys
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== BIÊN TẬP BÁO CÁO TOÀN DIỆN: CHUẨN ĐƠN SẮC QUỐC TẾ (MONOCHROME BOOKTABS) ===")

section_files = [
    "docs_sections/part_01_cover_and_problem.md",
    "docs_sections/part_02_requirements_and_io.md",
    "docs_sections/part_03_architecture.md",
    "docs_sections/part_04_algorithms.md",
    "docs_sections/part_05_dataset.md",
    "docs_sections/part_06_implementation.md",
    "docs_sections/part_07_evaluation.md",
    "docs_sections/part_08_future_and_conclusion.md"
]

all_sections_content = []
for fpath in section_files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
            all_sections_content.append(c)
            print(f"  [OK] Đã nạp module: {fpath} ({len(c):,} ký tự)")
    else:
        print(f"  [ERROR] Không tìm thấy: {fpath}")

# Tạo file Markdown tổng thể
master_md_path = "BAO_CAO_TOAN_DIEN_30_TRANG_BOOMERANG_RADAR_AI.md"
with open(master_md_path, "w", encoding="utf-8") as f:
    f.write("\n\n<div class='page-break'></div>\n\n".join(all_sections_content))
print(f"  -> File Markdown tổng hợp: {master_md_path}")

# Template HTML: 100% Monochrome (Đen - Trắng chuẩn sách xuất bản quốc tế)
html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Báo cáo toàn diện hệ thống Boomerang Radar AI (Chuẩn Đơn sắc Quốc tế)</title>
    <style>
        @page {{
            size: A4;
            margin: 22mm 18mm 22mm 22mm;
            @top-right {{
                content: "Boomerang Radar AI &bull; Báo cáo Kỹ thuật & Khoa học Dữ liệu";
                font-family: 'Times New Roman', serif;
                font-size: 8.5pt;
                color: #333333;
                font-style: italic;
            }}
            @bottom-right {{
                content: "Trang " counter(page);
                font-family: 'Times New Roman', serif;
                font-size: 9pt;
                color: #000000;
                font-weight: bold;
            }}
        }}
        
        * {{
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}
        
        body {{
            font-family: 'Times New Roman', Times, serif;
            color: #000000;
            line-height: 1.45;
            font-size: 11.5pt;
            margin: 0;
            padding: 0;
            background: #ffffff;
        }}
        
        /* 1. TRANG BÌA CHUẨN ĐƠN SẮC QUỐC TẾ */
        .cover-page {{
            height: 96vh;
            border: 2px solid #000000;
            padding: 35px 25px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            page-break-after: always;
            background: #ffffff;
        }}
        .institution {{
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 10.5pt;
            font-weight: 700;
            letter-spacing: 0.8px;
            color: #000000;
            text-transform: uppercase;
        }}
        .faculty {{
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 10pt;
            font-weight: 600;
            color: #222222;
            margin-top: 4px;
            border-bottom: 1px solid #000000;
            padding-bottom: 8px;
            width: 85%;
        }}
        .cover-badge {{
            display: inline-block;
            border: 1.5px solid #000000;
            background: #ffffff;
            color: #000000;
            font-size: 9pt;
            font-weight: 700;
            padding: 4px 18px;
            border-radius: 4px;
            letter-spacing: 1px;
            margin-bottom: 14px;
            font-family: 'Segoe UI', Arial, sans-serif;
            text-transform: uppercase;
        }}
        .main-title {{
            font-size: 27pt;
            font-weight: 900;
            color: #000000;
            margin: 0 0 8px 0;
            letter-spacing: 0.5px;
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        .sub-title-cover {{
            font-size: 12pt;
            color: #111111;
            line-height: 1.45;
            font-weight: 600;
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        .cover-metrics-box {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            width: 100%;
            margin: 18px 0;
        }}
        .metric-item {{
            border: 1.2px solid #000000;
            background: #ffffff;
            padding: 8px 4px;
            text-align: center;
        }}
        .m-val {{
            display: block;
            font-size: 16pt;
            font-weight: 800;
            color: #000000;
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        .m-lbl {{
            font-size: 7.5pt;
            color: #333333;
            font-weight: 700;
            text-transform: uppercase;
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        .cover-meta-info {{
            width: 95%;
            text-align: left;
            margin-top: 15px;
        }}
        .meta-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 10.5pt;
            font-family: 'Times New Roman', serif;
        }}
        .meta-table td {{
            padding: 4px 6px;
            border: none;
            color: #000000;
        }}

        /* 2. TIÊU ĐỀ & CHỈ MỤC THỐNG NHẤT */
        .chapter-title {{
            font-size: 15.5pt;
            font-weight: 800;
            color: #000000;
            border-bottom: 1.5px solid #000000;
            padding-bottom: 4px;
            margin-top: 24px;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-family: 'Segoe UI', Arial, sans-serif;
            page-break-after: avoid;
        }}
        .sub-title {{
            font-size: 12.5pt;
            font-weight: 700;
            color: #000000;
            margin-top: 16px;
            margin-bottom: 6px;
            font-family: 'Segoe UI', Arial, sans-serif;
            page-break-after: avoid;
        }}
        
        /* 3. THÂN BÀI & ĐOẠN VĂN */
        p {{
            text-align: justify;
            margin: 0 0 8px 0;
            text-indent: 1.25cm;
            color: #000000;
        }}
        
        ul, ol {{
            margin: 0 0 10px 0;
            padding-left: 28px;
        }}
        li {{
            margin-bottom: 4px;
            text-align: justify;
            color: #000000;
        }}
        strong {{
            color: #000000;
        }}
        
        /* 4. BẢNG BIỂU CHUẨN BOOKTABS HỌC THUẬT */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0 14px 0;
            font-size: 10pt;
            page-break-inside: avoid;
            border-top: 1.8px solid #000000;
            border-bottom: 1.8px solid #000000;
        }}
        table th {{
            background: #ffffff;
            color: #000000;
            padding: 7px 8px;
            font-weight: 700;
            border-top: none;
            border-bottom: 1.2px solid #000000;
            border-left: none;
            border-right: none;
            font-family: 'Segoe UI', Arial, sans-serif;
            text-align: left;
        }}
        table td {{
            padding: 6px 8px;
            border-top: none;
            border-bottom: 0.5px solid #d4d4d4;
            border-left: none;
            border-right: none;
            color: #000000;
            vertical-align: middle;
        }}
        table tr:last-child td {{
            border-bottom: none;
        }}

        /* 5. KHỐI CÔNG THỨC TOÁN HỌC */
        .formula-box {{
            background: #fafafa;
            border: 1px solid #000000;
            border-radius: 2px;
            padding: 8px 12px;
            margin: 8px 0 12px 0;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 10pt;
            color: #000000;
            line-height: 1.45;
            page-break-inside: avoid;
        }}
        
        /* 6. CALLOUT HỘP THÔNG ĐIỆP ĐƠN SẮC */
        .callout {{
            border-left: 3px solid #000000;
            background: #fafafa;
            padding: 8px 12px;
            margin: 10px 0;
            font-size: 10.5pt;
            color: #000000;
            page-break-inside: avoid;
        }}
        
        /* 7. SƠ ĐỒ KHỐI KIẾN TRÚC ĐƠN SẮC */
        .arch-container {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin: 12px 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            page-break-inside: avoid;
        }}
        .arch-layer {{
            border: 1.2px solid #000000;
            padding: 6px 10px;
            background: #ffffff;
        }}
        .arch-layer-header {{
            font-weight: bold;
            color: #000000;
            font-size: 10.5pt;
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .arch-layer-badge {{
            background: #000000;
            color: #ffffff;
            padding: 1px 7px;
            font-size: 8pt;
            font-weight: bold;
        }}
        .arch-items {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 6px;
        }}
        .arch-card {{
            background: #ffffff;
            border: 0.8px solid #555555;
            padding: 5px 6px;
            font-size: 8.5pt;
            color: #000000;
        }}
        .arch-card-title {{
            font-weight: bold;
            color: #000000;
            margin-bottom: 2px;
        }}

        /* 8. MỤC LỤC BÁO CÁO */
        .toc-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 10.5pt;
            font-family: 'Times New Roman', serif;
            border-top: 1.5px solid #000000;
            border-bottom: 1.5px solid #000000;
        }}
        .toc-table td {{
            border: none;
            padding: 4px 2px;
            border-bottom: 1px dotted #888888;
            color: #000000;
        }}
        .toc-chap {{
            color: #000000;
            font-weight: bold;
        }}
        .toc-sub {{
            padding-left: 18px !important;
            color: #222222;
        }}
        .toc-head th {{
            background: #ffffff;
            color: #000000;
            border: none;
            border-bottom: 1.5px solid #000000;
            padding: 6px 4px;
        }}

        .page-break {{
            page-break-after: always;
        }}
        .avoid-break {{
            page-break-inside: avoid;
        }}
    </style>
</head>
<body>

{''.join(all_sections_content)}

</body>
</html>
"""

html_master_path = "BAO_CAO_TOAN_DIEN_30_TRANG.html"
with open(html_master_path, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"  -> File HTML in ấn chuẩn hóa đơn sắc: {html_master_path}")

# Biên dịch ra file PDF hoàn chỉnh qua Microsoft Edge Headless
pdf_master_path = "BAO_CAO_TOAN_DIEN_BOOMERANG_RADAR_AI_30_TRANG.pdf"
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

print("Đang tiến hành xuất bản file PDF bằng Microsoft Edge Headless...")
cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    f"--print-to-pdf={os.path.abspath(pdf_master_path)}",
    "--no-pdf-header-footer",
    os.path.abspath(html_master_path)
]

res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_master_path) and os.path.getsize(pdf_master_path) > 0:
    sz = os.path.getsize(pdf_master_path)
    import fitz
    doc = fitz.open(pdf_master_path)
    print(f"\n=======================================================")
    print(f"XUẤT BẢN PDF ĐƠN SẮC CHUẨN THẾ GIỚI THÀNH CÔNG RỰC RỠ!")
    print(f"  + Tệp tin: {pdf_master_path}")
    print(f"  + Dung lượng: {sz:,} bytes (~{sz/1024/1024:.2f} MB)")
    print(f"  + TỔNG SỐ TRANG IN THỰC TẾ: {len(doc)} TRANG")
    print(f"=======================================================")
else:
    print(f"Lỗi biên dịch PDF: {res.stderr}")
