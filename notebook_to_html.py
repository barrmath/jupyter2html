from nbconvert import HTMLExporter
from os import listdir
from os import mkdir

# lister les notebooks present à la racine
all_file = listdir()

# créer le dossier html et gerer si le dossier existe deja
try:
    mkdir('html')
except OSError as error:
    # print(error)
    pass

# pour chaque fichier notebook faire la convertion et envoyer la copie html vers le dossier html
for file in all_file:
    if file.endswith('.ipynb'):
        # faire la convertion avec un object
        htmlexport = HTMLExporter()
        htmlexport.exclude_input = True
        htmldata,ressource = htmlexport.from_file(file)
        # write to output file
        outputdata = 'html/'+file
        with open(outputdata, "w") as f:
            f.write(htmldata)
