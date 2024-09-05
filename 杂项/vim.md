```cpp file:"vim"
# x
删除一个字符 ** Press  x  to delete the character under the cursor. **
# i or a
.....
# u 
撤回命令结果 ** Press  u  to undo the last commands,   U  to fix a whole line. **
# U 
撤回一整行结果 
# CTRL+R
撤回u/U命令的结果
# CTRL+G
显示文件信息 光标信息 
# CTRL+U CTRL+D
U向上半屏  D向下半屏
# A （区分大小写）
行末追加 ** Press  A  to append text. **
# d 
+w 删除单词 ** Type  dw  to delete a word. **
+e 删除光标 
+$ 删除整行 ** Type  d$  to delete to the end of the line. **
{
	d   motion
	Where:
	d      - is the delete operator.
	motion - is what the operator will operate on (listed below).
	
	A short list of motions:
	w - until the start of the next word, EXCLUDING its first character.
	e - to the end of the current word, INCLUDING the last character.
	$ - to the end of the line, INCLUDING the last character.
	
	1. Type  2w  to move the cursor two words forward.
	2. Type  3e  to move the cursor to the end of the third word forward.
	3. Type  0  (zero) to move to the start of the line.
}

# p
粘贴删除的数据 ** Type  p  to put previously deleted text after the cursor. **
# r
+字母 替换当前字母 ** Type  rx  to replace the character at the cursor with  x . **
# c
+e 删除当前光标后的单词并进入插入模式 ** To change until the end of a word, type  ce . **
# gg
光标移动到文件头部
# G 
光标移动到文件末尾
# %
移动到( or [ or { 的匹配位置  ** Type  %  to find a matching ),], or } . **

```