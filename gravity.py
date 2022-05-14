import pandas as pd

df=pd.read_csv('data_cleaned - data_cleaned.csv')

df.drop(['Unnamed: 0'],axis=1,inplace=True)

df['star_radius']=df['star_radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = df['star_radius'].to_list()
mass = df['star_mass'].to_list()
gravity =[]

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si(radius,mass)

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for i in range(0,len(mass)):
        g= (mass[i]*G)/((radius[i])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)

df["Gravity"] = gravity

df.to_csv("star_with_gravity.csv")