import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras import Sequential
from keras.layers import Dense, Activation, Dropout
from sklearn.metrics import confusion_matrix, classification_report
from plot_cm import plot_confusion_matrix
import psycopg2
from io import BytesIO

##### Loading saved csv ##############
df = pd.read_pickle("final_audio_data_csv/audio_data.csv")

####### Making our data training-ready
X = df["feature"].values
X = np.concatenate(X, axis=0).reshape(len(X), 40)

y = np.array(df["class_label"].tolist())
y = to_categorical(y)

####### train test split ############
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

##### Training ############

model = Sequential([
    Dense(256, input_shape=X_train[0].shape),
    Activation('relu'),
    Dropout(0.5),
    Dense(256),
    Activation('relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')
])

print(model.summary())

model.compile(
    loss="categorical_crossentropy",
    optimizer='adam',
    metrics=['accuracy']
)

print("Model Score: \n")
history = model.fit(X_train, y_train, epochs=1000)

#### Save the model in the PostgreSQL database #####
# Serialize the model to bytes
model_bytes = model.to_json().encode('utf-8')

# Connect to the PostgreSQL database
conn = psycopg2.connect('postgres://srishti_database_ai_user:JaYaL1A92lAp0ikj0RxGjgKihQ3etVWj@dpg-cic47a95rnuk9qb0sbc0-a.oregon-postgres.render.com/srishti_database_ai')

# Create a cursor
cur = conn.cursor()
cur1 = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS model_table (id serial PRIMARY KEY, model_data bytea)")
# Insert the model data into the database
cur1.execute("INSERT INTO model_table (model_data) VALUES (%s)", (psycopg2.Binary(model_bytes),))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()

score = model.evaluate(X_test, y_test)
print(score)

#### Evaluating our model ###########
print("Model Classification Report: \n")
y_pred = np.argmax(model.predict(X_test), axis=1)
cm = confusion_matrix(np.argmax(y_test, axis=1), y_pred)
print(classification_report(np.argmax(y_test, axis=1), y_pred))
plot_confusion_matrix(cm, classes=["Does not have Wake Word", "Has Wake Word"])
