from tabnanny import verbose
from sklearn import metrics
from read_csv import doc_preprocess 
from sklearn.model_selection import train_test_split, validation_curve
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Embedding
from tensorflow.keras.layers import SimpleRNN

x, y = doc_preprocess('IMDB_Dataset.csv')
x_train , x_test , y_train , y_test = train_test_split(x, y , test_size=0.2)
x , y = doc_preprocess('sample1.csv')

model = Sequential()
input_len = 878
model.add(Embedding(38180,128, input_length=input_len))
model.add(SimpleRNN(128 , return_sequences=True))
model.add(SimpleRNN(64, return_sequences=True))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(16))
model.add(Dense(1 , activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer = 'adam',metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=512,epochs=5 ,verbose=2,validation_data=(x_test,y_test))
score , accu = model.evaluate(x , y , batch_size =32 , verbose = 2)

y_pre = model.predict(x)
print(y_pre)
print('Test score is : ',score)
print("Test accuracy is : ",accu)