import pandas
from datasets import load_dataset
import matplotlib.pyplot as plt

# a. Pobierz dane
dataset = load_dataset("imodels/credit-card")
df = pandas.DataFrame(dataset['train'])

# b. Usuń duplikaty
df_no_duplicate = df
df_no_duplicate = df_no_duplicate.drop_duplicates(inplace=True)
#print(df_no_duplicate)

# c. Oblicz korelację pomiędzy wiekiem i limitem kredytu
correlation_age_limit = df['age'].corr(df['limit_bal'])
print(f'Korelacja pomiędzy wiekiem a limitem kredytu: {correlation_age_limit}')

# d. Dodaj kolumnę będącą sumą wszystkich transakcji (bill_amt_X)
df['bill_amt_sum'] = df['bill_amt1'] + df['bill_amt2'] + df['bill_amt3'] + df['bill_amt4'] + df['bill_amt5'] + df['bill_amt6']

# e. Znajdź 10 najstarszych klientów i narysuj tabelkę
df_sorted = df.sort_values(by='age', ascending=False)

education_cols = df_sorted[['education:1', 'education:2', 'education:3', 'education:4', 'education:5', 'education:6']].head(10)
education_dict = {1: "graduate school", 2: "university", 3: "high school", 4: "others", 5: "unknown", 6: "unknown"}

for i, column in enumerate(education_cols, 1):
    if (df_sorted[column] == 1).any():
        df_sorted.loc[df_sorted[column] == 1, 'education'] = education_dict[i]

print((df_sorted[['limit_bal', 'age', 'education', 'bill_amt_sum']].head(10)).to_markdown(index=False))

# f. Narysuj histogramy
fig, axes = plt.subplots(3, 1, figsize=(10, 30))

axes[0].hist(df['limit_bal'], bins=20, color='blue')
axes[0].set_title('Histogram limitu kredytu')
axes[0].set_xlabel('Limit kredytu')

axes[1].hist(df['age'], bins=20, color='green')
axes[1].set_title('Histogram wieku')
axes[1].set_xlabel('Wiek')

axes[2].scatter(df['age'], df['limit_bal'], color='red', alpha=0.5)
axes[2].set_title('Zależność limitu kredytu od wieku')
axes[2].set_xlabel('Wiek')
axes[2].set_ylabel('Limit kredytu')

plt.show()