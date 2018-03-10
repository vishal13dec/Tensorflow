########################################################################################################################
#                                                                                                                     #
#                                        How To use PlaceHolder In Tensorflow                                         #
#                                                                                                                     #
########################################################################################################################

# Statement To Import Tensorflow library In Session
import tensorflow as tf

# To Take the Input To Computational Graph During The Execution Using Placeholder
a=tf.placeholder(dtype=tf.int32,name='Variable')

# Declaration Of Constant 
b=tf.constant(23,name='b')

c=tf.add(a,b)

# Creation Of Tensorflow Session 
sess=tf.Session()

# Initialization Of Variable In Tensorflow Session
sess.run(tf.global_variables_initializer())

# Below command execute the Tensorflow Graph Defined Above To Process The Graph For Variable c. 
# feed_dict is a dictionary which takes the key value pair for all the placeholder needed to calculate the value .

result=sess.run(c,feed_dict={a:23})
print(result)

sess.close()
