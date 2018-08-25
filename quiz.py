import json 
import time
import os

print("hello")

with open("storequiz.json", 'r') as qa:
	ques_set=qa.read()
	rightans=0
	ques_lst=json.loads(ques_set)

	print(len(ques_lst))
	for i in range(len(ques_lst)) :
		ques_dict=ques_lst[i]
		print("\n {qno} {q}".format(qno=i+1,q=ques_dict['q']))
		print(" a) {a1} \n b) {a2} \n c) {a3} \n d) {a4} ".format( a1=ques_dict['a'], a2=ques_dict['b'], a3=ques_dict['c'], a4=ques_dict['d']))
		guess=input("\n your answer: ")
			
		if ques_dict['ca'] == guess :
			print("correct answer!! \n +10 points")
			rightans+=1
		else:
			print(" wrong answer. \n +0 points")
			print("correct answer is: {}".format(ques_dict['ca']))
			time.sleep(3)
	else:
		print("\n  you have completed the quiz. \n  you have gained {p} points.\n  your percentage= {per}%".format(p=rightans*10, per=(rightans*10)/2))




