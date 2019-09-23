# TESTING MODEL DEPLOYMENT
Simple API testing using pythonanywhere and postman. 
<br><br>
## Introduction
In this section, we deploy our already defined Random Forrest model, to data Credit Scoring from [here](https://github.com/khairunisa6/Study-Case-Astra-Creditscore). We are using 3 collumn, which is :
- <i><b>limit</i></b> means the amount of credit 
- <i><b>age</i></b> is the age of to whom credit is owed to. Values usualy ranged from 18 to 70
- <i><b>bill</i></b> is the amount of credit paid in the first month.

We are deployed our model using pythonanywhere.com which you can access using POSTMAN (specificaly, POSTMAN extension from google chrome). You can see our code in pythonanywhere.com by opening <i>Random_Forrest_API.py</i> or click [here](https://github.com/andreasmmadjiah/REST-API-testing/blob/master/Random_Forrest_API.py)

## Using Postman : How To

We are creating <b><i>random forrest</b></i> model, which is basicaly ensemble method for classification or regression by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees (see this wikipedia [link](https://en.wikipedia.org/wiki/Random_forest) for more info). ![](https://github.com/andreasmmadjiah/REST-API-testing/blob/master/image/1_i0o8mjFfCn-uD79-F1Cqkw.png?raw=true)<br> We uploaded our model to <b>pythonanywhere</b> and using <b>postman</b> to test our model. Using <b>pythonanywhere</b>, we creating a server for other users to access our random forrest model. To access it via postman, follow this step :
<br><br>

1. (go to next step if you already have chrome) Download google chrome. It's not mandatory, but because we use <b>postmen</b> extension, it is recomended to use chrome. Access this link to download chrome : [Click Here to download Chrome](https://www.google.com/chrome/) 
2. After you download chrome, install <b>postman</b> extension by [click here to download postman extension](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) 
3. After you install it, just launch the app (via desktop or via chrome) <br>![](https://raw.githubusercontent.com/andreasmmadjiah/REST-API-testing/master/image/postman.png)
4. Sign in using google account (or sign up)
5. After you sign in, click close every pop up window. This should to home in postman <br> ![](https://raw.githubusercontent.com/andreasmmadjiah/Testing-pythonanywhere-/master/image/1.%20close%20create.PNG)
6. Change the option below tab to ``POST`` and input URL in the right of this option to : [andreasmm.pythonanywhere.com/api](andreasmm.pythonanywhere.com/api) <br>![](https://raw.githubusercontent.com/andreasmmadjiah/REST-API-testing/master/image/2.%20new%20tab%20and%20post.PNG) 
7. Change below ``POST`` tab, to ``Body``, then ``raw`` then ``json(application/json)``
    ![](https://raw.githubusercontent.com/andreasmmadjiah/REST-API-testing/master/image/3.%20Change%20below%20tab%20jo%20body.PNG)
8. Now you are ready. If you want to use only one observation for example limit=20000, age=24,bill=34000, then use this example format : <br>
<i><b>{"limit":20000,"age":24,"bill":30000}</i></b> or <i><b>{"limit":[20000],"age":[24],"bill":[30000]}</i></b>. <br> if you want to input more than one observation, for example, you want to add the second limit=34000, age=45, bill= 24000 then you can input : <br>
<i><b>{"limit":[20000,34000],"age":[24,45],"bill":[30000,24000]}</i></b>.<br> Or if you want to use 10 observation you can use : <b><i> {"limit":[12000,120000,21000,31000,145000,12000,120000,21000,31000,145000], "age":[23,32,43,60,20,46,34,55,23,62],"bill":[22000,110000,19000,29000,8000,22000,110000,19000,29000,8000]}</b></i>. <br>You can add as much as you like using this format.<br> Example if one observation    ![](https://raw.githubusercontent.com/andreasmmadjiah/Testing-pythonanywhere-/master/image/Example%20using%20one%20obs.PNG)
    For more than one obs :![](https://raw.githubusercontent.com/andreasmmadjiah/REST-API-testing/master/image/Example%20using%2010%20obs.PNG)
9. After you are ready, just click ``SEND`` beside URL that you already input. (Like above pic)
10. Your result will be showed in the bottom <br> ![](https://raw.githubusercontent.com/andreasmmadjiah/REST-API-testing/master/image/result.PNG)
11. DONE! you can change your data as much as you like 
 
