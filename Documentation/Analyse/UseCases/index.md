# Cas d'utilisations

```plantuml
left to right direction
actor Utilisateur as user

rectangle "Simulation Sélection Naturelle" {
    ([[#!1_Analyse/UseCases/UC01.md UC01 - SimulerSimulation]]) as UC01
    ([[#!1_Analyse/UseCases/UC02.md UC02 - VisualiserRésultats]]) as UC02

}


user -- UC01
user -- UC02


```

## Liens

* [UC01 SimulerSimulation](UC01.md)
