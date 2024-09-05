var_1 = 10
var_2 = 10.0
var_3 = 400+10j

var_2 = ["10", "kannan"] # [] -> List
typeof = type(var_3)
print(typeof)
print(type(var_2))



#  "" or '' -> str
# multi line string """ 
#  CONTENT
# """
var_2 = "kannan"
print(type(var_2))

para = """Building an end-to-end CI/CD pipeline for Django applications using Jenkins, Docker, Kubernetes, EKS, ArgoCD, GitHub Actions, AWS EC2, and Terraform can be quite a robust setup. In this article, we will guide you through setting up a comprehensive CI/CD pipeline using AWS EC2, AWS EKS, Jenkins, Github actions, Docker, trivy scan, SonarQube, ArgoCD, Kubernetes cluster of your choice, and terraform


extra line added
"""

print(para)


# set -> { }


grp_1 = { "Kannan","yuvaraj", "harish", "kannan", "kannan" }

print(grp_1)

# tuple -> ( )

grp_2 = (10, 11, 12, 10, "kannan", "kannan")

print(grp_2)

# list -> [ ]

grp_3 = [10, 11, 12, 100, 123]
grp_3.sort()
grp_3.reverse()
print(grp_3)

# dictionary -> dict -> { "key " : ["kannan", "harish"]}

grp_4 = {
    "name" : "kannan"
}

print(grp_4)


# boolean -> bool -> True or False

namespace = True

namespace1 = False
print(type(namespace1))
