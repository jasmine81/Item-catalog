import json
f="""[{
		"name":"brunda",
  		"contact":7013011498,
  		"email":"brundasree666@gmail.com",
  		"rollno":81,
  		"is student":true
     },
 	 {
 	 	"name":"bru",
 	 	"contact":123445,
 	 	"email":"16pa1a0581@vishnu.edu.in",
 	 	"rollno":123,
 	 	"is student":true
 	 }]
"""

data=json.loads(f)
print(data)

