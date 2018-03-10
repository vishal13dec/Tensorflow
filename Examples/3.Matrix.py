############################################################################################################################
#                                                                                                                          #
#                                           Matrix Calculation In TensorFlow                                               #
#                                                                                                                          #
############################################################################################################################

# Importing the Tensorflow Library
import tensorflow as tf

# Creation Of [4,5] matrix with value initialised with zero and dattype to be tf.int32
a=tf.zeros(shape=[4,5],name='a',dtype=tf.int32)

# Creation Of [4,5] matrix with value initialised with 1 and dattype to be tf.int32
b=tf.ones(shape=[4,5] ,name='b',dtype=tf.int32)

#Matrix Operation In Tensorflow
c=tf.add(a,b)

sess=tf.Session()
print(sess.run(c))
sess.close()
