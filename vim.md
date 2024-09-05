```cpp file:"vim"
# x
删除一个字符 ** Press  x  to delete the character under the cursor. **
# i or a 
.....
# A （区分大小写）
行末追加 ** Press  A  to append text. **
# d 
+w 删除单词 ** Type  dw  to delete a word. **
+e 删除光标后的单词
+$ 删除整行 ** Type  d$  to delete to the end of the line. **

d   motion
Where:
d      - is the delete operator.
motion - is what the operator will operate on (listed below).

A short list of motions:
w - until the start of the next word, EXCLUDING its first character.
e - to the end of the current word, INCLUDING the last character.
$ - to the end of the line, INCLUDING the last character.
```