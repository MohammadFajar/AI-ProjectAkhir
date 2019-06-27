from sklearn import tree
from sklearn.metrics import accuracy_score
import pandas as pd

filepath = "pima-indians-diabetes.csv"
sep = ","
delimiter = None

df = pd.read_csv(filepath, sep=sep, delimiter=delimiter)

x = df[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
       "BMI", "DiabetesPedigreeFunction", "Age"]]
y = df["Class"]

clf = tree.DecisionTreeClassifier()
clf.fit(x,y)

y_pred = clf.predict(x)
print("Akurasi", accuracy_score(y, y_pred))
# show columns
print("Hasil prediksi", clf.predict([[3,900,820,70,50,50,0.351,50]]))

