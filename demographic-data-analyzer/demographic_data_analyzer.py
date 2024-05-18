import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    spec = df['race'].unique()
    check1=[]
    check2=[]
    for i in spec:
      i_count = df.loc[df['race']==i,'race'].count()
      check1.append(i)
      check2.append(i_count)
    
    
    race_count = pd.Series(check2,index=check1)

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex']=='Male','age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    Bach_count = df.loc[df['education']=='Bachelors','education'].count()
    total_count = df['education'].count()
    percentage_bachelors =round(Bach_count/total_count*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    total_Adegree = df.loc[((df['education']=='Bachelors') |
                        (df['education']=='Masters') |
                          (df['education']=='Doctorate')),'education'].count()
    
    total_Adegree_Over50 = df.loc[((df['education']=='Bachelors') | (df['education']=='Masters') |
                                   (df['education']=='Doctorate')) & (df['salary']=='>50K'), 'salary'].count()

    total_degree_Over50 = df.loc[(df['education']!='Bachelors') & (df['education']!='Masters') & 
                                  (df['education']!='Doctorate') & (df['salary']=='>50K'),'salary'].count()
    
    total_degree = df.loc[((df['education']!='Bachelors') & (df['education']!='Masters') &
                                 (df['education']!='Doctorate')),'education'].count()
    
    
    higher_education = total_Adegree_Over50
    lower_education = total_degree_Over50
        
    # percentage with salary >50K
    higher_education_rich = round((total_Adegree_Over50/total_Adegree)*100,1)
    lower_education_rich = round((total_degree_Over50/total_degree)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week']==min_work_hours), 'salary'].count()
    rich_min_workers = df.loc[(df['hours-per-week']==min_work_hours) & (df['salary']=='>50K'),'salary'].count()

    rich_percentage = (rich_min_workers/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    country = df['native-country'].unique()
    ppl_percent = []
    country_name = []
    for name in country:
      no_ppl = df.loc[(df['native-country']==name),'native-country'].count()
      no_ppl_over50 = df.loc[(df['native-country']==name) & (df['salary']=='>50K'),'salary'].count()
      percent_country = round((no_ppl_over50/no_ppl)*100,1)
      country_name.append(name)
      ppl_percent.append(percent_country)

    country_list = pd.Series(ppl_percent, index= country_name)
    highest_earning_country = country_list.idxmax()
    highest_earning_country_percentage = country_list.max()

    # Identify the most popular occupation for those who earn >50K in India.
    occ_Over50 = df.loc[(df['native-country']=='India') & (df['salary']=='>50K') , 'occupation']
    top_IN_occupation = occ_Over50.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
