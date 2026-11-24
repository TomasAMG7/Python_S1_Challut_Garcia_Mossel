# Projet Python S1 ENSAE: Respirer a un prix : qualité de l'air et coût de la vie en Île-de-France

_Challut Gauthier, Garcia Loréna, Mossel Tomas_

## Sujet et objectif

Dans ce projet, nous nous intéressons à l’exploration des liens entre la qualité de l'air, et plus précisément les concentrations des principaux polluants atmosphériques, et le coût de la vie en Île-de-France, entendu dans un double sens : le coût de la vie au sens littéral, mesuré par la mortalité, et le coût de la vie au sens économique, mesuré par les prix de l'immobilier. Ce sujet est d’actualité et constitue un enjeu de santé publique majeur, ce qui motive notre choix. Nous allons tenter d’observer si nous retrouvons des résultats de précédentes études. 

## Données 

Pour étudier la pollution, nous avons du récuperer les données derrière des cartes interactives du site Airparif, puisque on avait besoin des données temporelles au niveau des communes. En inspectant les cartes de Airparifs, on a pu identifier la sources des données et les récupérer pour chaque combinaison de polluant-année-commune. Les données vont 2007 à 2024, pour trois polluants ($\mathrm{NO_2}$, $\mathrm{PM_{2.5}}$, $\mathrm{O_3}$) et englobent toutes les communes de l'île-de-France. En ce qui concerne la mortalité, nous récupérons sur data.gouv le nombre de personnes décédées en France, à la commune (période de 2008 à 2025), ainsi que les populations municipales (1968 à 2023). Enfin, pour les prix de l’immobilier, nous avons pris les données publiques du site datagouv (Île-de-France 2014-2025) et pour les arrondissements le site des notaires de Paris (1995-2025).

## Organisation du dépôt 

Ce projet s’organise de la façon suivante : 

1) un dossier 'code' dans lequel se trouve la fonction de récupération de données 
2) un dossier 'data' dans lequel se trouve l'extraction via API et scrapping de nos données, puis leur stockage
3) un dossier 'axe de réflexion' dans lequel se trouve : 1) notebook sur la mortalité 2) notebook sur la pollution 3) notebook sur les prix immobiliers
4) un notebook final qui constitue une synthèse de notre projet 

Dans le notebook de synthèse, la première partie consiste à la récupération de données ainsi qu’aux premières manipulations nécessaires pour les nettoyer et les rendre exploitables. Nous avons une sous section pour chaque base d’intérêt : pollution, mortalité, prix de l’immobilier. 

Nous nous concentrons ensuite sur les statistiques descriptives, encore une fois pour chaque sous section. Cette partie comprend des statistiques classiques (moyenne, médiane…) mais également de la visualisation à travers des graphiques. 

Enfin, nous utilisons nos bases pour tenter d’observer des liens entre pollution et moralité dans un premier temps, puis pollution et prix de l’immobilier, à travers des régressions à effets fixes, déclinées en fonction de certains éléments (échelle d’analyse, inclusion des années Covid…). 


