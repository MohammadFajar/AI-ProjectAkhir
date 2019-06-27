def predik(a,b,c,d,e,f,g,h):
       from sklearn import tree
       from sklearn.metrics import accuracy_score
       import pandas as pd
       from sklearn.model_selection import train_test_split

       filepath = "pima-indians-diabetes.csv"
       sep = ","
       delimiter = None

       df = pd.read_csv(filepath, sep=sep, delimiter=delimiter)

       x = df[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
              "BMI", "DiabetesPedigreeFunction", "Age"]]

       y = df["Class"]

       #clf = SVC(gamma='auto')
       clf = tree.DecisionTreeClassifier()
       #clf = neighbors.KNeighborsClassifier(3, p=2, metric="minkowski")

       X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42, shuffle=True)

       clf.fit(X_train, y_train)

       # y_pred = clf.predict(X_test)
       # print("Akurasi", accuracy_score(y_test, y_pred))
       # # show columns
       # print("Hasil prediksi", clf.predict([[8,155,85,33,0,34,0.445,47]]))
       hasil=clf.predict([[a,b,c,d,e,f,g,h]])
       return hasil