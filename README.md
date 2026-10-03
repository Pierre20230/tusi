# Tusi — mises à jour en ligne

Ce dépôt est le serveur de mises à jour des machines Tusi (publié par GitHub Pages à l'adresse `https://pierre20230.github.io/tusi/`).

La page de chaque machine lit `manifest.json` à l'ouverture. Si une version plus récente que la sienne est publiée pour sa machine (`v7` = Tusi v7.4, `v8` = Tusi v8.1), elle affiche « nouvelle version » ; « Installer la version … » télécharge le firmware, le vérifie (firmware ESP32 complet et intact, firmware Tusi, bonne machine), l'envoie à la machine, qui le vérifie à son tour avant de redémarrer.

## Publier une nouvelle version

1. Remplacer `Tusi_v7.bin` et/ou `Tusi_v8_1.bin` par les nouveaux fichiers compilés (même nom). Le firmware doit garder l'adresse `UPDATE_URL` de ce dépôt.
2. `python publier.py "notes de version"` : le script lit la version et la date dans chaque `.bin` et réécrit `manifest.json`.
3. Commit et push. La nouvelle version est visible des machines en 1 à 10 minutes.

Une version n'est proposée qu'aux machines dont le firmware est plus ancien (date de compilation).
