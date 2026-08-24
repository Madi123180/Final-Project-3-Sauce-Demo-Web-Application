# Sauce Demo Test Automation — Python Selenium

A complete, production-ready test automation project targeting [SauceDemo](https://www.saucedemo.com), covering login, cart, checkout, end-to-end.

- Page Object Model (POM)
- Data-driven testing(external file (FP3Data.xlsx))
- Keyword-driven testing(external file (KeywordDrivenFP3.xlsx))
- Allure Reporting
- html Reporting

---

## 1. Project Structure

```
HR Management FP2
├── pages/                      <- Page Object Model
│   ├── AddProductToCart.py
│   ├── Checkout.py
│   ├── LoginPage.py
│   ├── Logout.py
│   ├── ProductSelection.py
│   ├── ResetAppState.py
│   └── SortOption.py
│   
├── TestCases/                    
│   ├── test_AddProductToCart.py
│   ├── test_Checkout.py
│   ├── test_InvalidLogin.py
│   ├── test_LoginPage.py
│   ├── test_ProductSelection.py
│   ├── test_ResetAppState.py
│   └── test_SortOption.py
├── UTIL/
│   ├── __init__.py
│   └── XLUtils.py
├── reports /                                <- generated reports 
│   ├── allure-addproductreport
│   ├── allure-checkoutreport
│   ├── allure-invalidloginreport
│   ├── allure-loginpagereport
│   ├── allure-productselectionreport
│   ├── allure-resetappreport
│   └── allure-sortoptionreport
├── allure-results
├── screenshots                             <- generated screenshots
├── conftest.py
└── requirements.txt

```

# 2. Setup
```
pip install -r requirements.txt
```

Edge must be installed locally. `webdriver-manager` downloads the matching
Driver automatically — no manual driver setup needed


## 3. Running Tests
```
# running single test: 
python -m pytest -s  TestCases\test_LoginPage.py  

# Generating allure report:
python -m pytest -s  TestCases\test_AddProductToCart.py --alluredir=allure-results --clean-alluredir
allure generate allure-results -o reports/allure-addproductreport --clean 

# Generating html report:
python -m pytest -s  TestCases\test_AddProductToCart.py --html=AddProductToCart.html

```





 








