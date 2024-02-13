
# Deep Reinforcement Learning for Stock Trading from Scratch: Multiple Stock Trading Using Ensemble Strategy

This repository contains a Jupyter Notebook that demonstrates the application of Deep Reinforcement Learning (DRL) algorithms to build an automated stock trading system using an ensemble strategy. It leverages financial data from Yahoo Finance and applies various DRL algorithms to trade stocks within the Dow 30 constituents.

## Getting Started

The notebook is structured to guide you through the process of implementing a DRL-based stock trading strategy, from data download and preprocessing to training DRL agents and backtesting their performance.

### Installation

To run the notebook, you will need to install several Python packages, including pandas, numpy, matplotlib, and specific packages for DRL like stable-baselines and tensorflow. The notebook includes commands to install these dependencies.

### Content Overview

1. **Problem Definition**: Introduces the stock trading problem as a Markov Decision Process and outlines the goal of maximizing portfolio value through automated trading strategies.

2. **Getting Started - Load Python Packages**: Lists the necessary Python packages and provides commands for their installation.

3. **Download Data**: Uses the `YahooDownloader` class to fetch historical stock data from Yahoo Finance.

4. **Preprocess Data**: Covers data preprocessing steps, including feature engineering by adding technical indicators and a turbulence index to the dataset.

5. **Build Environment**: Describes the creation of a custom trading environment using the OpenAI Gym framework, detailing the action and state spaces.

6. **Implement DRL Algorithms**: Demonstrates the application of various DRL algorithms, including A2C, PPO, and DDPG, to train trading agents.

7. **Backtesting Performance**: Evaluates the trained models' performance through backtesting, comparing the DRL strategy against a Dow Jones Industrial Average (DJIA) baseline.

## Usage

You can run the notebook directly on Google Colab using the provided link at the top of this README. It allows you to execute the code and see the results in an interactive environment without any local setup.

## Contributing

Contributions to improve the notebook or extend the strategies are welcome. Please feel free to submit issues or pull requests with your improvements.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
