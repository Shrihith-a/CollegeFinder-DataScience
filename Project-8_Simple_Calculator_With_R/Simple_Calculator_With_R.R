
# Giving condition
Addition <- function(a,b) {
  return(a + b)
}
Subtraction <- function(a,b){
  return(a - b)
}
Multiplication <- function(a,b){
  return(a * b)
}
Division <- function(a,b) {
  return(a/b)
}
Exponentiation <- function(a,b){
  return(a^b)
}

# take input from the user
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponentiation")

#Selection of choice and user input 
choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5]:"))

num1 = as.integer(readline(prompt="Enter first number: "))

operator <- switch(choice,"+","-","*","/","^")

# result condition from user input and printing result

result <- switch(choice, Addition(num1, num2), Subtraction(num1, num2), Multiplication(num1, num2), Division(num1, num2),Exponentiation(num1,num2))
print(paste(num1, operator, num2, "=", result))