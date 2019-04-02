#Team Wilde Loops -- Patrick Ren, Abir Taheer, Derrick Chen
#IntroCS pd1
#HW23 -- Stringy Loops
#2019-03-13

#add_mult_print(a,b) takes 2 numeric inputs and prints a message like that shown below.
def add_mult_print(a,b):
    print("\"the sum of " + str(a) + " and " + str(b) + " is " + str(a+b) + "\ntheir product is " + str(a*b) + "\"")
    #\n is used for a line break, + is used to connect strings, \ before " is used to show that the " is not being used to denote a string

add_mult_print(3,6)
print("\nshould be \"the sum of 3 and 6 is 9 \ntheir product is 18\"\n\n")

#add_mult_html(a,b) takes 2 numeric inputs and returns a string of HTML code that will render as shown below.
def add_mult_html(a,b):
    return("<html><body><p>the <i>sum</i> of " + str(a) + " and " + str(b) + " is <b>" + str(a+b) + "</b><br>\ntheir <i>product</i> is <b>" + str(a*b) + "</b></p></body></html>")
    #the same as add_mult_print, but adds HTML tags in order to italicize and bold certain words.

print(add_mult_html(3,6))
print("\nshould be <html><body><p>the <i>sum</i> of 3 and 6 is <b>9</b><br>\ntheir <i>product</i> is <b>18</b></p></body></html>\n\n")

#sum_digits returns the sum of the digits in a number
def sum_digits(n):
    sumd = 0  # keeps track of the sum
    while n > 0:  # while n still has a positive integer in the ones place
        sumd = sumd + (n % 10)  # adds the current ones digit of n to sumd
        n = n // 10  # removes the ones digit of n
    return sumd

#tablefy(n) takes a positive integer input and returns a string of HTML code that will render a table like the one below.
def tablefy(n):
    html = "<html><body><table border=1><tr><th>n</th><th>n^2</th><th>sumDigits</th></tr>" #tr makes table row, th makes table(column) headings, td puts table data
    counter = 1 #starts the table with an n value of 1
    while counter <= n:
        html += "<tr><td>" + str(counter) + "</td><td>" + str(counter**2) + "</td><td>" + str(sum_digits(counter**2)) + "</td></tr>" #adds a new row to the table for the new value of the counter
        counter += 1 #adds one to the counter
    html += "</table></body></html>" #adds the table, html, body end tags after the while loop is done
    return html

print(tablefy(10))
print("\nshould be <html><body><table border=1><tr><th>n</th><th>n^2</th><th>sumDigits</th></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>4</td><td>4</td></tr><tr><td>3</td><td>9</td><td>9</td></tr><tr><td>4</td><td>16</td><td>7</td></tr><tr><td>5</td><td>25</td><td>7</td></tr><tr><td>6</td><td>36</td><td>9</td></tr><tr><td>7</td><td>49</td><td>13</td></tr><tr><td>8</td><td>64</td><td>10</td></tr><tr><td>9</td><td>81</td><td>9</td></tr><tr><td>10</td><td>100</td><td>1</td></tr></table></body></html>")