# Exploring New York weather, 2015–2020

Exploratory analysis of temperature, precipitation and other weather observations from five New York stations. The project includes data cleaning, missing-value analysis, station/year comparisons, statistical plots and a map, supported by the reusable `edapy` helpers.

Use Python 3.12. From the repository root:

```text
python -m venv .venv
```

Activate the environment (`.venv\Scripts\Activate.ps1` in PowerShell), then:

```text
python -m pip install -r requirements.txt
python -m notebook Weather_Project.ipynb
python -m unittest discover -s tests
```

The `data/` directory contains the observations, geographic data, and a GHCND data dictionary. `index.html` is a previously exported notebook, and the PowerPoint contains the original presentation. Retained notebook outputs and the HTML export are historical; the focused maintenance checks do not recompute all figures.

The original study explored patterns relevant to a warming hypothesis. Six years and five stations support local descriptive observations; they do not establish long-term climate attribution. Comparisons also depend on station coverage, missing-value treatment and the chosen period.
