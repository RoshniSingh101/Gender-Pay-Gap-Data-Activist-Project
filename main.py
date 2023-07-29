# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
#libary seaborn
import seaborn as sns
#import numpy 
import numpy as np 

# The GWC_utilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable as a pandas DataFrame
# load the dataset
lwd = pd.read_csv("glassdoor.csv")

#-----boxplot for education overall------

print("Today, most people understand that there is a trend in which higher education leads to a higher base pay.")

print("However, can gender be a factor in how much employers pay their employees regardless of their level of education?\n")

input("Press enter to see how base pay differs between different levels of education.\n")

# display rows of dataset
lwd.head()
#print the boxplot
sns.boxplot(data=lwd, x="Education", y="BasePay", showmeans=True, order=["High School", "College", "Masters","PhD"]).set(title="BasePay vs. Education")

print("The overall trend in these boxplots show us that as the degree of education people recieve increases, their base pay will increase.")

print("Click on the 'X' to see how initial salary differs between gender of those who have a PhD.\n")

plt.show()

#-------PhD Data Analysis-------------

print("PhD Five Number Summaries:")

print("Females PhD -- Min: $36,548, Q1: $80,975, Median: $97,742.50, Q3: $113,224, Max: $160,614")

print("Males PhD -- Min: $40,187, Q1: $84,734.50, Median: $101,761.50, Q3: $121,919.75, Max: $179,726")

print("From samples of 106 women and 132 men, on average, there was a $6,199.98 gap in salary between men and women with a PhD according to Glassdoor in 2019. Furthermore, statistical tests such as a two-sample t-interval reveal to us that we can be 90% confident that the true gender pay gap between men and women with a PhD in 2019 falls between $747.10 and $11,631.")

print("\nClick on the 'X' to see how base pay salary differs between men and women with a masters degree.")

#------------boxplot for PhD-------
phdBooleanList = lwd["Education"] == "PhD"
phdData = lwd.loc[phdBooleanList]
# display rows of dataset
phdData.head()
#print the boxplot
sns.boxplot(data=phdData, x="Gender", y="BasePay", showmeans=True).set(title="PhD BasePay vs. Gender")

plt.show()

#-------Masters Data Analysis-----------

print("\nMasters Five Number Summaries:")

print("Females Masters -- Min: $37,780, Q1: $76,194.50, Median: $91,711, Q3: $106,866.50, Max: $155,203")

print("Males Masters -- Min: $45,915, Q1: $84,878, Median: $100,305, Q3: $116,751, Max: $165,229")

print("From samples of 106 women and 150 men, on average, there was a $8,689.81 gap in salary between men and women with a masters degree according to Glassdoor in 2019. Statistical tests such as a two-sample t-interval reveal to us that we can be 90% confident that the true gender pay gap between men and women with a masters degree in 2019 falls between $3,585 and $13,795.")

print("\nClick on the 'X' to see how initial salary differs between gender of those who have a college undergraduate degree.\n")

#--------boxplot for masters-------
mastersBooleanList = lwd["Education"] == "Masters"
mastersData = lwd.loc[mastersBooleanList]
# display rows of dataset
mastersData.head()
#print the boxplot
sns.boxplot(data=mastersData, x="Gender", y="BasePay", showmeans=True,order=["Female", "Male"]).set(title="Masters BasePay vs. Gender")
plt.show()

#-------College Data Analysis-----------

print("\nCollege Five Number Summaries:")

print("Females College -- Min: $38,613, Q1: $70,975.50, Median: $86,241, Q3: $104,397, Max: $127,608")

print("Males College -- Min: $36,642, Q1: $77,939, Median: $98,737, Q3: $119,686, Max: $160,460")

print("From samples of 123 women and 118 men, on average, there was a $11,927.37 gap in salary between men and women with an undergraduate degree according to Glassdoor in 2019. Statistical tests such as a two-sample t-interval reveal to us that we can be 90% confident that the true gender pay gap between men and women with an undergraduate degree in 2019 falls between $6,755.40 and $17,101.")

print("\nClick on the 'X' to see how initial salary differs between gender of those who have a high school degree.\n")

#--------boxplot for college-------
collegeBooleanList = lwd["Education"] == "College"
collegeData = lwd.loc[collegeBooleanList]
# display rows of dataset
collegeData.head()
#print the boxplot
sns.boxplot(data=collegeData, x="Gender", y="BasePay", showmeans=True).set(title="College BasePay vs. Gender")
plt.show()

#-------High School Data Analysis-------

print("\nHigh School Five Number Summaries:")

print("Females High School -- Min: $34,208, Q1: $65,485, Median: $86,844, Q3: $103,513.75, Max: $149,893")

print("Males High School -- Min: $47,036, Q1: $74,829, Median: $89,559, Q3: $106,798, Max: $163,208")

print("From samples of 132 women and 133 men, on average, there was a $5,390.15 gap in salary between men and women with a high school degree according to Glassdoor in 2019. Statistical tests such as a two-sample t-interval reveal to us that we can be 90% confident that the true gender pay gap between men and women with a high school degree in 2019 falls between $398.63 and $10,382.")

print("\nClick on the 'X' to read the conclusion of my data analysis.\n")

#--------boxplot for high school-------
hsBooleanList = lwd["Education"] == "High School"
hsData = lwd.loc[hsBooleanList]
# display rows of dataset
hsData.head()
#print the boxplot
sns.boxplot(data=hsData, x="Gender", y="BasePay", showmeans=True).set(title="High School BasePay vs. Gender")
plt.show()

#------Data Analysis Conclusion-------

print("\nWork-life balance and financial stability are reasons to close the gender pay gap; women across the nation are working tirelessly to support themselves and their families. The US Bureau of Labor Statistics 2022 report shows that full-time female employees earned only 82.9 percent of what full-time male employees earned; women are much more likely than men (61% vs. 37%) to assert that the reason for the gap is that employers treat women differently; 45% of women argue that a significant factor contributing to the pay gap is women making different choices about balancing work and family from men, according to Pew Research Center; however, 40% of men say they are less likely to hold that view; 48% of employed women report feeling pressure to focus on their responsibilities at home, compared with 35% of employed men; 67% of working mothers with children younger than 18 agree, compared to 45% of working dads, while working moms and dads (57% vs. 62%) report feeling pressure to support the family and unmarried working mothers also feel the same way (77%). The statistics and my data analysis promote the need for our society to push forward to close this pay gap. People need to work with local legislatures by calling and emailing them to have their voices heard. Women in the US are struggling, and the government needs to do more to push for equity in treatment, work benefits, and pay. Thank you so much for reading my data analysis, and I hope this opened a new perspective for you to think about!")
