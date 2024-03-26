
# Deep Reinforcement Learning for Stock Trading from Scratch: Multiple Stock Trading Using Ensemble Strategy

Welcome to the GitHub repository of our AI/ML-Driven Trading Bot project! As an NYU MS CS student deeply fascinated by the intersection of technology and finance, I've embarked on a journey to explore the potential of artificial intelligence and machine learning in the realm of stock trading. This project encapsulates my exploration and the strides I've made in creating an automated trading bot capable of navigating the complexities of the financial markets.

## Project Overview
This trading bot leverages the powerful FinRL library, a deep reinforcement learning library dedicated to automated trading, to predict and execute trades across the Dow 30 stocks. By integrating a variety of technical indicators and employing state-of-the-art machine learning models, this bot aims to make informed trading decisions to maximize returns while minimizing risk.

## Features
1. Comprehensive Data Processing: Utilizes the Yahoo Finance API to fetch historical stock data, ensuring a robust dataset for model training and evaluation.
2. Advanced Feature Engineering: Implements several technical indicators (MACD, RSI, CCI, DX) as features for the ML models, providing them with insightful data points for making predictions.
3. Diverse Model Support: Includes implementations for multiple deep reinforcement learning models, including A2C, PPO, and DDPG, each with custom configurations to cater to different trading strategies.
4. Risk Management: Incorporates a turbulence index to gauge market volatility, allowing the bot to adjust its trading strategy dynamically to mitigate potential losses.
5. Performance Evaluation: Offers comprehensive backtesting tools to evaluate the trading bot's performance against benchmarks, with metrics such as Sharpe Ratio and total account value growth.

## Getting Started
I hope you have python 3.8+ installed on your system.
Please refer to the provided Jupyter notebook for detailed setup and execution instructions. The file will guide you through the installation of necessary libraries.

## How It Works
1. Data Fetching: Collects historical data for the Dow 30 stocks using Yahoo Finance.
2. Feature Engineering: Prepares the data with technical indicators and market volatility measures.
3. Model Training: Trains multiple reinforcement learning models using the processed data.
4. Backtesting: Evaluates the models' performance through backtesting over historical data.
5. Live Trading Simulation: Demonstrates the bot's ability to trade in a simulated environment with real-time market data.

## Discussion and Results
Our trading bot showcased promising results in backtesting, demonstrating the potential of AI/ML in automating and optimizing stock trading strategies. The project also highlights the importance of continuous learning and adaptation in the rapidly evolving financial markets.

## Future Directions
Moving forward, I plan to explore more complex models, including LSTM and Transformer-based architectures, to improve the bot's prediction accuracy and trading performance. Additionally, integrating alternative data sources, such as news and social media sentiment, could offer further insights for making informed trading decisions.

## Contribute
This project is open for collaboration! Whether you're interested in enhancing the trading algorithms, expanding the dataset, or improving the bot's UI, your contributions are welcome.

## Contact
For any queries or suggestions, feel free to reach out to me through GitHub or at adm8315@nyu.edu. Let's make automated trading smarter together!

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
