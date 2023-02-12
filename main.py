import pandas as pd

# Read the .csv file into a pandas DataFrame
df = pd.read_csv('RAW_recipes.csv')

print('What dietary restrictions do you have? Choose from the list:' )
print('vegan, vegetarian, keto, low-carb, mediterranean, high-protein, low-protein, low-fat, or healthy')
print('Please enter your selection in all lowercase, seperated by a comma, our code is too efficient to handle extra words.')
restrict = input()

dietary_restrictions = restrict.split(', ')

selected_rows = df.loc[(df['tags'].str.contains(dietary_restrictions[0]) | df['tags'].str.contains(dietary_restrictions[1])) &
                       (df['tags'].str.contains('breakfast') | df['tags'].str.contains('lunch') | df['tags'].str.contains('dinner') | df['tags'].str.contains('snack'))]

if len(selected_rows) >= 20:
    breakfast = selected_rows[selected_rows['tags'].str.contains('breakfast')]
    breakfast = breakfast.sample(n=5)
    print('Breakfast' ,breakfast['name'].values)
    lunch = selected_rows[selected_rows['tags'].str.contains('lunch')]
    lunch = lunch.sample(n=5)
    print('Lunch' ,lunch['name'].values)
    dinner = selected_rows[selected_rows['tags'].str.contains('dinner')]
    dinner = dinner.sample(n=5)
    print('Dinner' ,dinner['name'].values)
    snack = selected_rows[selected_rows['tags'].str.contains('snack')]
    snack = snack.sample(n=5)
    print('Snack' ,snack['name'].values)
 
else:
    print("Not enough recipes to generate a five-day menu.")
