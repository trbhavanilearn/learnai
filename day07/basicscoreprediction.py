import numpy as np
from sklearn.linear_model import LinearRegression

def sqrt(num):
    return num*num


sqrt(7)
sqrt(1024)

#over 1 score 6
#over 2 score 12
#over 3 score 18

def get_score(over):
    return over*6

a=get_score(10)
#print(f"Current Score : {a}")

#over 1 score 8
#over 2 score 14
#over 3 score 20

def get_score_model(over):
    return ((over*6)+2)

a=get_score_model(4)
#print(a)

score=[6,12,18]
score2d=[[6],[12],[18]]

print(np)
#over=np.array([[1],[2],[3],[4],[5],[10],[50],[100]])
X=np.array([[1],[2],[3],[4],[5]])

#scores=np.array([6,12,18,30])
#scores=np.array([8,14,20,32])
y=np.array([8,14,20,26,32])
#scores=np.array([1,4,9,16,25,100,2500,10000])
#print(over.shape)
#print(scores.shape)
#print(LinearRegression)


#fit - receive 2 varialabe
model=LinearRegression().fit(X,y)
guess=int(model.predict([[6]])[0])
print(guess)
