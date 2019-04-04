import tensorflow as tf
import numpy as np

saved_path = 'add_and_multiple_two'

# Create a tf.keras model.
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=[2], kernel_initializer=tf.keras.initializers.Constant(2)))
model.summary()

# Save the tf.keras model in the SavedModel format.
saved_to_path = tf.contrib.saved_model.save_keras_model(
    model, saved_path)

# Load the saved keras model back.
model_prime = tf.contrib.saved_model.load_keras_model(saved_to_path)
model_prime.summary()

predict_result = model_prime.predict(np.array([[2, 3]]))

print(predict_result)
