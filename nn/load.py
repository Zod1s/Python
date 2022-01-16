# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers


# def get_uncompiled_model():
#     inputs = keras.Input(shape=(784,), name='digits')
#     x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
#     x = layers.Dense(64, activation='relu', name='dense_2')(x)
#     outputs = layers.Dense(10, activation='softmax', name='predictions')(x)
#     model = keras.Model(inputs=inputs, outputs=outputs)
#     return model


# def get_compiled_model():
#     model = get_uncompiled_model()
#     model.compile(optimizer=keras.optimizers.RMSprop(learning_rate=1e-3),
#                   loss=keras.losses.SparseCategoricalCrossentropy(),
#                   metrics=[keras.metrics.SparseCategoricalAccuracy()])
#     return model


# untrainedModel = get_compiled_model()
# trainedModel = get_compiled_model()

# _, (x_test, y_test) = keras.datasets.mnist.load_data()

# x_test = x_test.reshape(10000, 784).astype('float32') / 255

# y_test = y_test.astype('float32')

# trainedModel.load_weights('.\\models\\')

# _,acc = untrainedModel.evaluate(x_test, y_test, verbose=2)
# print("Restored model, accuracy: {:5.2f}%".format(100*acc))

# _,acc = trainedModel.evaluate(x_test, y_test, verbose=2)
# print("Restored model, accuracy: {:5.2f}%".format(100*acc))

from tensorflow.keras.datasets import mnist
import tensorflow as tf

new_model = tf.keras.models.load_model('.\\models\\my_model.h5')


_, (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 784).astype('float32') / 255

y_test = y_test.astype('float32')

_, acc = new_model.evaluate(x_test, y_test, verbose=2)
print("Restored model, accuracy: {:5.2f}%".format(100 * acc))
