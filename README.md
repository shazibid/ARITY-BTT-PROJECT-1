# Classification of Vehicle Turns from Telematic Data
---

### 👥 **Arity 1B Team Members**

| Name             | GitHub Handle | Contribution                                                                                |
|------------------|---------------|--------------------------------------------------------------------------                   |
| Shazi Bidarian   | [@shazibid](https://github.com/shazibid)| Data exploration, visualization, project coordination, state 1 + 2 unsupervised modeling    |
| Connie Yang      | [@connieyyy](http://github.com/connieyyy)| Data exploration, project coordination, state 0 unsupervised modeling, documentation         |
| Kelly Pham       | [@kllyph](https://github.com/kllyph)| Data preprocessing, supervised learning with random forest                                  |
| Jaewon Kim       | [@CanDoJaewon](https://github.com/CanDoJaewon)| Data exploration, label matching                                                            |

---

## 🎯 **Project Highlights**
- Developed a machine learning model using `K-Means, DBSCAN,` and `HDBSCAN` to classify turns.
- Achieved `96%` accuracy for random forest model, demonstrating `consistency of replication of modeling results` for `Arity`.

---

## 👩🏽‍💻 **Setup and Installation**
1. Install the following prerequisites:\
a. `Python 3.8+`\
b. `Git`

2. Clone the repo

3. Set up virtual environment

4. Install dependencies

5. Verify installation

6. Open in VS Code and run notebooks

7. Open the workspace in VS Code

8. Select the Python kernel (.venv environment)

9. Start with raw.ipynb to understand the data and explore state0, state1/, state2/ for analysis by driving state

## Project Structure
- **Data/**
  - **Raw/** → untouched iOS & Android data
  - **Processed/** → cleaned + split datasets
- **Notebooks/** → EDA + experiments
- **SRC/** → finalized scripts (data cleaning, modeling)
- **Results/** → plots, metrics, reports
- **README.md** → project overview + instructions

---

## 🏗️ **Project Overview**

**Describe:**

- Arity collects user driving data with consent and safe drivers get a lower rate on their insurance policies
- Use AI/ML to classify data points into different types of turns
- Use telematics data to classify vehicle turning behaviors
- Cluster models to distinguish different types of turns
- Create a supervised model to classify vehicle turns

---

## 📊 **Data Exploration**
* 20 MB dataset, dictionary structure and CSV format
* Plotted data points with matplotlib and seaborn
* Removed outliers with interquartile method

  
<img width="476" height="167" alt="Screenshot 2025-12-10 at 2 10 25 PM" src="https://github.com/user-attachments/assets/015a1eb2-7aa7-4af1-b303-ec7f96b3b36c" />
<img width="439" height="233" alt="Screenshot 2025-12-10 at 1 43 43 PM" src="https://github.com/user-attachments/assets/41f53298-ee94-468d-b698-80e8763c0abc" />

---

## 🧠 **Model Development**
* Model(s) used: K-Means, HDBSCAN, DBSCAN, and Random Forest
---

## 📈 **Results & Key Findings**
* 96% accuracy score with random forest modeling

<img width="444" height="203" alt="Screenshot 2025-12-10 at 2 31 18 PM" src="https://github.com/user-attachments/assets/46d62f87-3148-4423-b503-cca30ffe8f07" />
<img width="458" height="213" alt="Screenshot 2025-12-10 at 2 31 35 PM" src="https://github.com/user-attachments/assets/55ffa1ed-24de-4ec0-ae12-34c5dff12fff" />
<img width="466" height="207" alt="Screenshot 2025-12-10 at 2 31 48 PM" src="https://github.com/user-attachments/assets/d7447d91-90d5-4d4b-a9aa-6d09cdd60eb0" />
<img width="470" height="189" alt="Screenshot 2025-12-10 at 2 31 57 PM" src="https://github.com/user-attachments/assets/1c87ecda-698c-48d5-b488-d0bba0b547fe" />

---

## 🚀 **Next Steps**
- We want to focus on optimizing the supervised model to ensure it generalizes well and is ready for deployment. This includes applying techniques such as **grid search** or **randomized search** to systematically explore hyperparameter combinations, using cross‑validation, and tuning parameters like tree depth, minimum samples per leaf, and the number of estimators to balance accuracy with robustness. 
- We can also compare Random Forest with other ensemble methods such as Gradient Boosting, and analyze feature importance to understand which inputs drive cluster predictions most strongly. 

---

## 📝 **License**
This project is licensed under the MIT License.

---

## 📄 **References**
[Presentation Slides](https://docs.google.com/presentation/d/16cA-imadbY--9Ssgt-z4tKh-O-mydWV8oQi8I51cVWY/edit?usp=sharing)

---

## 🙏 **Acknowledgements** 

Thank you to our advisor, **Francesco De Bernardis**, and coach, **Matt Brems** who supported our project.
