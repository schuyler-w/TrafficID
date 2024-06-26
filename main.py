import sys
import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

from functions import load_data, get_model, plot_classification_mosaic, plot_misclassified

EPOCHS = 10
NUM_CATEGORIES = 43
TEST_SIZE = 0.3


def main():
    # Check command line arguments
    if len(sys.argv) not in [1, 2, 3, 4]:
        sys.exit("Usage: python main.py [data_directory] [model_name.type] [metric_report.txt]")

    # if no args
    if len(sys.argv) == 1:
        directory = "gtsrb"
    else:
        directory = sys.argv[1]

    # get image arrays and labels for images
    images, labels = load_data(directory)

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)

    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels),
        test_size=TEST_SIZE
    )

    # train model, function defined in functions.py
    model = get_model()

    model.fit(x_train, y_train,
              epochs=EPOCHS)

    model.evaluate(x_test, y_test, verbose=2)

    # Predict the labels
    y_pred = model.predict(x_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true_classes = np.argmax(y_test, axis=1)

    # Generate classification report and confusion matrix
    report = classification_report(y_true_classes, y_pred_classes, target_names=[str(i) for i in range(NUM_CATEGORIES)])
    print(report)

    cm = confusion_matrix(y_true_classes, y_pred_classes)
    print("Truncated Confusion Matrix:")
    print(cm)

    # set print options for numpy so that full confusion matrix is printed to report
    np.set_printoptions(threshold=np.inf, linewidth=200, edgeitems=10)

    # Write the classification report and confusion matrix to classification_report.txt
    if len(sys.argv) == 4:
        with open(sys.argv[3], 'w') as f:
            f.write("Classification Report:\n")
            f.write(report + "\n")
            f.write("Confusion Matrix:\n")
            f.write(str(cm) + "\n")
        print(f"Report written to {sys.argv[3]}")
    else:
        with open("classification_report.txt", 'w') as f:
            f.write("Classification Report:\n")
            f.write(report + "\n")
            f.write("Confusion Matrix:\n")
            f.write(str(cm) + "\n")
        print("Report written to classification_report.txt")

    # Display confusion matrix using ConfusionMatrixDisplay
    fig, ax = plt.subplots(figsize=(15, 15))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[str(i) for i in range(NUM_CATEGORIES)])
    disp.plot(include_values=True, cmap='viridis', ax=ax, xticks_rotation='vertical')
    plt.title('Confusion Matrix')
    plt.savefig('confusion_matrix.png')
    print("Confusion matrix saved to confusion_matrix.png")

    # Display a 5x5 plot of a set of random 25 images in the test set
    plot_classification_mosaic(x_test, y_true_classes, y_pred_classes, 'prediction_results.png')
    print("Prediction results saved to prediction_results.png")

    # plot mosaic of misclassified images
    plot_misclassified(x_test, y_true_classes, y_pred_classes, 'misclassified_results.png')
    print("Misclassified results saved to misclassified_results.png")

    # save model to file specified or default
    if len(sys.argv) == 3:
        model.save(sys.argv[2])
        print(f"Model saved to {sys.argv[2]}.")
    else:
        model.save("model.keras")
        print(f"Model saved to model.keras.")


if __name__ == "__main__":
    main()
