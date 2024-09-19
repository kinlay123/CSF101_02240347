with open('fruit_transactions.txt', 'r') as file:
    data = file.readlines()

length = len(data)
print(f'The length of data is {length}')

first_line = data[0]
print(f'The first line is: {first_line}')


all_dict_data = []
for line in data:
    line_dictionary = {}
    cleaned_line = line.replace('\n', '')
    splitted_line = cleaned_line.split(',')

    line_dictionary['name'] = splitted_line[0]
    line_dictionary['action'] = splitted_line[1]
    line_dictionary['quantity'] = int(splitted_line[2])
    line_dictionary['item'] = splitted_line[3]
    line_dictionary['price'] = float(splitted_line[4])

    all_dict_data.append(line_dictionary)


total_sales = sum(item['quantity'] * item['price'] for item in all_dict_data if item['action'] == 'sold')
print(f'Total sales from SOLD transactions: ${total_sales:.2f}')

fruit_counts = {}
for item in all_dict_data:
    fruit = item['item']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

most_popular_fruit = max(fruit_counts, key=fruit_counts.get)
most_popular_fruit_count = fruit_counts[most_popular_fruit]

print(f'The most popular fruit is: {most_popular_fruit} ({most_popular_fruit_count} transactions)')

total_value = sum(item['quantity'] * item['price'] for item in all_dict_data)
total_transactions = len(all_dict_data)
average_transaction_value = total_value / total_transactions
print(f'Average transaction value: ${average_transaction_value:.2f}')

spender_totals = {}
for item in all_dict_data:
    if item['action'] == 'bought':
        if item['name'] in spender_totals:
            spender_totals[item['name']] += item['quantity'] * item['price']
        else:
            spender_totals[item['name']] = item['quantity'] * item['price']

biggest_spender = max(spender_totals, key=spender_totals.get)
biggest_spender_total = spender_totals[biggest_spender]
print(f'Biggest spender: {biggest_spender} with ${biggest_spender_total:.2f}')

summary_content = (
    f"The total sales from SOLD transaction: ${total_sales}\n"
    f"Most Popular Fruit: {most_popular_fruit} ({most_popular_fruit_count} transactions)\n"
    f"Average Transaction_Value: ${average_transaction_value:.2f}\n"
    f"Biggest Spender: {biggest_spender} with ${biggest_spender_total:.2f} spent on 'bought' transactions\n"
)

with open('transaction_summary.txt', 'w') as summary_file:
    summary_file.write(summary_content)

print("Summary report has been written in 'transaction_summary.txt'.")

