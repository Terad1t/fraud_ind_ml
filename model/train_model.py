import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("data/transacoes.csv")

X = df.drop(columns=["fraude", "id"])
y = df["fraude"]

categorical_cols = ["pais", "dispositivo"]
numeric_cols = ["valor", "hora", "tentativas", "cartao_presente"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print("classificação report: ")
print(classification_report(y_test, y_pred))

joblib.dump(pipeline, "model/fraud_model.pkl")

print("modelo salvo em model/fraud_model.pkl")