import os
import schedule
import time

# 切换到本地仓库目录
os.chdir("/Users/chenjuan/Documents/person/learn/python/emm")


# 定义一个函数，用于向 a.txt 中追加一行 "helloworld"，并提交代码到 Github 仓库
def append_line():
    with open("a.txt", "a") as f:
        f.write("hello world\n")
    # 添加所有文件到 Git
    os.system("git add .")
    # 提交代码
    os.system("git commit -m 'automatic commit' --author='chenjun <cchenjuan@163com>'")
    # 推送到远程仓库
    os.system("git push")


# 每天 12:00 执行一次 append_line 函数
# schedule.every().day.at("12:00").do(append_line)
if __name__ == "__main__":
    append_line()
    # sech
    # while True:
    #     # 每隔 1 分钟检查一次是否需要执行定时任务
    #     schedule.run_pending()
    #     time.sleep(60)
