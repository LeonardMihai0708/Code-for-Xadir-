i = int(input("Cate orase  sunt?"))
j = 1

Fisier = open('text.txt','w')

for j in range(i):
    cod1 = """<label class="textOverImage" style="background-image:url('img/"""

    link = input("Link:\n")

    cod2 = """');">\n<input type="checkbox">\n<h2>"""

    numele = input("Numele:\n")

    cod3 = """</h2>\n<div>\n"""

    text = input("Text:\n")

    cod4 = "\n</div>\n</label>\n\n\n"

    COD = cod1+link+cod2+numele+cod3+text+cod4

    Fisier.write(COD)
        
    j=j+1

Fisier.close()