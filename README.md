# Backtesting de Stratégies d’Options sur Actions S&P 500

Ce projet pédagogique a pour objectif de backtester et comparer plusieurs stratégies d’options sur des actions du S&P 500. Il se base sur des données historiques extraites sous forme de fichier CSV contenant les cours de clôture hebdomadaires sur 10 ans pour trois tickers (par exemple AAPL, MSFT et AMZN).

## Objectifs du Projet

- **Acquérir des compétences en finance quantitative :**  
  Comprendre et appliquer le modèle de Black-Scholes pour la valorisation des options, ainsi que les concepts de rendements et volatilité.

- **Implémenter et comparer plusieurs stratégies d’options :**
  - **Covered Call** : Détenir l'action et vendre un call couvert pour générer des revenus.
  - **Long Straddle** : Acheter simultanément un call et un put ATM pour profiter de périodes de forte volatilité.
  - **Bull Call Spread** : Acheter un call à un strike inférieur et vendre un call à un strike supérieur pour parier sur une hausse modérée.

- **Analyser la performance et le risque :**  
  Calculer et visualiser des indicateurs tels que le profit cumulé, le drawdown maximal et le ratio de Sharpe pour chaque stratégie.

## Données

Les données de marché utilisées dans ce projet proviennent 


## Structure du Projet

1. **Lecture et Préparation des Données :**  
   Chargement du fichier CSV, imputation des valeurs manquantes, calcul des rendements hebdomadaires et estimation de la volatilité.

2. **Analyse Exploratoire (EDA) :**  
   Visualisation de l’évolution des cours de clôture, des rendements et de la volatilité pour mieux comprendre le comportement des actifs.

3. **Modèle de Valorisation des Options :**  
   Implémentation du modèle de Black-Scholes pour le pricing d’options (call et put) en fonction du prix du sous-jacent, du strike, du temps jusqu'à l'échéance, du taux sans risque et de la volatilité.

4. **Backtesting des Stratégies :**  
   Définition de fonctions de backtesting pour les stratégies Covered Call, Long Straddle et Bull Call Spread. Chaque fonction simule l'ouverture et la fermeture des positions sur des cycles déterminés (par exemple, mensuels) et calcule le profit pour chaque trade.

5. **Analyse des Performances :**  
   Calcul des indicateurs de performance (profit cumulé, drawdown, ratio de Sharpe) et visualisation de l’évolution des profits pour comparer les stratégies.

## Exécution

Pour exécuter le projet :

1. **Dépendances :**  
   Assurez-vous d'installer les packages Python requis :
   - `pandas`
   - `numpy`
   - `matplotlib`
   - `seaborn`

2. **Fichier de Données :**  
   

