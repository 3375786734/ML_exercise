
#定义两个伪目标,make的时候可以选build/test
.PHONY: build test
build: mylib.a
CFLAGS = -I test 

VPATH = test
mylib.a: my_math.o my_print.o
	ar crv mylib.a my_math.o my_print.o
%.o: %.cpp
	g++ -c $<
# $<代表.cpp  $@ 代表.o


#my_math.o: my_math.cpp
#	g++ -c my_math.cpp

#my_print.o: my_print.cpp
#	g++ -c my_print.cpp

#选择编译得到.out文件
test: a.out

a.out: test.cpp
	g++ $< -L. mylib.a

.PHONY: clean
clean:

