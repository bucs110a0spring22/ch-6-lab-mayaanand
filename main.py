import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: count (int) the number of iterations until n =1
    """
    count = 0
    while(n != 1):
        if(n % 2) == 0:       # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count += 1
    return count
def drawGraph(iteration):
  ''' Draws graph on x-axis that is a positive integer,and gives the number of iterations it takes until the integer is 1
      args: iteration (int) how many times the loop repeats, the upper bound
      return: none
  '''
  grapher = turtle.Turtle()
  grapher.speed(0)
  grapher.up()
  grapher.goto(0,0)
  grapher.down()

  writer = turtle.Turtle()
  writer.speed(0)
  
  wn = turtle.Screen()
  wn.setworldcoordinates(0,0,10,10)

  max_so_far = 0

  for i in range(1, iteration + 1):
    result = seq3np1(i)
    

    if result > max_so_far:
      max_so_far = result
      writer.clear()
      writer.up()
      writer.goto(0, max_so_far)
      string = "Maximum so far: " + str(max_so_far)
      writer.write(string)

    wn.setworldcoordinates(0, 0, i + 10, max_so_far + 10)
    grapher.goto(i, result)

  wn.exitonclick()
  
def main():
  upper = int(input("Please enter an upper bound for the function: "))
  start = 1
  while (start < upper):
    start += 1
    drawGraph(upper)
main()