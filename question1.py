from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def fetch_forex_rate(date, currency_code):
    driver = webdriver.Chrome()

    # 货币代号到中文名称的映射
    currency_map = {
        "USD": "美元",
        "EUR": "欧元",
        "JPY": "日元",
        # 添加其他需要支持的货币及其中文名称
    }

    currency_name = currency_map.get(currency_code, "")
    if not currency_name:
        print(f"Unsupported currency code: {currency_code}")
        return

    try:
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "erectDate"))
        )

        # 输入查询日期
        date_input = driver.find_element(By.ID, "erectDate")
        date_input.clear()
        date_input.send_keys(date)

        # 选择货币
        currency_select = driver.find_element(By.ID, "pjname")
        for option in currency_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == currency_name:  # 这里需要确保currency_code是中文货币名称
                option.click()
                break

        # 定位所有搜索按钮
        search_buttons = driver.find_elements(By.CLASS_NAME, "search_btn")

        # 点击第二个搜索按钮
        if len(search_buttons) > 1:
            search_buttons[1].click()  # 点击第二个按钮
        else:
            print("Second search button not found.")
            return

        # 获取现汇卖出价
        # 等待表格数据加载完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "BOC_main"))
        )

        # 定位到表格
        table = driver.find_element(By.CLASS_NAME, "BOC_main")

        # 获取所有行
        rows = table.find_elements(By.TAG_NAME, "tr")

        row=rows[1]
        cols = row.find_elements(By.TAG_NAME, "td")  # 定位行中的所有单元格
        if cols:  # 如果找到了单元格（非标题行）
            currency_name = cols[0].text  # 货币名称
            sell_rate = cols[3].text  # 现汇卖出价
            print(f"Currency: {currency_name}, Sell Rate: {sell_rate}")

        with open("result.txt", "w") as file:
            file.write(sell_rate)

        print(sell_rate)

    except Exception as e:
        print("Error fetching forex rate:", e)
    finally:
        driver.quit()
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 question1.py <YYYYMMDD> <CurrencyCode>")
    else:
        date = sys.argv[1]
        currency_code = sys.argv[2]
        fetch_forex_rate(date, currency_code)
    

    #fetch_forex_rate('20211231' , 'USD')
