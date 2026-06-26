<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

<h1>An Inference-Based Analysis of Gender Differences in Salary</h1>

<div class="section">
  <h2>Overview</h2>
  <p>
    This project performs a full statistical analysis of gender-based salary differences using real-world inspired employee data.
    It combines exploratory data analysis, hypothesis testing, and regression modeling to quantify salary disparity and evaluate its statistical significance.
    The pipeline is implemented using NumPy (custom OLS), SciPy, Pandas, Matplotlib, and Seaborn.
  </p>
</div>

<div class="section">
  <h2>Objective</h2>
  <p>To investigate whether a statistically significant gender-based salary gap exists while controlling for:</p>
  <ul>
    <li>Age</li>
    <li>Years of Experience</li>
    <li>Education Level</li>
    <li>Job Title</li>
  </ul>
  <p><b>Source:</b> Kaggle Salary Dataset</p>
</div>

<div class="section">
  <h2>Dataset Summary</h2>
  <div class="box">
    <p><b>Shape:</b> 1780 rows × 6 columns</p>

    <h3>Gender Distribution</h3>
    <p>Male: 966</p>
    <p>Female: 814</p>

    <h3>Average Salary by Gender</h3>
    <p>Female: 107,294.8</p>
    <p>Male: 118,056.2</p>

    <h3>Education Levels</h3>
    <p>High School, Bachelor’s, Master’s, PhD</p>
  </div>
</div>

<div class="section">
  <h2>Statistical Results</h2>

  <h3>Welch’s T-Test</h3>
  <ul>
    <li>t-statistic: 4.4121</li>
    <li>p-value: 1.1e-05</li>
    <li>Mean difference: 10,761.4</li>
    <li>95% CI: (5,977.55, 15,545.25)</li>
    <li><b>Result:</b> Significant gender difference (Reject H₀)</li>
  </ul>

  <h3>F-Test</h3>
  <ul>
    <li>F-statistic: 1.0435</li>
    <li>p-value: 0.2646</li>
    <li><b>Result:</b> No variance difference (Fail to reject H₀)</li>
  </ul>

  <h3>OLS Regression</h3>
  <ul>
    <li>R²: 0.8748</li>
    <li>Adjusted R²: 0.859</li>
    <li>Male coefficient: 1908.6</li>
    <li>p-value: 0.0656</li>
    <li><b>Result:</b> No significant gender effect after controls</li>
  </ul>
</div>

<h2>EDA Visualizations</h2>
<img width="400" height="400" alt="Screenshot 2026-06-26 164337" src="https://github.com/user-attachments/assets/4a1e0b33-4446-4ab5-8126-b0220f02b22d" />
<img width="400" height="350" alt="Screenshot 2026-06-26 164320" src="https://github.com/user-attachments/assets/24802fbc-dd58-4d4e-a100-5cb7fb5a54f7" />
<img width="400" height="400" alt="Screenshot 2026-06-26 164307" src="https://github.com/user-attachments/assets/4f8fa7e0-6c4c-409a-9e56-098d2e3e611f" />
<img width="400" height="350" alt="Screenshot 2026-06-26 164252" src="https://github.com/user-attachments/assets/53f8c673-d1e8-4bce-817d-ae8468a3090e" />
<img width="400" height="350" alt="Screenshot 2026-06-26 164236" src="https://github.com/user-attachments/assets/d138e898-aeee-4633-830d-da80ffd0af9d" />
<img width="400" height="400" alt="Screenshot 2026-06-26 164221" src="https://github.com/user-attachments/assets/3ff4a5a3-af87-4184-a94a-3a5f55fdead1" />
<div class="section">
  <h2>Key Insight</h2>
  <p>
    A significant raw gender pay gap exists, but after controlling for education, experience, and job role,
    the gender effect becomes statistically insignificant. This suggests the gap is largely explained by other factors.
  </p>
</div>


</body>
</html>
