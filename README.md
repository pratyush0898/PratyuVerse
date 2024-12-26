# PratyuVerse

PratyuVerse is a cutting-edge AI, meticulously crafted from scratch, designed to offer personalized insights, guidance, and mentorship, all tailored to the unique journey of Pratyush Kumar.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

PratyuVerse is an AI chatbot built using GPT-2, fine-tuned on personal data and web-scraped content related to Pratyush Kumar. The chatbot is designed to provide personalized responses and insights based on the data it has been trained on.

## Features

- **Personalized Chatbot**: Interact with a chatbot that provides responses based on Pratyush Kumar's personal and professional journey.
- **Data Preprocessing**: Scripts to preprocess text data for training.
- **Model Training**: Fine-tune the GPT-2 model on custom data.
- **Web Scraping**: Gather data from specified URLs to enhance the training dataset.

## Installation

To get started with PratyuVerse, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/pratyush0898/pratyuverse.git
   cd pratyuverse
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Data Gathering

To gather data from specified URLs and personal data, run:

```sh
python scripts/gather_data.py
```

### Data Preprocessing

To preprocess the gathered data, run:

```sh
python scripts/preprocess_data.py
```

### Model Training

To fine-tune the GPT-2 model on the preprocessed data, run:

```sh
python scripts/train_model.py
```

### Chatbot Interaction

To interact with the chatbot, run:

```sh
python chatbot.py
```

## Project Structure

```
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
├── chatbot.py
├── data
│   ├── data.json
│   ├── data.txt
│   ├── domains.txt
│   ├── training.txt
├── package.json
├── requirements.txt
└── scripts
    ├── gather_data.py
    ├── preprocess_data.py
    └── train_model.py
```

- **chatbot.py**: Script to run the chatbot.
- **data/**: Directory containing data files.
- **scripts/**: Directory containing scripts for data gathering, preprocessing, and model training.
- **requirements.txt**: List of dependencies required for the project.
- **LICENSE**: License for the project.

## Collaboration

We welcome contributions from the community! If you would like to contribute to PratyuVerse, please follow these steps:

    1. Fork the repository on GitHub.
    2. Create a new branch for your feature or bugfix.
    3. Make your changes and commit them with clear and concise messages.
    4. Push your changes to your forked repository.
    5. Create a pull request to the main repository.

Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the PratyuVerse License (PVL). See the [LICENSE](LICENSE) file for more details.
