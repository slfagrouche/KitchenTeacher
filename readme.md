
---

# KitchenTeacher

KitchenTeacher is an interactive web application that predicts dishes from food images, provides YouTube recipe videos, and fetches detailed recipe instructions. This project utilizes Gradio for the user interface and leverages Hugging Face's model inference capabilities for dish prediction.

## Features

- **Dish Prediction**: Upload an image of a food item, and KitchenTeacher will predict the dish using a pre-trained model from Hugging Face.
- **YouTube Recipe Videos**: Once the dish is predicted, KitchenTeacher fetches YouTube recipe videos related to the predicted dish, allowing users to explore different recipes.
- **Detailed Recipe Instructions**: Additionally, KitchenTeacher fetches detailed recipe instructions from TheMealDB API, providing users with step-by-step instructions and ingredient lists.

## Installation

To run KitchenTeacher locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://huggingface.co/spaces/Slfagrouche/KitchenTeacher
   ```

2. Navigate to the project directory:
   ```bash
   cd KitchenTeacher
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python your_gradio_script.py
   ```


## Usage

1. Open the application in your web browser.
2. Upload an image of a food item.
3. KitchenTeacher will predict the dish, fetch YouTube recipe videos, and provide detailed recipe instructions.

## Contributing

Contributions are welcome! If you'd like to contribute to KitchenTeacher, please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This project makes use of [Gradio](https://github.com/gradio-app/gradio) for building the interactive interface.
- Model inference is powered by [Hugging Face](https://huggingface.co/).
- Recipe data is fetched from [TheMealDB](https://www.themealdb.com/api.php).

## Support

For any questions or issues, please [open an issue](https://github.com/your-username/KitchenTeacher/issues) on GitHub.

---

Feel free to customize this README to better fit your project's specifics and add any additional information you think is relevant. Let me know if you need further assistance!