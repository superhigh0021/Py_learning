from decimal import Decimal as dm
class SymbolAndProbability:
    symbol ='x'
    probability ='0'
    left ='0'
    right ='0'

    #构造函数
    def _init_(self, symbol, probability, left, right):
        self.symbol = symbol
        self.probability = probability
        self.left = left
        self.right = right

    #算数编码
    def arithmetic_code(symbol_str, arr):
        # 将输⼊字符串转化为数组
        count_fIrst =int(symbol_str.count(arr[1].symbol))
        symbol_arr =[]
        for index in range(0,len(symbol_str)):
            symbol_arr.append(symbol_str[index])
        #初始化,length为1, start b为0
        length ='1.0'
        start_b ='0'
        print("\n>>>算术编码过程如下：")
        for x_index in range(0,len(symbol_arr)):
            # 和字典匹配，如果匹配到，就编码
            for y_index in range(1,len(arr)):
                if symbol_arr[x_index]== arr[y_index].symbol:
                    start_n = dm(start_b)+ dm(arr[y_index].left)* dm(length)
                    end_n = dm(start_b)+ dm(arr[y_index].right)* dm(length)
                    length = dm(end_n)- dm(start_n)
                    start_b = dm(start_n)
                    print("symbol", symbol_arr[x_index],"startN",format(start_n,'.30f'),"endN",format(end_n,'.30f'),"L",format(length,'.30f'))
                    break
                    #匹配不到说明输入符号有问题,退出!
                if y_index ==len(arr)-1and symbol_arr[x_index]!= arr[y_index].symbol:
                    print(">>>error! 输⼊符号中有字典中未存储符号")
                    exit(0)
            #返回区间左端点作为编码结果
        return dm(start_n), count_fIrst

    #算数解码
    def arithmetic_decode(end_code, arr, count_First):
        print("\n>>>算术解码为：")
        str_for_count =''
        for x_index in range(1,len(arr)):
            if dm(arr[x_index].left)<= dm(end_code)< dm(arr[x_index].right):
                last = x_index
                print(arr[x_index].symbol, end='')
                if arr[x_index].symbol == arr[1].symbol:
                    str_for_count += arr[x_index].symbol
                break
        while dm(end_code)!= dm('0'):
            end_code = dm((dm(end_code)- dm(arr[last].left))/ dm(dm(arr[last].right)- dm(arr[last].left)))
            for x_index in range(1,len(arr)):
                if dm(arr[x_index].left)<= dm(end_code)< dm(arr[x_index].right):
                    last = x_index
                    print(arr[x_index].symbol, end='')
                    if arr[x_index].symbol == arr[1].symbol:
                        str_for_count += arr[x_index].symbol
                    break
        if str_for_count.count(arr[1].symbol)< count_First:
            print(arr[1].symbol*(count_First - str_for_count.count(arr[1].symbol)))
        return

    #打印输⼊内容
    def class_print_all(arr):
        print("\n>>>输⼊符号，对应概率和编码区间为：")
        for x_index in range(1,len(arr)):
            print("symbol:'", arr[x_index].symbol,"' probability:", arr[x_index].probability,"  区间→[", arr[x_index].left,",", arr[x_index].right,")")

    #输入概率和符号
    def symbol_probability_input(self):
        #spli('str')函数会将字符串 str切掉，如果两个str中间没有非空字符（ strstr)，则空字符为分割结果，利用此原理，输入空格。
        print(">>>输⼊符号，以空格隔开\n[注]符号中有空格，例如要输⼊[' ','a',' ','b',' ']，应该这样输⼊：_a__b_\n    即输⼊符号“空格”时，它和前⾯字符以空格隔开，后⾯则不需要")
        symbol =input().split(' ')
        symbol_string =''
        #如果是空字符，就将其变为空格
        for str_index in range(0,len(symbol)):
            if symbol[str_index]=='':
                symbol[str_index]=' '
            symbol_string += symbol[str_index]
        #检查输入符号是否重复？
        for rpt_index in range(0,len(symbol_string)):
            if symbol_string.count(symbol[rpt_index])>1:
                print(">>>error！输⼊了重复符号")
                exit(0)
        probability =input(">>>输⼊概率，以空格隔开\n").split(' ')
        #检查概率完备性及输⼊情况
        sum_p =0
        for x_index in range(0,len(probability)):
            sum_p += dm(probability[x_index])
        if abs(sum_p -1)>1e-4:
            print("error! 概率不具有完备性！")
            exit(0)
        if len(symbol)!=len(probability):
            print("error! 输⼊符号数⽬与概率数⽬不匹配")
            exit(0)
        arr =[]
        init = SymbolAndProbability(symbol='zero', probability='0', left='0', right='0')
        #arr第一个元素〔下标为O)存放有关初始化的操作
        arr.append(init)
        for x_index in range(1,len(probability)+1):
            # 当前的符号，准备存⼊实体类
            syb = symbol[x_index -1]
            # 当前的概率，准备存⼊实体类
            pb = probability[x_index -1]
            # 当前的区间左端点为前⼀区间的右端点，准备存⼊实体类
            left = arr[x_index -1].right
            # 实例化类
            new_element = SymbolAndProbability(symbol=syb, probability=pb, left=left, right=dm(left)+ dm(pb))
            arr.append(new_element)
        return arr

if __name__ =='__main__':
    ss = SymbolAndProbability()
    # 输⼊符号和概率
    array_sy_pb =  ss.symbol_probability_input()
    # 打印具体信息
    ss.class_print_all(array_sy_pb)
    # 获得算术编码结果
    code_end, count_first = ss.arithmetic_code(str(input("\n输⼊字符串（不需要使⽤空格隔开）\n")), array_sy_pb)
    # 算术编码解码
    ss.arithmetic_decode(code_end, array_sy_pb, count_first)