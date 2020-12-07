from abc import ABCMeta, abstractmethod


# 抽象产品角色，以什么样的表现去使用
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# 产品角色
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei == True:
            print("花呗支付了{0}元!".format(money))
        else:
            print("支付宝余额支付了{0}元!".format(money))

# 产品角色
class WechatPay(Payment):
    def pay(self, money):
        print("微信支付了%d元!" % (money))

# 工厂类角色
class PaymentFactory:
    def ctreate_payment(self, method):
        if method == 'Alipay':
            return Alipay()
        elif method == 'WechatPay':
            return WechatPay()
        elif method == 'HuabeiPay':
            return Alipay(use_huabei=True)
        else:
            raise TypeError('No such payment named %s' % method)

# 客户端调用。不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例
pf = PaymentFactory()
p = pf.ctreate_payment('HuabeiPay')
p.pay(100)
q = pf.ctreate_payment('Alipay')
q.pay(200)