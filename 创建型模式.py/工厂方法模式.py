from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei == True:
            print("花呗支付了{0}元!".format(money))
        else:
            print("支付宝余额支付了{0}元!".format(money))

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付了%d元!" % (money))

class BankPay(Payment):
    def pay(self, money):
        print("银行支付了%d元!" % (money))

# 创建产品的工厂类的接口
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# 工厂类
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

# 工厂类
class WechatPayPayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

# 工厂类
class HuabeiPayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

# 新增加银行支付的工厂类
class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()

bfp = BankPayFactory().create_payment()
bfp.pay(100)  # 银行支付了100元!