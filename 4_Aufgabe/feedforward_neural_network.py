import keras
from os.path import expanduser
from keras.layers import Dense, Dropout
from keras.datasets import mnist
from keras.models import Sequential
from untils import Utils


class FeedforwardNeuralNetwork():

    # Der Parameter BATCH_SIZE beläuft sich somit auf die Anzahl der Datensätze pro Mini-Batch, also den
    # Trainingsdaten, die zur Berechnung eines Update-Schrittes im Gradientenverfahren verwendet werden.
    BATCH_SIZE = 128

    # Anzahl der Klassen in den Daten
    NUM_CLASSES = 10

    # Anzahl der Training-Iterationen über die vorhandenen Trainingsdaten
    EPOCHS = 200
    SAVE_IMG=False
    USER_HOME = expanduser("~")+"/"


    def __init__(self, ):
        # Laden des Datensatzes und Aufteilung in 60.000 Trainings- und 10.000 Testdaten
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()

        # Transformation der 28x28 Bilder als Vektoren der Länge 28*28
        self.x_train = self.x_train.reshape(60000, 784)
        self.x_test  = self.x_test.reshape(10000, 784)

        # Normalisierung der Daten zwischen 0 und 1
        self.x_train = self.x_train.astype('float32')
        self.x_test  = self.x_test.astype('float32')
        self.x_train /= 255
        self.x_test  /= 255

        # Encodieren der Integer-Klassen (0-9) in One-Hot Vektoren
        self.y_train = keras.utils.to_categorical(self.y_train, self.NUM_CLASSES)
        self.y_test  = keras.utils.to_categorical(self.y_test,  self.NUM_CLASSES)


    def softmax(self, lernrate=0.01):
        # Softmax-Layer zur Klassifikation
        self.model = Sequential()
        self.model.add(Dense(10, activation='softmax', input_shape=(784,)))

        # Vorbereitung des Modells für das Training
        self.model.compile(loss='categorical_crossentropy',
        optimizer=keras.optimizers.SGD(lr=lernrate),
        metrics=['accuracy'])


    def softmax_multilayer(self, lernrate=0.01, activation='sigmoid'):
        # Modell als Mehrschichtiges Netz zur Klassifikation
        self.model = Sequential()
        self.model.add(Dense(200, activation=activation, input_shape=(784,)))
        self.model.add(Dense(100, activation=activation))
        self.model.add(Dense(60, activation=activation))
        self.model.add(Dense(30, activation=activation))
        self.model.add(Dense(10, activation='softmax'))

        # Vorbereitung des Modells für das Training
        self.model.compile(loss='categorical_crossentropy',
        optimizer=keras.optimizers.SGD(lr=lernrate),
        metrics=['accuracy'])


    def softmax_multilayer_adam(self,lernrate=0.01,activation='sigmoid',decay=0.0):
        # Modell als Mehrschichtiges Netz zur Klassifikation
        self.model = Sequential()
        self.model.add(Dense(200, activation=activation,input_shape=(784,)))
        self.model.add(Dense(100, activation=activation))
        self.model.add(Dense(60, activation=activation))
        self.model.add(Dense(30, activation=activation))
        self.model.add(Dense(10, activation='softmax'))

        #Verwenden von Adam als Optimizer
        self.model.compile(loss='categorical_crossentropy',
        optimizer=keras.optimizers.Adam(lr=0.001, decay=decay),
        metrics=['accuracy'])

    def softmax_multilayer_adam_dropout_1(self, lernrate=0.01, activation='sigmoid',decay=0.0):
        # Modell als Mehrschichtiges Netz zur Klassifikation mit Dropout
        self.model = Sequential()
        self.model.add(Dense(200, activation=activation,input_shape=(784,)))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(100, activation=activation))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(60, activation=activation))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(30, activation=activation))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(10, activation='softmax'))

        #Verwenden von Adam als Optimizer
        self.model.compile(loss='categorical_crossentropy',
        optimizer=keras.optimizers.Adam(lr=0.001, decay=decay),
        metrics=['accuracy'])


    def softmax_multilayer_adam_dropout_2(self, lernrate=0.01, activation='sigmoid',decay=0.0):
        # Modell als Mehrschichtiges Netz zur Klassifikation
        self.model = Sequential()
        self.model.add(Dense(512, activation=activation,input_shape=(784,)))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(512, activation=activation))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(10, activation='softmax'))

        #Verwenden von Adam als Optimizer
        self.model.compile(loss='categorical_crossentropy',
        optimizer=keras.optimizers.Adam(lr=0.001, decay=decay),
        metrics=['accuracy'])

    def fit(self):
        # Training des Modells (fit)
        # self.model.history
        self.history = self.model.fit(self.x_train, self.y_train,
        batch_size=self.BATCH_SIZE,
        epochs=self.EPOCHS,
        validation_data=(self.x_test, self.y_test))

    def showPlot(self,titel_plot):
        score = self.model.evaluate(self.x_test, self.y_test, verbose=0)
        Utils.path = self.USER_HOME
        Utils.create_plot(titel=titel_plot,history=self.history,score=score,save=self.SAVE_IMG)