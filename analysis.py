import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_renewals.csv")

print("DATA OVERVIEW")
print(df.head())
print("\nRows and columns:", df.shape)
print("\nRenewal rate: {:.1f}%".format(df["renewed"].mean() * 100))
print("\nRenewal rate by plan:")
print((df.groupby("plan_type")["renewed"].mean() * 100).round(1).sort_values(ascending=False))
print("\nAverage months as customer, by renewal status:")
print(df.groupby("renewed")["months_as_customer"].mean().round(1))
print("\nAverage support requests, by renewal status:")
print(df.groupby("renewed")["support_requests"].mean().round(1))

(df.groupby("plan_type")["renewed"].mean() * 100).sort_values().plot(kind="bar")
plt.title("Renewal Rate by Plan Type")
plt.ylabel("Renewed (%)")
plt.xlabel("Plan Type")
plt.tight_layout()
plt.savefig("renewal_rate_by_plan.png", dpi=150)
plt.show()

df.boxplot(column="months_as_customer", by="renewed")
plt.title("Customer Tenure by Renewal Status")
plt.suptitle("")
plt.xlabel("Renewed (0 = No, 1 = Yes)")
plt.ylabel("Months as Customer")
plt.tight_layout()
plt.savefig("tenure_by_renewal.png", dpi=150)
plt.show()
