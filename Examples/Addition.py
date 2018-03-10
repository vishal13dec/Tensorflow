#########################################################################################################################
#                                                                                                                       #
#                       Code In Tensorflow To Add Two Numbers                                                           #
#                                                                                                                       #
#########################################################################################################################


#Importing Tensorflow Library
import tensorflow as tf

# Declaration Of Constant in Tensorflow
a=tf.constant(10,name='a') 
b=tf.constant(23,name='b')

#Operation In Tensorflow
c=tf.add(a,b)

#Creation Of New Session
sess=tf.Session()

# Execution Of Graph Declared Above
print(sess.run(c))

#Closing the session
sess.close()
