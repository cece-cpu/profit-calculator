def calculate_profit(selling_price, purchase_cost, shipping_cost, platform_fee):
    profit = selling_price - purchase_cost - shipping_cost - platform_fee
    profit_margin = profit / selling_price * 100
    return profit, profit_margin


print("跨境商品利润计算器")
print("--------------------")

try:
    selling_price = float(input("请输入商品售价："))
    purchase_cost = float(input("请输入采购成本："))
    shipping_cost = float(input("请输入运费："))
    platform_fee = float(input("请输入平台费用："))

    if selling_price <= 0:
        print("输入错误：商品售价必须大于 0。")
    else:
        profit, profit_margin = calculate_profit(
            selling_price,
            purchase_cost,
            shipping_cost,
            platform_fee
        )

        print("商品售价：", selling_price, "元")
        print("预计利润：", profit, "元")
        print("预计利润率：", round(profit_margin, 2), "%")

        if profit_margin >= 20:
            print("分析结果：利润率较好，可以继续评估。")
        elif profit_margin > 0:
            print("分析结果：有利润，但利润率偏低。")
        else:
            print("分析结果：商品可能亏损。")

except ValueError:
    print("输入错误：请输入数字，例如 100 或 99.5。")