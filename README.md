# nearest-record-disclosure-audit

## Français

Mesurer les ressemblances aux données source sans promettre la confidentialité.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m nearest_record_disclosure_audit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Mesure les plus proches enregistrements source et témoin par distance de Gower avec plages numériques figées. Les dimensions absentes sont exclues, et une comparaison entièrement absente reste inconnue.

### Limites

Recherche exacte bornée, identifiants et plages déclarés ; voisinage descriptif, sans preuve de confidentialité différentielle, de réidentification ou d’indépendance des témoins.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Measure source-record similarity without promising privacy.

Synthetic data; no network access or secret required.

```sh
python -m nearest_record_disclosure_audit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Measures nearest source and holdout records with Gower distance under frozen numeric ranges. Missing dimensions are excluded, and an entirely missing comparison stays unknown.

### Limits

Bounded exact search, declared IDs and ranges; descriptive proximity, no differential-privacy, reidentification or holdout-independence proof.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Medir similitud con registros fuente sin prometer privacidad.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m nearest_record_disclosure_audit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Mide registros fuente y de control más cercanos con distancia Gower y rangos fijos. Se excluyen dimensiones ausentes y una comparación totalmente ausente queda desconocida.

### Límites

Búsqueda exacta acotada, IDs y rangos declarados; proximidad descriptiva, sin prueba de privacidad diferencial, reidentificación o independencia del control.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.nist.gov/publications/de-identifying-government-datasets-techniques-and-governance
