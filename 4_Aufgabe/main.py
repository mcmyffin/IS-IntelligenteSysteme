from convolutional_neural_network import CNN
from feedforward_neural_network import FeedforwardNeuralNetwork

ffnn = FeedforwardNeuralNetwork()
ffnn.SAVE_IMG=False

# 2.1 Einschichtiges Netz mit Softmax
# === 100 ====
ffnn.EPOCHS=100
ffnn.softmax(lernrate=0.01)
ffnn.fit()
ffnn.showPlot("2.1 ["+str(ffnn.EPOCHS)+"] Einschichtiges Netz mit Softmax activation")

# === 200 ====
ffnn.EPOCHS=200
ffnn.softmax(lernrate=0.01)
ffnn.fit()
ffnn.showPlot("2.1 ["+str(ffnn.EPOCHS)+"] Einschichtiges Netz mit Softmax activation")



# 2.2 Mehrschichtiges Netz mit Softmax und Sigmoid
# === 100 ===
ffnn.EPOCHS=100
ffnn.softmax_multilayer(lernrate=0.01,activation='sigmoid')
ffnn.fit()
ffnn.showPlot("2.2 ["+str(ffnn.EPOCHS)+"] Mehrschichtiges Netz mit Softmax und Sigmoid activation")

# === 200 ===
ffnn.EPOCHS=200
ffnn.softmax_multilayer(lernrate=0.01,activation='sigmoid')
ffnn.fit()
ffnn.showPlot("2.2 ["+str(ffnn.EPOCHS)+"] Mehrschichtiges Netz mit Softmax und Sigmoid activation")


# 2.3 Mehrschichtiges Netz mit Softmax und ReLu
# === 100 ===
ffnn.EPOCHS=100
ffnn.softmax_multilayer(lernrate=0.01, activation='relu')
ffnn.fit()
ffnn.showPlot("2.3 ["+str(ffnn.EPOCHS)+"] activation = relu")

# === 200 ===
ffnn.EPOCHS=200
ffnn.softmax_multilayer(lernrate=0.01, activation='relu')
ffnn.fit()
ffnn.showPlot("2.3 ["+str(ffnn.EPOCHS)+"] activation = relu")



# 2.4.1 zusätzlich mit Adam Optimizer
# === 100 ===
ffnn.EPOCHS=100
ffnn.softmax_multilayer_adam(lernrate=0.1,activation="relu",decay=0.0)
ffnn.fit()
ffnn.showPlot("2.4.1 ["+str(ffnn.EPOCHS)+"] activation = relu & Adam decay=0.0")

# 2.4.2 zusätzlich mit Adam Optimizer
# === 100 ===
ffnn.EPOCHS=100
ffnn.softmax_multilayer_adam(lernrate=0.1,activation="relu",decay=0.1)
ffnn.fit()
ffnn.showPlot("2.4.2 ["+str(ffnn.EPOCHS)+"] activation = relu & Adam decay=0.1")



# 2.5 zusätzlich mit Dropout
ffnn.EPOCHS=100
ffnn.softmax_multilayer_adam_dropout_1(lernrate=0.1,activation="relu",decay=0.1)
ffnn.fit()
ffnn.showPlot("2.4.2 ["+str(ffnn.EPOCHS)+"] Dropout=0.1 activation = relu & Adam decay=0.1")

## 2.5.1
ffnn.EPOCHS=100
ffnn.softmax_multilayer_adam_dropout_2(lernrate=0.1,activation="relu",decay=0.1)
ffnn.fit()
ffnn.showPlot("2.4.2 ["+str(ffnn.EPOCHS)+"] Dropout=0.2 activation = relu & Adam decay=0.1")

# 2.5.2
ffnn.EPOCHS=300
ffnn.softmax_multilayer_adam_dropout_2(lernrate=0.1,activation="relu",decay=0.1)
ffnn.fit()
ffnn.showPlot("2.4.2 ["+str(ffnn.EPOCHS)+"] Dropout=0.2 activation = relu & Adam decay=0.1")



# 3. Convolutional neural Network (CNN)
cnn = CNN()
cnn.SAVE_IMG=False

# (1) mit adam optimizer
cnn.EPOCHS=15
cnn.softmax_multilayer_adam()
cnn.fit()
cnn.showPlot("3 ["+str(cnn.EPOCHS)+"] CNN Adam decay=0.1")

# (2) mit adadelta optimizer
cnn.EPOCHS=15
cnn.softmax_multilayer_adadelta()
cnn.fit()
cnn.showPlot("3 ["+str(cnn.EPOCHS)+"] CNN Adadelta decay=0.1")


