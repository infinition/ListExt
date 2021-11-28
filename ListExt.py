#liste les différentes extensions de fichiers contenues dans un dossier et ses sous-dossiers
#affiche les extensions et le nombre de fichiers de chaque type
#classe par ordre decroissant
import os

dossier = input("Enter the directory: ")
#current_dir = os.getcwd()
#current_dir ="

def liste_fichiers(dossier):
    """liste les fichiers d'un dossier et ses sous-dossiers"""
    for root, dirs, files in os.walk(dossier):
        for fichier in files:
            extension = os.path.splitext(fichier)[1]
            if extension not in liste_extensions:
                liste_extensions[extension] = 1
            else:
                liste_extensions[extension] += 1

def affiche_extensions_triees():
    """affiche les extensions et le nombre de fichiers de chaque type"""
    for extension, nombre in sorted(liste_extensions.items(), key=lambda x: x[1], reverse=True):
        print(extension, nombre)


if __name__ == "__main__":
    liste_extensions = {}
    liste_fichiers(dossier)
    affiche_extensions_triees()
    print("\n")
    print("Extension" + " " * 8 + "Nombre")