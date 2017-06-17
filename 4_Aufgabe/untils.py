import matplotlib.pyplot as plt

class Utils():

    path = ""

    def create_plot(titel, history, score, save=False):
        # Plot von Accuracy und Loss über das Keras History-Object
        Utils.__plot_training(training_loss=history.history['loss'],
        validation_loss=history.history['val_loss'],
        training_accuracy=history.history['acc'],
        validation_accuracy=history.history['val_acc'],
        titel=titel,
        save=save)

        if(save):
            f = open(str(Utils.path + titel + '.txt'), 'w')
            print('Test loss: '+str(score[0]),file=f)
            print('Test accuracy: '+str(score[1]),file=f)
            f.close()
        else:
            print('Test loss:', score[0])
            print('Test accuracy:', score[1])


    def __plot_training(training_loss, validation_loss, training_accuracy, validation_accuracy,titel,save):
        """ Plot von Accuracy und Loss der Trainings- und Validierungs-Daten
        """
        plt.gcf().clear()
        plt.figure(1)
        plt.gcf().canvas.set_window_title(titel)
        plt.plot(training_accuracy)
        plt.plot(validation_accuracy)
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')

        if save : plt.savefig(Utils.path + titel + '-model_accuracy' + '.png')
        plt.gcf().clear()

        plt.figure(2)
        plt.gcf().canvas.set_window_title(titel)
        plt.plot(training_loss)
        plt.plot(validation_loss)
        plt.title('cross-entropy loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')

        if save: plt.savefig(Utils.path + titel + '-cross-entropy_loss' + '.png')
        else: plt.show()