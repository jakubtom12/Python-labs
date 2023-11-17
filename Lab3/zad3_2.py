import pandas
from datasets import load_dataset
import matplotlib.pyplot as plt

# a. Pobierz dane
dataset = load_dataset("imodels/credit-card")
df = pandas.DataFrame(dataset['train'])

# b. Usuń duplikaty
df = df.drop_duplicates()

# c. Oblicz korelację pomiędzy wiekiem i limitem kredytu
correlation_age_limit = df['age'].corr(df['limit_bal'])
print(f'Korelacja pomiędzy wiekiem a limitem kredytu: {correlation_age_limit}')

# d. Dodaj kolumnę będącą sumą wszystkich transakcji (bill_amt_X)
df['sum_transactions'] = df.filter(like='bill_amt').sum(axis=1)

# e. Znajdź 10 najstarszych klientów i narysuj tabelkę
oldest_clients = df.nlargest(10, 'age')[['limit_bal', 'age', 'education', 'sum_transactions']]
print(oldest_clients)

# f. Narysuj histogramy
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Histogram limitu kredytu
axes[0].hist(df['limit_bal'], bins=20, color='blue', alpha=0.7)
axes[0].set_title('Histogram limitu kredytu')
axes[0].set_xlabel('Limit kredytu')

# Histogram wieku
axes[1].hist(df['age'], bins=20, color='green', alpha=0.7)
axes[1].set_title('Histogram wieku')
axes[1].set_xlabel('Wiek')

# Zależność limitu kredytu od wieku
axes[2].scatter(df['age'], df['limit_bal'], color='red', alpha=0.5)
axes[2].set_title('Zależność limitu kredytu od wieku')
axes[2].set_xlabel('Wiek')
axes[2].set_ylabel('Limit kredytu')

plt.tight_layout()
plt.show()