#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

# Sample data
categories = ['Apples', 'Bananas', 'Oranges', 'Grapes']
quantities = [30, 40, 25, 35]

# Bar chart
plt.figure(figsize=(8, 6))
plt.bar(categories, quantities, color='skyblue')
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Quantity of Fruits')
plt.grid(True)
plt.show()

# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(quantities, labels=categories, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Fruits')
plt.show()

