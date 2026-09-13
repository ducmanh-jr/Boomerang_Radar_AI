# -*- coding: utf-8 -*-
import os
import sys
import glob
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== BẮT ĐẦU QUY TRÌNH BIÊN TẬP VÀ XUẤT BÁO CÁO 30 TRANG ===")

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
            print(f"  + Đã nạp module: {fpath} ({len(c)} ký tự)")
    else:
        print(f"  ! Cảnh báo: Không tìm thấy {fpath}")

# Tạo file Markdown tổng hợp hoàn chỉnh
master_md_path = "BAO_CAO_TOAN_DIEN_30_TRANG_BOOMERANG_RADAR_AI.md"
with open(master_md_path, "w", encoding="utf-8") as f:
    f.write("\n\n<div class='page-break'></div>\n\n".join(all_sections_content))
print(f"Đã tạo file Markdown tổng thể: {master_md_path}")

# Xây dựng file HTML chất lượng in ấn sách/luận văn chuyên nghiệp
html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Báo cáo toàn diện hệ thống Boomerang Radar AI</title>
    <style>
        @page {{
            size: A4;
            margin: 22mm 18mm 22mm 20mm;
            @top-right {{
                content: "Boomerang Radar AI - Báo cáo Chuyên sâu";
                font-size: 8pt;
                color: #64748b;
                font-style: italic;
            }}
            @bottom-right {{
                content: "Trang " counter(page);
                font-size: 8.5pt;
                color: #475569;
                font-weight: bold;
            }}
        }}
        
        * {{
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}
        
        body {{
            font-family: 'Times New Roman', Times, serif, 'Segoe UI', Tahoma, sans-serif;
            color: #1e293b;
            line-height: 1.65;
            font-size: 12.5pt;
            margin: 0;
            padding: 0;
            background: #ffffff;
        }}
        
        /* BÌA LUẬN VĂN */
        .cover-page {{
            height: 98vh;
            border: 3px double #0f172a;
            padding: 35px 25px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            page-break-after: always;
            border-radius: 8px;
        }}
        .institution {{
            font-size: 11pt;
            font-weight: 700;
            letter-spacing: 1px;
            color: #0f172a;
            text-transform: uppercase;
        }}
        .faculty {{
            font-size: 10.5pt;
            font-weight: 600;
            color: #334155;
            margin-top: 4px;
            border-bottom: 1.5px solid #cbd5e1;
            padding-bottom: 8px;
            width: 80%;
        }}
        .cover-badge {{
            display: inline-block;
            background: #0284c7;
            color: white;
            font-size: 10pt;
            font-weight: 700;
            padding: 5px 16px;
            border-radius: 20px;
            letter-spacing: 1.5px;
            margin-bottom: 15px;
            font-family: 'Segoe UI', sans-serif;
        }}
        .main-title {{
            font-size: 28pt;
            font-weight: 900;
            color: #0f172a;
            margin: 0 0 10px 0;
            letter-spacing: 1px;
            font-family: 'Segoe UI', sans-serif;
        }}
        .sub-title-cover {{
            font-size: 13pt;
            color: #334155;
            line-height: 1.5;
            font-weight: 600;
        }}
        .cover-metrics-box {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            width: 100%;
            margin: 25px 0;
        }}
        .metric-item {{
            border: 1px solid #cbd5e1;
            background: #f8fafc;
            border-radius: 6px;
            padding: 10px 5px;
            text-align: center;
        }}
        .m-val {{
            display: block;
            font-size: 17pt;
            font-weight: 800;
            color: #0284c7;
            font-family: 'Segoe UI', sans-serif;
        }}
        .m-lbl {{
            font-size: 8pt;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            font-family: 'Segoe UI', sans-serif;
        }}
        .cover-meta-info {{
            width: 90%;
            text-align: left;
            margin-top: 20px;
        }}
        .meta-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 11pt;
        }}
        .meta-table td {{
            padding: 5px 8px;
            border: none;
            color: #334155;
        }}

        /* TIÊU ĐỀ CHƯƠNG & MỤC */
        .chapter-title {{
            font-size: 18pt;
            font-weight: 800;
            color: #0f172a;
            border-bottom: 2px solid #0284c7;
            padding-bottom: 6px;
            margin-top: 28px;
            margin-bottom: 16px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-family: 'Segoe UI', sans-serif;
        }}
        .sub-title {{
            font-size: 14pt;
            font-weight: 700;
            color: #1e3a8a;
            margin-top: 18px;
            margin-bottom: 8px;
            font-family: 'Segoe UI', sans-serif;
        }}
        
        p {{
            text-align: justify;
            margin: 0 0 10px 0;
            text-indent: 20px;
        }}
        
        ul, ol {{
            margin: 0 0 12px 0;
            padding-left: 30px;
        }}
        li {{
            margin-bottom: 5px;
            text-align: justify;
        }}
        
        /* BẢNG BIỂU */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 14px 0 18px 0;
            font-size: 10.5pt;
        }}
        table th {{
            background: #0f172a;
            color: white;
            padding: 8px 10px;
            font-weight: 600;
            border: 1px solid #0f172a;
            font-family: 'Segoe UI', sans-serif;
        }}
        table td {{
            padding: 7px 10px;
            border: 1px solid #cbd5e1;
            color: #334155;
        }}
        table tr:nth-child(even) {{
            background: #f8fafc;
        }}
        .highlight-row {{
            background: #ecfdf5 !important;
            font-weight: bold;
        }}

        /* HỘP CÔNG THỨC & CODE */
        .formula-box {{
            background: #f1f5f9;
            border-left: 4px solid #0284c7;
            border-radius: 4px;
            padding: 10px 14px;
            margin: 10px 0 14px 0;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 10.5pt;
            color: #0f172a;
            line-height: 1.5;
        }}
        
        /* CALLOUT BOXES */
        .callout {{
            border-left: 4px solid #0284c7;
            background: #f0f9ff;
            padding: 10px 14px;
            border-radius: 0 6px 6px 0;
            margin: 12px 0;
            font-size: 11pt;
            font-family: 'Segoe UI', sans-serif;
        }}
        .callout-success {{
            border-left-color: #10b981;
            background: #ecfdf5;
        }}
        .callout-warning {{
            border-left-color: #f59e0b;
            background: #fffbeb;
        }}
        
        /* SƠ ĐỒ KHỐI KIẾN TRÚC */
        .arch-container {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin: 15px 0;
            font-family: 'Segoe UI', sans-serif;
        }}
        .arch-layer {{
            border: 1.5px solid #cbd5e1;
            border-radius: 6px;
            padding: 8px 12px;
            background: #f8fafc;
        }}
        .arch-layer-header {{
            font-weight: bold;
            color: #0f172a;
            font-size: 11.5pt;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .arch-layer-badge {{
            background: #0284c7;
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 9pt;
        }}
        .arch-items {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
        }}
        .arch-card {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            padding: 6px 8px;
            font-size: 9.5pt;
            color: #475569;
        }}
        .arch-card-title {{
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 2px;
        }}

        /* MỤC LỤC BÁO CÁO */
        .toc-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 11.5pt;
        }}
        .toc-table td {{
            border: none;
            padding: 6px 4px;
            border-bottom: 1px dotted #cbd5e1;
        }}
        .toc-chap {{
            font-family: 'Segoe UI', sans-serif;
            color: #0f172a;
        }}
        .toc-sub {{
            padding-left: 20px !important;
            color: #475569;
        }}
        .toc-head th {{
            background: #f1f5f9;
            color: #0f172a;
            border: none;
            border-bottom: 2px solid #0f172a;
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
print(f"Đã tạo file HTML in ấn: {html_master_path}")

# Biên dịch ra file PDF hoàn chỉnh qua Microsoft Edge Headless
pdf_master_path = "BAO_CAO_TOAN_DIEN_BOOMERANG_RADAR_AI_30_TRANG.pdf"
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

print("Đang khởi chạy tiến trình xuất PDF...")
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
    print(f"BIÊN DỊCH PDF THÀNH CÔNG!")
    print(f"  + Tệp PDF: {pdf_master_path}")
    print(f"  + Kích thước: {sz:,} bytes (~{sz/1024/1024:.2f} MB)")
    
    # Kiểm tra số trang qua fitz
    import fitz
    doc = fitz.open(pdf_master_path)
    print(f"  + TỔNG SỐ TRANG THỰC TẾ: {len(doc)} TRANG")
else:
    print(f"Lỗi biên dịch PDF: {res.stderr}")
