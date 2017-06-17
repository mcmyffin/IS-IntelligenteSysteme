import keras
from os.path import expanduser
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.datasets import mnist
from keras.models import Sequential

from untils import Utils


class CNN():

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

        # Dimension der Daten erweitern um Kanal
        self.x_train = self.x_train.reshape(self.x_train.shape[0], 28, 28, 1)
        self.x_test = self.x_test.reshape(self.x_test.shape[0], 28, 28, 1)

        # Normalisierung der Daten zwischen 0 und 1
        self.x_train = self.x_train.astype('float32')
        self.x_test  = self.x_test.astype('float32')
        self.x_train /= 255
        self.x_test  /= 255

        # Encodieren der Integer-Klassen (0-9) in One-Hot Vektoren
        self.y_train = keras.utils.to_categorical(self.y_train, self.NUM_CLASSES)
        self.y_test  = keras.utils.to_categorical(self.y_test,  self.NUM_CLASSES)



    def softmax_multilayer_adam(self, lernrate=0.01,decay=0.1):
        # Convolutional Neural Network
        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
        self.model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(self.NUM_CLASSES, activation='softmax'))

        #Verwenden von Adam als Optimizer
        self.model.compile(loss='categorical_crossentropy',
        optimizer=keras.optimizers.Adam(lr=0.001, decay=decay),
        metrics=['accuracy'])


    def softmax_multilayer_adadelta(self,lernrate=0.01,decay=0.1):
        # Convolutional Neural Network
        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
        self.model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(self.NUM_CLASSES, activation='softmax'))

        #Verwenden von Adadelta als Optimizer
        self.model.compile(loss='categorical_crossentropy',
        optimizer=keras.optimizers.Adadelta(lr=lernrate,decay=decay,),
        metrics=['accuracy'])



    def fit(self):
        # Training des Modells
        self.history = self.model.fit(self.x_train, self.y_train,
        batch_size=self.BATCH_SIZE,
        epochs=self.EPOCHS,
        validation_data=(self.x_test, self.y_test))


    def showPlot(self,titel_plot):
        score = self.model.evaluate(self.x_test, self.y_test, verbose=0)
        Utils.path = self.USER_HOME
        Utils.create_plot(titel=titel_plot,history=self.history,score=score,save=self.SAVE_IMG)