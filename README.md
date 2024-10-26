# SMS Spam Detection

The SMS Spam Detection application is a machine learning tool designed to classify SMS messages as either spam or not spam. It utilizes a pre-trained model to analyze messages and identify potentially harmful content. Developed using the Flask web framework, the application features an interactive interface for real-time message classification.

**Dataset**: [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)


## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, TailwindCSS, JavaScript
- **Containerization**: Docker, Docker Compose
- **Machine Learning**: Scikit-learn, XGBoost, NLTK, Seaborn, Matplotlib, Pandas, NumPy 

## Demo

![Spam Message Demo](./data/images/spam.png)

## Installation

### Prerequisites

Ensure the following are installed on your local machine:
- Python 3.8+
- Docker and Docker Compose (optional for containerized deployment)

### Clone the Repository

```bash
git clone git@github.com:abdullahashfaq-ds/SMS-Spam-Detection.git
cd SMS-Spam-Detection
```

### Method 01: Virtual Environment Setup

```bash
python -m venv venv
# On Windows, use:
venv\Scripts\activate
# On Linux/MacOS, use:
source venv/bin/activate
# To set up the production environment:
pip install -r requirements.txt
# To set up the development environment:
pip install -r requirements.dev.txt
# To run the project:
python app.py
```

### Method 02: Docker Setup

For a containerized environment, build and run the container:

```bash
docker build -t spam-detection .  
docker run -p 5000:5000 spam-detection 
```

Access the application at `http://localhost:5000`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For inquiries or support, please open an issue on GitHub or contact [abdullahashfaq.ds@gmail.com](mailto:abdullahashfaq.ds@gmail.com).
