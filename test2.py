#文件和异常
#Python内置的open函数，可以指定文件名、操作模式、编码信息来获得操作文件的对象。
#操作模式是指要打开什么样的文件（字符文件还是二进制文件）
#'r' 读  'w' 写入 'x' 写入，如果文件已经存在会异常 'a' 追加 'b'二进制模式 't'文本模式 '+' 更新(可以读可以写)

#读写文本文件
def main():
    f = open('爱打架李开复.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()