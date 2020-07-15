with open("pagina.html", "w", encoding="utf-8") as pagina:
    pagina.write(""" 
    <!D0CTYPE html> 
    <html lang="pt-BR"> 
    <head>
    <meta charset="utf-8"> 
    <title>Titulo da Pagina</title>
     </head> 
    <body> 
    Ola! 
    """)
    for l in range(10):
            pagina.write(f"<p>Nº:{l}</p>\n")
    pagina.write(""" 
    </body> 
    </html> """)

filmes = {
	"drama": ["Cidadão Kane", "0 Poderoso Chefão"],
	"comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
	"policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
	"guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}
with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write(""" 
    <!D0CTYPE html> 
    <html lang="pt-BR">
    <head>
    <meta charset="utf-8"> 
    <title>Filmes</title> 
    </head>
    <body>
    """)
    for c, v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        for e in v:
            pagina.write(f"<h2>{e}</h2>\n")
    pagina. write( "</body></html>")