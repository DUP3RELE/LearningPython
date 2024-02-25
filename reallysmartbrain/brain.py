from imageai.Predicition import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(os.path.join(execution_path , "resnet50_weights_tf_dim_ordering_" + "channels_last" + ".h5"))

gay = 1 + 2
print(gay)

from imageai.Predicition import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(os.path.join(execution_path , "resnet50_weights_tf_dim_ordering_" + "channels_last" + ".h5"))

gay = 1 + 2
print('hello there')