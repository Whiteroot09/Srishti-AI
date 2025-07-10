import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
num_samples = 10
# Load positive and negative samples
positive_samples = []
negative_samples = []

# Load positive samples
for i in range(num_samples):
    filename = f"audio_data/{i}.npy"
    audio = np.load(filename, allow_pickle=True)
    positive_samples.append(audio)

# Load negative samples
for i in range(num_samples):
    filename = f"background_sound/{i}.npy"
    audio = np.load(filename, allow_pickle=True)
    negative_samples.append(audio)

# Create labels (1 for positive samples, 0 for negative samples)
labels = np.concatenate((np.ones(num_samples), np.zeros(num_samples)))

# Combine positive and negative samples
all_samples = np.concatenate((positive_samples, negative_samples))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(all_samples, labels, test_size=0.2, random_state=42)

# Normalize the audio samples
X_train = X_train / np.max(np.abs(X_train))
X_test = X_test / np.max(np.abs(X_test))

# Reshape the data for compatibility with Conv1D layer
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Build the model architecture
model = Sequential()
model.add(Conv1D(32, 3, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(MaxPooling1D(2))
model.add(Conv1D(64, 3, activation='relu'))
model.add(MaxPooling1D(2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)

# Save the trained model
model.save("wake_word_model.h5")

print("Model training completed.")
