import os
import re
import requests


# Liste tous les fichiers Markdown dans le même dossier que le script
markdown_files = [f for f in os.listdir() if f.endswith(".md")]

# Créez le contenu du fichier Readme.md avec des liens vers les fichiers Markdown
readme_content = "# Liste des tutoriaux\n\n"
for markdown_file in markdown_files:
    readme_content += f"- [{markdown_file}]({markdown_file})\n"

# Écrivez le contenu dans le fichier Readme.md
with open("Readme.md", "w") as readme_file:
    readme_file.write(readme_content)

print("Le fichier Readme.md a été créé avec succès.")

# Dossier de destination pour les images
destination_folder = "docs"

# Créez le dossier de destination s'il n'existe pas
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Liste tous les fichiers Markdown dans le même dossier que le script
markdown_files = [f for f in os.listdir() if f.endswith(".md")]

for markdown_file in markdown_files:
    with open(markdown_file, "r") as file:
        markdown_content = file.read()

    # Utilisez une expression régulière pour trouver les liens d'images dans le Markdown
    image_links = re.findall(r'\[!\[.*?\]\((.*?)\)\]\((.*?)\)', markdown_content)

    for image_link in image_links:
        original_url = image_link[1]
        filename = os.path.basename(original_url)
        local_path = os.path.join(destination_folder, filename)

        # Téléchargez l'image depuis l'URL d'origine
        response = requests.get(original_url)
        if response.status_code == 200:
            with open(local_path, 'wb') as image_file:
                image_file.write(response.content)

        # Mettez à jour le lien dans le Markdown
        markdown_content = markdown_content.replace(original_url, local_path)



    # Écrivez le contenu Markdown mis à jour dans le même fichier
    with open(markdown_file, "w") as file:
        file.write(markdown_content)