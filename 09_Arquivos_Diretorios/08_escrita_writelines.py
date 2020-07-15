lines = ["Hello world.\n", "Welcome to TutorialsTeacher.\n"]
arquivo = open('nome_errado.txt', 'w', encoding="utf8")

arquivo.writelines(lines)
arquivo.close()
