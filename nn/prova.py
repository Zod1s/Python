from tensorflow import keras
from tensorflow.keras import layers
from numpy import argmax

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255

y_train = y_train.astype('float32')
y_test = y_test.astype('float32')

x_val = x_train[-10000:]
y_val = y_train[-10000:]
x_train = x_train[:-10000]
y_train = y_train[:-10000]


def get_uncompiled_model():
    model = keras.Sequential([
        keras.Input(shape=(784,), name='digits'),
        layers.Dense(128, activation='relu', name='dense_1'),
        layers.Dropout(0.5),
        layers.Dense(128, activation='relu', name='dense_2'),
        layers.Dropout(0.5),
        layers.Dense(10, activation='softmax', name='predictions')
    ])

    return model


def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(optimizer=keras.optimizers.RMSprop(learning_rate=1e-3),
                  loss=keras.losses.SparseCategoricalCrossentropy(),
                  metrics=[keras.metrics.SparseCategoricalAccuracy()])
    return model


model = get_compiled_model()

history = model.fit(x_train, y_train,
                    batch_size=64,
                    epochs=25,
                    # We pass some validation for
                    # monitoring validation loss and metrics
                    # at the end of each epoch
                    validation_data=(x_val, y_val))

print('\nhistory dict:', history.history)

# Evaluate the model on the test data using `evaluate`
print('\n# Evaluate on test data')
results = model.evaluate(x_test, y_test, batch_size=128)
print('test loss, test acc:', results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print('\n# Generate predictions for 1 sample')

sample = x_test[:1]
label = y_test[:1]
predictions = model.predict(sample)
pred = argmax(predictions[0])

print('predictions shape:', predictions.shape)
print(f"label: {label[0]}")
print(f"{pred} is the prediction")

print("\n")

model.save('.\\models\\my_model.h5')

print("SAVED")
