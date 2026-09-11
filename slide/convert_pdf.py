import os
import subprocess
import sys

def convert_html_to_pdf():
    html_path = os.path.abspath('slide/index.html')
    pdf_path = os.path.abspath('slide/presentation.pdf')
    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        file_url
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        print(f"SUCCESS: Created PDF at {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    else:
        print("Edge default headless failed, trying --headless=new...")
        cmd[1] = "--headless=new"
        subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
            print(f"SUCCESS: Created PDF with --headless=new at {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
        else:
            print(f"ERROR: PDF generation failed. Stderr: {result.stderr}")

if __name__ == "__main__":
    convert_html_to_pdf()
