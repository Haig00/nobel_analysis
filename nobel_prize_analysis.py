import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Set Seaborn theme for nice visuals
sns.set_theme(style="whitegrid")

# Load the dataset
df = pd.read_csv("nobel.csv")

# Add helpful columns
df['decade'] = (df['year'] // 10) * 10
df['us_born_winner'] = df['birth_country'] == 'United States of America'
df['is_female'] = df['sex'] == 'Female'

# ------------------------------------------------------------------
# 🎯 Question 1: Most commonly awarded gender and birth country
gender_counts = df['sex'].value_counts()
country_counts = df['birth_country'].value_counts()

top_gender = gender_counts.idxmax()
top_country = country_counts.idxmax()

print("🔹 Q1: Most Common Demographics")
print(f"Most awarded gender: {top_gender}")
print(f"Most awarded birth country: {top_country}\n")

# ------------------------------------------------------------------
# 🎯 Question 2: Decade with highest US-born to total winners ratio
decade_us_ratio = df.groupby('decade')['us_born_winner'].mean().reset_index()
max_us_decade = decade_us_ratio.loc[decade_us_ratio['us_born_winner'].idxmax(), 'decade']

print("🔹 Q2: Highest Ratio of US-Born Winners")
print(f"Decade with highest ratio: {int(max_us_decade)}\n")

# 📊 Plot: Proportion of US-born Winners by Decade
plt.figure(figsize=(10, 5))
sns.lineplot(data=decade_us_ratio, x='decade', y='us_born_winner', marker='o', color='blue')
plt.title('Proportion of US-born Nobel Winners by Decade')
plt.ylabel('Proportion US-born')
plt.xlabel('Decade')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------
# 🎯 Question 3: Decade/Category with highest proportion of female laureates
female_ratio = df.groupby(['decade', 'category'])['is_female'].mean().reset_index()
max_female_row = female_ratio.loc[female_ratio['is_female'].idxmax()]

print("🔹 Q3: Female Laureates Over Time")
print(f"Decade: {int(max_female_row['decade'])}, Category: {max_female_row['category']}, "
      f"Female Ratio: {max_female_row['is_female']:.2f}\n")

# 📊 Plot: Female Laureate Proportions
plt.figure(figsize=(12, 6))
sns.lineplot(data=female_ratio, x='decade', y='is_female', hue='category', marker='o')
plt.title('Proportion of Female Nobel Laureates by Decade and Category')
plt.ylabel('Proportion Female')
plt.xlabel('Decade')
plt.legend(title='Category')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------
# 🎯 Question 4: First Woman to Win a Nobel Prize
first_female = df[df['is_female']].sort_values('year').iloc[0]
print("🔹 Q4: First Woman Nobel Laureate")
print(f"Name: {first_female['full_name']}")
print(f"Category: {first_female['category']}")
print(f"Year: {first_female['year']}\n")

# ------------------------------------------------------------------
# 🎯 Question 5: Multiple-time Winners (Individuals and Organizations)
multi_individuals = df['full_name'].value_counts()
multi_orgs = df['organization_name'].value_counts()

repeat_individuals = multi_individuals[multi_individuals > 1]
repeat_organizations = multi_orgs[multi_orgs > 1]

print("🔹 Q5: Multiple-Time Nobel Winners")
print("🏅 Individuals:")
print(repeat_individuals.to_string())

print("\n🏛️ Organizations:")
print(repeat_organizations.dropna().to_string())