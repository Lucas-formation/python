import pikepdf

file = "nom.pdf"

pdf_file = pikepdf.Pdf.open(file)
urls = []
for page in pdf_file.pages:
    for annots in page.get("/annots"):
        uri=annots.get("/A").get("/URI")
        if uri is not None :
            print("[+] URL Found:", uri)
            urls.append(uri)
print("[*] Total URLs extracted:", len(urls))