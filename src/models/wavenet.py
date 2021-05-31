import tensorflow as tf


class WaveNet(tf.keras.Model):
    def __init__(self):
        super(WaveNet, self).__init__()
        self.