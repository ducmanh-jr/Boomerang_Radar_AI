# -*- coding: utf-8 -*-
import os
import sys
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== BIÊN TẬP BÁO CÁO TOÀN DIỆN THEO CHUẨN KHOA HỌC & THỊ GIÁC ===")

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

# Template HTML tuân thủ nghiêm ngặt 4 tiêu chuẩn:
# 1. Tối đa 2 font chữ (Segoe UI cho Tiêu đề, Times New Roman cho Thân bài).
# 2. Tối đa 3 màu chủ đạo: Deep Navy (#0f172a), Tech Blue (#0284c7), Emerald Green (#059669).
# 3. Kích thước 11.5pt, khoảng cách dòng 1.45, tỷ lệ khoảng trắng cân đối, căn lề chuẩn in ấn.
# 4. Ngắt trang thông minh tránh mồ côi tiêu đề.

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Báo cáo toàn diện hệ thống Boomerang Radar AI</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm 15mm 20mm 20mm;
            @top-right {{
                content: "Boomerang Radar AI &bull; Báo cáo Nghiên cứu & Triển khai";
                font-family: 'Segoe UI', sans-serif;
                font-size: 8pt;
                color: #64748b;
            }}
            @bottom-right {{
                content: "Trang " counter(page);
                font-family: 'Segoe UI', sans-serif;
                font-size: 8.5pt;
                color: #334155;
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
            color: #0f172a;
            line-height: 1.45;
            font-size: 11.5pt;
            margin: 0;
            padding: 0;
            background: #ffffff;
        }}
        
        /* 1. TRANG BÌA ĐIỀU HÀNH */
        .cover-page {{
            height: 96vh;
            border: 2.5px solid #0f172a;
            padding: 30px 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            page-break-after: always;
            border-radius: 4px;
        }}
        .institution {{
            font-family: 'Segoe UI', sans-serif;
            font-size: 10.5pt;
            font-weight: 700;
            letter-spacing: 0.8px;
            color: #0f172a;
            text-transform: uppercase;
        }}
        .faculty {{
            font-family: 'Segoe UI', sans-serif;
            font-size: 10pt;
            font-weight: 600;
            color: #475569;
            margin-top: 3px;
            border-bottom: 1.5px solid #cbd5e1;
            padding-bottom: 6px;
            width: 85%;
        }}
        .cover-badge {{
            display: inline-block;
            background: #0284c7;
            color: white;
            font-size: 9.5pt;
            font-weight: 700;
            padding: 4px 16px;
            border-radius: 16px;
            letter-spacing: 1px;
            margin-bottom: 12px;
            font-family: 'Segoe UI', sans-serif;
            text-transform: uppercase;
        }}
        .main-title {{
            font-size: 26pt;
            font-weight: 900;
            color: #0f172a;
            margin: 0 0 8px 0;
            letter-spacing: 0.5px;
            font-family: 'Segoe UI', sans-serif;
        }}
        .sub-title-cover {{
            font-size: 12pt;
            color: #334155;
            line-height: 1.45;
            font-weight: 600;
            font-family: 'Segoe UI', sans-serif;
        }}
        .cover-metrics-box {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            width: 100%;
            margin: 16px 0;
        }}
        .metric-item {{
            border: 1px solid #cbd5e1;
            background: #f8fafc;
            border-radius: 4px;
            padding: 8px 4px;
            text-align: center;
        }}
        .m-val {{
            display: block;
            font-size: 16pt;
            font-weight: 800;
            color: #0284c7;
            font-family: 'Segoe UI', sans-serif;
        }}
        .m-lbl {{
            font-size: 7.5pt;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            font-family: 'Segoe UI', sans-serif;
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
            font-family: 'Segoe UI', sans-serif;
        }}
        .meta-table td {{
            padding: 4px 6px;
            border: none;
            color: #334155;
        }}

        /* 2. TIÊU ĐỀ & CHỈ MỤC THỐNG NHẤT */
        .chapter-title {{
            font-size: 16pt;
            font-weight: 800;
            color: #0f172a;
            border-bottom: 2px solid #0284c7;
            padding-bottom: 5px;
            margin-top: 24px;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-family: 'Segoe UI', sans-serif;
            page-break-after: avoid;
        }}
        .sub-title {{
            font-size: 13pt;
            font-weight: 700;
            color: #0284c7;
            margin-top: 16px;
            margin-bottom: 8px;
            font-family: 'Segoe UI', sans-serif;
            page-break-after: avoid;
        }}
        
        /* 3. THÂN BÀI & ĐOẠN VĂN */
        p {{
            text-align: justify;
            margin: 0 0 9px 0;
            text-indent: 1.25cm;
        }}
        
        ul, ol {{
            margin: 0 0 10px 0;
            padding-left: 28px;
        }}
        li {{
            margin-bottom: 4px;
            text-align: justify;
        }}
        strong {{
            color: #0f172a;
        }}
        
        /* 4. BẢNG BIỂU DỮ LIỆU CHUẨN MỰC */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0 14px 0;
            font-size: 10pt;
            page-break-inside: avoid;
        }}
        table th {{
            background: #0f172a;
            color: #ffffff;
            padding: 7px 8px;
            font-weight: 600;
            border: 1px solid #0f172a;
            font-family: 'Segoe UI', sans-serif;
            text-align: left;
        }}
        table td {{
            padding: 6px 8px;
            border: 1px solid #cbd5e1;
            color: #334155;
            vertical-align: middle;
        }}
        table tr:nth-child(even) {{
            background: #f8fafc;
        }}
        .highlight-row {{
            background: #ecfdf5 !important;
            font-weight: bold;
        }}

        /* 5. KHỐI CÔNG THỨC & CODE */
        .formula-box {{
            background: #f8fafc;
            border-left: 3.5px solid #0284c7;
            border-radius: 3px;
            padding: 8px 12px;
            margin: 8px 0 12px 0;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 10pt;
            color: #0f172a;
            line-height: 1.45;
            page-break-inside: avoid;
        }}
        
        /* 6. CALLOUT HỘP THÔNG ĐIỆP */
        .callout {{
            border-left: 3.5px solid #0284c7;
            background: #f0f9ff;
            padding: 8px 12px;
            border-radius: 0 4px 4px 0;
            margin: 10px 0;
            font-size: 10.5pt;
            font-family: 'Segoe UI', sans-serif;
            page-break-inside: avoid;
        }}
        .callout-success {{
            border-left-color: #059669;
            background: #ecfdf5;
        }}
        .callout-warning {{
            border-left-color: #d97706;
            background: #fffbeb;
        }}
        
        /* 7. SƠ ĐỒ KHỐI TRỰC QUAN */
        .arch-container {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin: 12px 0;
            font-family: 'Segoe UI', sans-serif;
            page-break-inside: avoid;
        }}
        .arch-layer {{
            border: 1.2px solid #cbd5e1;
            border-radius: 4px;
            padding: 6px 10px;
            background: #f8fafc;
        }}
        .arch-layer-header {{
            font-weight: bold;
            color: #0f172a;
            font-size: 10.5pt;
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .arch-layer-badge {{
            background: #0284c7;
            color: white;
            padding: 1px 7px;
            border-radius: 8px;
            font-size: 8pt;
        }}
        .arch-items {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 6px;
        }}
        .arch-card {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 3px;
            padding: 5px 6px;
            font-size: 8.5pt;
            color: #475569;
        }}
        .arch-card-title {{
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 2px;
        }}

        /* 8. MỤC LỤC BÁO CÁO */
        .toc-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 10.5pt;
            font-family: 'Segoe UI', sans-serif;
        }}
        .toc-table td {{
            border: none;
            padding: 5px 2px;
            border-bottom: 1px dotted #cbd5e1;
        }}
        .toc-chap {{
            color: #0f172a;
            font-weight: bold;
        }}
        .toc-sub {{
            padding-left: 18px !important;
            color: #475569;
        }}
        .toc-head th {{
            background: #f1f5f9;
            color: #0f172a;
            border: none;
            border-bottom: 2px solid #0f172a;
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
print(f"  -> File HTML in ấn chuẩn hóa: {html_master_path}")

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
    print(f"XUẤT BẢN PDF TOÀN DIỆN THÀNH CÔNG RỰC RỠ!")
    print(f"  + Tệp tin: {pdf_master_path}")
    print(f"  + Dung lượng: {sz:,} bytes (~{sz/1024/1024:.2f} MB)")
    print(f"  + TỔNG SỐ TRANG IN THỰC TẾ: {len(doc)} TRANG")
    print(f"=======================================================")
else:
    print(f"Lỗi biên dịch PDF: {res.stderr}")
