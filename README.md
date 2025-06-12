# Cardboard Weight Calculator

This project is a Streamlit application that calculates the weight of cardboard based on user inputs for length, width, height, and GSM (grams per square meter). The application converts measurements to centimeters if they are provided in inches or millimeters and uses specific formulas to compute the cardboard length and weight.

## Project Structure

```
cardboard-weight-app
├── src
│   ├── app.py          # Main entry point for the Streamlit application
│   └── utils.py        # Utility functions for calculations and conversions
├── requirements.txt     # Dependencies required for the project
├── README.md            # Documentation for the project
└── vercel.json          # Configuration for deploying the application on Vercel
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cardboard-weight-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/app.py
```

Open your web browser and navigate to `http://localhost:8501` to access the application.

## Deployment

This application can be deployed on Vercel. Ensure that the `vercel.json` file is correctly configured with the necessary settings for your deployment.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.# Cardboard_weight_Checker
