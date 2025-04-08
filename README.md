# 📊 Bode Plotter avec SQLite et Tkinter

Ce projet génère des diagrammes de Bode pour des filtres analogiques (Bessel et Butterworth). Il utilise Tkinter pour l'interface graphique, SQLite pour stocker l'historique des filtres, et FPDF pour générer un PDF du diagramme de Bode.

## ⚙️ Fonctionnalités

- **📈 Tracer des diagrammes de Bode** : Saisissez l'ordre du filtre, la fréquence de coupure, et le type de filtre (Bessel ou Butterworth) pour générer le diagramme.
- **💾 Historique des filtres** : Les filtres appliqués sont enregistrés dans une base de données SQLite pour une consultation ultérieure.
- **📄 Générer un PDF** : Le diagramme de Bode peut être enregistré sous forme de fichier PDF avec le graphique.

## 🔧 Prérequis

- Python 3.x
- Les bibliothèques suivantes doivent être installées :
  - `numpy`
  - `matplotlib`
  - `scipy`
  - `sqlite3` (inclus avec Python)
  - `tkinter` (inclus avec Python)
  - `fpdf`

## 🚀 Installation

1. **Clonez le repository** :
   ```bash
   git clone https://github.com/Bourzgui/Bode-Plotter.git
   cd Bode-Plotter
   ```

2. **Installez les dépendances** :
   ```bash
   pip install numpy matplotlib scipy fpdf
   ```

## 🖥️ Utilisation

1. **Lancer l'application** :
   - Exécutez le fichier Python `diagrame.py` :
     ```bash
     python diagrame.py
     ```

2. **Saisie des données** :
   - Entrez l'**ordre du filtre** et la **fréquence de coupure**.
   - Sélectionnez le type de filtre (`Bessel` ou `Butterworth`).
   - Cliquez sur **"Tracer Bode"** pour générer le diagramme.

3. **Afficher l'historique** :
   - Accédez à l'historique des filtres appliqués en cliquant sur **"Afficher l'historique"** dans le menu.

4. **Générer un PDF** :
   - Après avoir tracé le diagramme, vous pouvez générer un **PDF** avec le diagramme en cliquant sur **"Générer PDF"** dans le menu.

## 📝 Explication du Code

### 1. **Création de la base de données SQLite** 💾

Le projet utilise une base de données SQLite pour enregistrer les filtres appliqués, avec les colonnes suivantes :

- **id** : Identifiant unique de chaque enregistrement.
- **filter_order** : L'ordre du filtre.
- **cutoff** : La fréquence de coupure.
- **filter_type** : Le type de filtre (Bessel ou Butterworth).

La fonction `create_database()` crée une table `filter_data` dans le fichier `filters.db`.

### 2. **Sauvegarde des données dans la base de données** 📝

La fonction `save_to_db()` est appelée chaque fois qu'un filtre est appliqué avec succès. Elle enregistre l'ordre, la fréquence de coupure et le type de filtre dans la base de données.

### 3. **Tracé du diagramme de Bode** 📈

La fonction `plot_bode()` :

1. Récupère l'ordre du filtre, la fréquence de coupure et le type de filtre de l'interface utilisateur.
2. Vérifie que les valeurs sont valides (positives).
3. Applique le filtre choisi (Bessel ou Butterworth) avec les paramètres donnés en utilisant les fonctions `bessel()` ou `butter()` de SciPy.
4. Trace le diagramme de Bode en utilisant `matplotlib` avec deux sous-graphiques :
   - **Amplitude (en dB)** : Affiché dans le premier graphique.
   - **Phase (en degrés)** : Affiché dans le deuxième graphique.
5. Enregistre les données du filtre dans la base de données via `save_to_db()` et sauvegarde le diagramme sous forme d'image PNG.

### 4. **Génération du PDF** 📄

La fonction `generate_pdf()` génère un fichier PDF contenant le diagramme de Bode. Elle utilise la bibliothèque `FPDF` pour créer un document, insère l'image du diagramme et l'enregistre sous le nom `bode_plot.pdf`.

### 5. **Affichage de l'historique des filtres** 🕒

La fonction `show_history()` permet d'afficher l'historique des filtres enregistrés dans la base de données sous forme de tableau dans une nouvelle fenêtre Tkinter. Les données affichées comprennent l'ID, l'ordre du filtre, la fréquence de coupure et le type de filtre.

### 6. **Interface graphique avec Tkinter** 🎨

L'application utilise Tkinter pour l'interface graphique. Voici les principales composantes :

- **Entrées utilisateur** : Les utilisateurs saisissent l'ordre du filtre et la fréquence de coupure via des champs de texte.
- **Boutons de commande** : Un bouton pour tracer le diagramme de Bode et un bouton pour générer le PDF.
- **Menu** : Un menu déroulant permettant de générer un PDF ou d'afficher l'historique des filtres.

## 📚 Historique des filtres

Les filtres appliqués sont enregistrés dans une base de données SQLite. Vous pouvez voir l'historique des filtres en cliquant sur **"Afficher l'historique"**.

## 📝 Crédits

- **Développé par** : Bourzgui fatima zahra
- **Technologies utilisées** : Python, Tkinter, SQLite, FPDF, Matplotlib, SciPy
 