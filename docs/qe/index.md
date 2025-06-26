# # Notes for Quantitative Economics

- 宏观仿真与预测:
  - Computational Macroeconomics-DSGE方法
  - Agent-Based Models in Economics-Judd等（ABM框架）
  - Quantitative Macroeconomic Modeling with Python(Battaglia等)

## 📚 阅读路线（组合经济学和计算方法）

### 🔹 阶段 1：建立基础（可跳读部分内容）

* 《Recursive Methods in Economic Dynamics》— DP思想 + 宏观建模的骨架
* 《Quantitative Macroeconomics with Python》— 模型代码复现实践
* 《A Course in Macro Modeling and Forecasting》— IMF 的开源教材，用 R 或 EViews 做政策预测

### 🔹 阶段 2：政策模拟与现代模型

* 《Dynamic Economics》— Adda & Cooper，案例导向型的政策模拟书
* 《Handbook of Computable General Equilibrium Modeling》— 政府/世界银行类机构常用
* 学术综述文章：
  * “Deep Reinforcement Learning in Macroeconomics”
  * “Agent-Based Macroeconomics: A Survey”

### 🔹 阶段 3：AI+经济前沿

* AI Economist 项目论文（斯坦福 & Salesforce）
* Fernández-Villaverde 等人关于“用RL求解DSGE”的论文
* 你的 RL 知识可以完全在这里“跨界重用”

---

## 三、🧪 项目路线（构建个人作品集）

### ✅ 项目 1：宏观指标预测器

> 模仿 IMF/WEO 样式，构建自己的 GDP/通胀/失业预测模型

* 工具：Python + FRED API + statsmodels + Plotly
* 加分点：做成 Web 页面 + 自动数据更新 + 可视化图表

---

### ✅ 项目 2：DSGE 小型政策模拟器

> 构建一个可以切换政策参数的小型 DSGE 模型（利率规则、政府支出规则）

* 工具：Dynare + Python 或 Julia（QuantEcon）
* 加分点：带交互式前端（用 Streamlit 或 Jupyter Widgets）

---

### ✅ 项目 3：宏观强化学习实验

> 训练一个 RL 智能体，模拟“央行”如何在不同通胀与产出情景下调整利率

* 工具：PyTorch + Gym + Matplotlib
* 建议起点：离散状态储蓄模型（Stochastic Growth + RL 策略学习）
* 加分点：写解说博客或视频，把“政策函数”可视化讲清楚

---

### ✅ 项目 4：YouTube / Newsletter 系列

> 把你读书 + 实验 + 仿真结果系统化输出

* 格式：宏观建模讲解、政策模型拆解、图像化经济趋势
* 示例标题：“为什么加息抗通胀有时会失败？用模型跑给你看”
* 加分点：项目代码都开源在 GitHub，附上仿真小论文和可视化图
