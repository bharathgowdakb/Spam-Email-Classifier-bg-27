import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load Data
df = pd.read_csv("dataset/spam.csv", encoding='latin-1')[['label', 'text']]
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Step 2: Preprocess Text
X = df['text']
y = df['label']

# Step 3: Vectorize Text
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# Step 4: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Step 5: Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 6: Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
