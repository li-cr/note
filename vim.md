```cpp file:"vim"
# x
删除一个字符 ** Press  x  to delete the character under the cursor. **
# i or a
.....
# u 
撤回命令结果 ** Press  u  to undo the last commands,   U  to fix a whole line. **
# A （区分大小写）
行末追加 ** Press  A  to append text. **
# d 
+w 删除单词 ** Type  dw  to delete a word. **
+e 删除光标 
+$ 删除整行 ** Type  d$  to delete to the end of the line. **

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
```