student={"raj":10000,"jay":12000,"shantanu":14000}
for item in student:
    print(item,"-->",student[item])


    for item in student:
        print(item,"--->",student[item])


# problem
jay={"java":78,"python":100,"coputer network":82}
raj={"java":79,"python":100,"computer network":88}
shanthanu={"java":85,"python":89,"computer nework":80}
student_list=[jay,raj,shanthanu]
sum1=0 
for item in student_list:
    for item in student:
        sum1=sum1+student[item]
        print(sum1/len(student))

    


