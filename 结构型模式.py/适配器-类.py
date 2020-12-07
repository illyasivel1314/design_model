from abc import ABCMeta, abstractmethod

# 目标接口
class Payment(object, metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print('支付了%d' % money)

# 待适配的类
class BankPay():
    def cost(self, money):
        print('银联支付了%d' % money)

# 类适配器
class PaymentAdapter(Payment, BankPay):
    """
    把不兼容cost转换成pay
    """

    def pay(self, money):
        self.cost(money)

p = PaymentAdapter()
p.pay(100)
"""
银联支付了100
"""