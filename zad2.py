import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothes', 'Food', 'Toys', 'Books']
sales = [150, 200, 300, 100, 50]

plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'])

plt.title('Sales in percent')
plt.show()
