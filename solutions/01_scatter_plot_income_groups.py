plt.scatter(low_income['age'], low_income['hours-per-week'],
            alpha=0.03, s=50, c='b', label='<=50K');
plt.scatter(high_income['age'], high_income['hours-per-week'],
            alpha=0.03, s=50, c='g', label='>50K');
plt.legend()
plt.xlabel('age'); plt.ylabel('hours-per-week');