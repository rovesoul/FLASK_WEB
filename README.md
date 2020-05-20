
# git方法
- echo "# FLASK_WEB" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git remote add origin https://github.com/rovesoul/FLASK_WEB.git
- git push -u origin master


后台是一个列表，从网页登录后，从这个列表随机取题目，但不重复；
我目前做法是向前端传一个后，删除一个元素，这样就能实现功能了；
但遇到一个问题，如果第二个人登录，读的还是这个列表，如果第一个人刷了10道，那第二个人就少了10个题。
我需要调整成怎么个思路实现：每个人进来后从完整的列表开始读取
