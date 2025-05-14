
读书实践周—git
Git与代码版本管理学习笔记
一、学习资料来源
1.	官方文档：
•	Git官方文档：https://git-scm.com/doc
•	GitHub官方指南：https://guides.github.com/
•	Gitee官方帮助：https://gitee.com/help
2.	在线教程：
•	廖雪峰的Git教程：https://www.liaoxuefeng.com/wiki/896043488029600
•	菜鸟教程Git教程：https://www.runoob.com/git/git-tutorial.html
•	阮一峰的Git教程：https://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html
3.	视频资源：
•	B站Git教程合集：https://www.bilibili.com/video/BV1Xx411m7kn
•	慕课网Git实战教程：https://www.imooc.com/learn/208
4.	推荐书籍：
•	《Pro Git》中文版（免费电子书）：https://git-scm.com/book/zh/v2
•	《Git权威指南》- 蒋鑫
•	《Git版本控制管理》- Jon Loeliger
二、实践流程
1. 本地安装配置Git
首先从Git官网下载并安装最新版本的Git。安装过程中保持默认选项即可，但需要注意以下几点：
1.	选择默认编辑器（我选择了VS Code）
2.	配置行结束符转换（选择"Checkout as-is, commit Unix-style line endings"）
安装完成后，在命令行中运行以下命令进行基本配置：
bash
复制
git config --global user.name "vertleo"
git config --global user.email "2338615482@qq.com"
2. 创建本地仓库
git init
  
  
3. 注册远程仓库账号并创建仓库
我选择了GitHub平台：
1.	GitHub：
 
主页链接：Your Repositories
  
排序算法链接（py）：algorithm/sort at master · virtleo/algorithm
 
  
 
Django框架学习：virtleo/Django
四、学习心得
1. 版本控制的必要性
通过本次实践，我深刻认识到版本控制系统的重要性。在没有使用Git之前，我的项目文件夹中常常充斥着"final-v1"、"final-v2"、"really-final"等命名的文件副本，不仅占用空间，而且难以管理。Git通过精确的版本记录和高效的存储机制，彻底解决了这个问题。
2. 分布式版本控制的优势
Git的分布式特性让我可以在本地完整地进行版本控制，不受网络限制。即使在没有互联网连接的情况下，我仍然可以提交更改、创建分支、查看历史记录。这种灵活性极大提高了开发效率。
3. 工作流程的理解
我学习了三种常见的工作流程：
1.	集中式工作流：类似SVN，所有开发者在一个主分支上工作
2.	功能分支工作流：每个新功能在独立分支上开发，完成后合并到主分支
3.	Git Flow：更复杂的分支模型，包含master、develop、feature、release和hotfix分支
经过实践，我认为对于个人项目和小型团队，功能分支工作流已经足够；而对于大型项目，Git Flow可能更为合适。
4. 团队协作的规范
Git虽然强大，但也需要团队制定规范才能发挥最大效益。我认识到：
•	提交信息应该清晰明确，遵循约定格式
•	分支命名应该有统一规则
•	代码审查（Pull Request）是保证质量的重要环节
•	定期同步远程仓库可以避免复杂的合并冲突
5. 进阶功能的探索
在学习基础操作后，我还探索了一些进阶功能：
•	交互式暂存（git add -p）：可以选择性地暂存文件的特定修改
•	储藏（git stash）：临时保存工作目录的修改，方便切换分支
•	重置（git reset）与回滚（git revert）的区别与应用场景
•	子模块（git submodule）：管理项目依赖
•	钩子（hooks）：自动化执行脚本
6. 持续学习的必要性
Git生态系统不断发展，GitHub、GitLab等平台也在不断推出新功能。我意识到需要持续学习，例如：
•	GitHub Actions自动化工作流
•	Git LFS管理大文件
•	代码审查工具的使用
•	项目管理与issue跟踪的集成
五、总结与建议
通过这次Git学习实践，我不仅掌握了基本的版本控制技能，还培养了良好的代码管理习惯。Git作为现代软件开发的核心工具，其重要性怎么强调都不为过。
最后，感谢学校安排这次实践任务，让我有机会系统地学习Git。我会继续完善我的Git技能，并将其应用到未来的学习和工作中。

