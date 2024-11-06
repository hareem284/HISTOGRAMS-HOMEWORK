
#I CANNOT FIND THE ERROR IN THE CODE I COULD NOT SEND IT ON WHATSAPP AS THEIR WERE SOME INTERNET ISSUES.BUT I THINK I DID SOMETHING WRONG BUT I CAN NOT FIND OUT WHAT.

#importing matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#reading csv file
df=pd.read_csv("Penguins Data (3).csv")
print(df)
plt.hist(data=df,width=6,marker="dashdot",color="purple")
plt.xlabel("studyName")
plt.ylabel("Sample Number")
plt.title("MAKING A HISTOGRAM ON SOMETHING EHICH I FOGOT LOL!!!!!!!!.I DO NOT KNOW WHAT THE NAME SHOULD BE")
plt.show()