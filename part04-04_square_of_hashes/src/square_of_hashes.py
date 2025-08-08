# Copy here code of line function from previous exercise
def line(integer,string):
    x = integer * string
    print(x)
def square_of_hashes(size):
    y = size
    # You should call function line here with proper parameters
    while size > 0:
        line(y, "#")
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
