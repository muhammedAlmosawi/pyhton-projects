import tensorflow as tf
from tensorflow.keras import datasets, layers, models # it will give an error where the file can't be imported but just ignore it (I did at least) it worked just fine (on my machine)
import matplotlib.pyplot as plt
import os
import random


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = [
    "airplane",
    "autombile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

model_path = "cifar10_cnn_model.h5"
if os.path.exists(model_path):
    model = tf.keras.models.load_model(model_path)
    print("model loaded from disk")
else:
    model = models.Sequential(
        [
            layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation="relu"),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dense(10)
        ]
    )

    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"]
    )
    model.fit(
        train_images,
        train_labels,
        epochs=10,
        validation_data=(test_images, test_labels)
    )

    model.save(model_path)
    print("model saved to disk")

def classify_image(image):
    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)
    predicted_class = tf.argmax(predictions[0]).numpy()
    return class_names[predicted_class]

def show_image_with_prediction(image, true_label):
    predicted_label = classify_image(image)
    plt.figure()
    plt.imshow(image)
    plt.title(f"predicted: {predicted_label}, True: {true_label}")
    plt.axis("off")
    plt.show()

image_index = random.randint(0, 9)

class_pred = classify_image(test_images[image_index])
show_image_with_prediction(test_images[image_index], class_pred)
