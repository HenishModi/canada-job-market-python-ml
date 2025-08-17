
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("job_postings_canada_large.csv")

# Average salary by province
sns.set_style("whitegrid")
avg_salary = df.groupby("province")["estimated_salary"].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(data=avg_salary.sort_values("estimated_salary", ascending=False), x="estimated_salary", y="province")
plt.title("Average Salary by Province (CAD)")
plt.xlabel("Average Salary (CAD)")
plt.tight_layout()
plt.savefig("avg_salary_by_province.png")

# Monthly trends
monthly = df.groupby("month")["job_id"].count().reset_index(name="job_count").sort_values("month")
plt.figure(figsize=(10,5))
plt.plot(monthly["month"], monthly["job_count"], marker="o")
plt.title("Monthly Job Posting Trends")
plt.xlabel("Month"); plt.ylabel("Job Count"); plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_trends.png")

# ML: Salary prediction
X = df[["province","job_title","month"]]
y = df["estimated_salary"]

categorical = ["province","job_title","month"]
preprocess = ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"), categorical)])
pipe = Pipeline(steps=[("prep", preprocess), ("model", LinearRegression())])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipe.fit(X_train, y_train)
r2 = pipe.score(X_test, y_test)
print(f"R^2 score on test set: {r2:.3f}")

sample = pd.DataFrame({"province":["Ontario","BC"], "job_title":["Data Analyst","Data Scientist"], "month":["2023-08","2023-10"]})
pred = pipe.predict(sample)
for i, val in enumerate(pred):
    print(f"Predicted salary for {sample.iloc[i].to_dict()}: ${val:,.0f}")
