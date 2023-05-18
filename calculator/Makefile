objects = main.o addition.o subtraction.o multiplication.o division.o
oper = operations.h

calculator: $(objects)
        cc -o calculator $(objects) $(oper)
    
$(objects): %.o:.c
        cc -c $< -o $@
 
 clean:
    rm -f $(objects)

.PHONY: all
