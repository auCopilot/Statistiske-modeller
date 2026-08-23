from pathlib import Path
from pypdf import PdfWriter


def combine_pdfs(input_dir, output_file):
    input_dir = Path(input_dir)

    # Get PDFs in directory order
    pdf_files = [f for f in input_dir.iterdir() if f.suffix.lower() == ".pdf"]

    writer = PdfWriter()

    for pdf_file in pdf_files:
        print(f"Adding: {pdf_file.name}")
        writer.append(str(pdf_file))

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"Combined {len(pdf_files)} PDFs into {output_file}")


if __name__ == "__main__":
    combine_pdfs(
        input_dir="pdfs",
        output_file="Statistical_Models.pdf",
    )