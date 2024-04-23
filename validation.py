<<<<<<< HEAD
import sys
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split

from main import load_data

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.5


def main():
    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python validation.py data_directory [output_filename]")  # python validation.py gtsrb results.txt

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    images, labels = np.array(images), np.array(labels)
    labels = tf.keras.utils.to_categorical(labels)

    x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=TEST_SIZE)

    # Prepare models
    models = {
        "Model 1": tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ]),
        "Model 2": tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(32,
                                  activation="relu"),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ]),

        "Model 3": tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3),
                                   activation="relu",
                                   input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64,
                                  activation="relu"),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ]),

        "Model 4": tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(64, (3, 3),
                                   activation="relu",
                                   input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.BatchNormalization(),

            tf.keras.layers.Conv2D(64, (3, 3),
                                   activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128,
                                  activation="relu"),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ]),

        "Model 5": tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(128, (3, 3),
                                   activation="relu",
                                   input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.BatchNormalization(),

            tf.keras.layers.Conv2D(128, (3, 3),
                                   activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(256,
                                  activation="relu"),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ]),

        "Model 6": tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(256, (3, 3),
                                   activation="relu",
                                   input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Conv2D(256, (3, 3),
                                   activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512,
                                  activation="relu"),
            tf.keras.layers.Dropout(0.4),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ]),


        "Model 7": tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(128, (3, 3),
                                   activation="relu",
                                   input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.BatchNormalization(),

            tf.keras.layers.Conv2D(128, (3, 3),
                                   activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(256,
                                  activation="relu"),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ]),

        # Best model found
        "Model 8": tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(128, (3, 3),
                                   activation="relu",
                                   input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.BatchNormalization(),

            tf.keras.layers.Conv2D(128, (3, 3),
                                   activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(256,
                                  activation="relu"),
            tf.keras.layers.Dropout(0.4),
            tf.keras.layers.Dense(NUM_CATEGORIES,
                                  activation="softmax")
        ])
    }

    if len(sys.argv) == 2:
        for name, model in models.items():
            print(f"Evaluating {name}")

            model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
            model.fit(x_train, y_train, epochs=EPOCHS, verbose=0)
            _, accuracy = model.evaluate(x_test, y_test, verbose=2)

            print(f"Accuracy for {name}: {accuracy}")

    else:
        original_stdout = sys.stdout

        with open(sys.argv[2], "w") as file:

            sys.stdout = file

            for name, model in models.items():
                print(f"Evaluating {name}")

                model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
                model.fit(x_train, y_train, epochs=EPOCHS, verbose=0)
                _, accuracy = model.evaluate(x_test, y_test, verbose=2)

                print(f"Accuracy for {name}: {accuracy}")

        sys.stdout = original_stdout


if __name__ == "__main__":
    main()
||||||| 724575be
=======
import sys
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split

from main import load_data

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.5


def main():
    # Check command-line arguments
    if len(sys.argv) not in [2]:
        sys.exit("Usage: python validation.py data_directory")  # python validation.py gtsrb

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    images, labels = np.array(images), np.array(labels)
    labels = tf.keras.utils.to_categorical(labels)

    x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=TEST_SIZE)

    # Prepare models
    models = {
        "Model 1": tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
        ]),
        "Model 2": tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
        ]),
        "Model 3": tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
        ]),
        "Model 4": tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.Dense(512, activation="relu"),
            tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
        ]),

        "Model 5": tf.keras.models.Sequential([

            tf.keras.layers.Conv2D(64, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

            # Flatten layers
            tf.keras.layers.Flatten(),

            # Add A Dense Hidden layer with 512 units and 50% dropout
            tf.keras.layers.Dense(512, activation="relu"),
            tf.keras.layers.Dropout(0.5),

            # Add Dense Output layer with 43 output units
            tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
        ])
    }

    for name, model in models.items():
        print(f"Evaluating {name}")

        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        model.fit(x_train, y_train, epochs=EPOCHS, verbose=0)
        _, accuracy = model.evaluate(x_test, y_test, verbose=2)

        print(f"Accuracy for {name}: {accuracy}")


if __name__ == "__main__":
    main()
>>>>>>> 1841eff779d3554a297c8a3383e820a0dffb2dfb